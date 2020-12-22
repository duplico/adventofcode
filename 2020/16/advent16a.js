"use strict";

const readline = require('readline');
const fs = require('fs');
let fields = []

function readField(line) {
     const fieldsRegex = /^(?<fieldname>.+): (?<min1>\d+)-(?<max1>\d+) or (?<min2>\d+)-(?<max2>\d+)$/;
     const fieldMatches = line.match(fieldsRegex)
     if (fieldMatches == null) {
          console.error("Error on input: " + line)
          process.exit(1)
     }

     fieldMatches.groups.min1 = parseInt(fieldMatches.groups.min1);
     fieldMatches.groups.min2 = parseInt(fieldMatches.groups.min2);
     fieldMatches.groups.max1 = parseInt(fieldMatches.groups.max1);
     fieldMatches.groups.max2 = parseInt(fieldMatches.groups.max2);

     fields.push(fieldMatches.groups)
}

/// Returns true if val is a valid value for ANY field.
function fieldValid(val) {
     return fields.some(field => (field.min1 <= val && val <= field.max1) ||
                                 (field.min2 <= val && val <= field.max2))
}

/// Totals the values of invalid values in line's fields.
function ticketErrors(line) {
     let invalidSum = 0
     let entries = line.split(",").map(n => parseInt(n));
     entries.forEach(function(entry) {
          if (!fieldValid(entry)) {
               invalidSum += entry;
          }
     });
     
     return invalidSum;
}

async function main(filepath) {
     const readInterface = readline.createInterface({
          input: fs.createReadStream(filepath),
          // output: process.stdout,
          console: false
     });

     let phase = 0
     let errorCount = 0

     for await (const line of readInterface) {
          if (line == "your ticket:" || line == "nearby tickets:") {
               phase++;
               continue;
          }
          
          if (line == "") {
               continue;
          }

          switch (phase) {
               case 0: // Reading fields
                    readField(line);
                    break;
               case 1: // Reading my ticket
                    break;
               case 2: // Reading nearby tickets
                    errorCount += ticketErrors(line)
                    break;
          }
     }

     console.log("Error count: " + errorCount)
}

if (require.main === module) {
     if (process.argv.length == 3) {
          main(process.argv[2]);
     } else if (process.argv.length < 3) {
          main("sample_input.txt");
     } else {
          console.error("Expected: node advent16a.js [sample_input.txt]")
          process.exit(1)
     }
}
