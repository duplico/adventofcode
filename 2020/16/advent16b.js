"use strict";

const readline = require('readline');
const fs = require('fs');
let fields = []
let fieldPossibilities = []

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

function fieldValid(field, val) {
     return (field.min1 <= val && val <= field.max1) ||
            (field.min2 <= val && val <= field.max2)
}

/// Returns true if val is a valid value for ANY field.
function anyFieldValid(val) {
     return fields.some(field => fieldValid(field, val))
     for (const field of fields) {

     }
}

function ticketHasInvalidFields(line) {
     let entries = line.split(",").map(n => parseInt(n));

     return !entries.every(anyFieldValid);
}

function sieveTicket(line) {
     let entries = line.split(",").map(n => parseInt(n));

     for (let i=0; i<entries.length; i++) {
          let j=fieldPossibilities[i].length;
          let val=entries[i];
          while (j--) {
               // Examine this field for the remaining possibilities:
               let field = fieldPossibilities[i][j];
               if (!fieldValid(field, val)) {
                    if (i == 19) {
                         console.log("Considering index " + j + " of: ");
                         console.log(fieldPossibilities[i]);
                         console.log(line);
                         console.log("Invalid field " + field.fieldname + ": " + val);
                    }
                    fieldPossibilities[i].splice(j,1);
               }
          }
     }
}

function removeAmbiguous(fieldChoices) {
     console.log(fieldChoices);
     if (fieldChoices.every(c => c.length == 1)) {
          return fieldChoices.flat();
     }

     let knownFields = []

     // Consider every field name.
     for (const field of fields) {
          // Is there a position that's currently the only option for it?
          if (fieldChoices.filter(choices => choices.includes(field.fieldname)).length == 1) {
               // Yes.
               knownFields.push(field.fieldname);
          }
     }

     // For every field with a knownField in it, clear out any of the
     //  other options.
     fieldChoices = fieldChoices.map(choices => {
          for (const knownField of knownFields) {
               if (choices.includes(knownField)) {
                    return [knownField];
               }
          }
          return choices;
     });

     // Now consider all the fields that only have one option. Delete that
     //  option from every other position, and recur.
     knownFields = fieldChoices.filter(c => c.length == 1).flat();

     return removeAmbiguous(fieldChoices.map(choices => choices.length == 1? choices : choices.filter(choice => !knownFields.includes(choice))));
}

async function main(filepath) {
     const readInterface = readline.createInterface({
          input: fs.createReadStream(filepath),
          // output: process.stdout,
          console: false
     });

     let phase = 0
     let errorCount = 0
     let mySeat;

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
                    for (let i=0; i<fields.length; i++) {
                         fieldPossibilities.push([]);
                         let fieldPoss = fieldPossibilities[i];
                         for (const field of fields) {
                              fieldPoss.push(field);
                         }
                    }
                    mySeat = line.split(",").map(n => parseInt(n));
                    break;
               case 2: // Reading nearby tickets
                    if (ticketHasInvalidFields(line)) {
                         continue;
                    }
                    // This seems to be a valid ticket, so sieve it.
                    sieveTicket(line)
                    
                    break;
          }
     }
     fieldPossibilities = fieldPossibilities.map(a => a.map(b => b.fieldname));
     let fieldNames = removeAmbiguous(fieldPossibilities);


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
