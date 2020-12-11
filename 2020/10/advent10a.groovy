// Handle reading the file path from the command line, and do some
//  VERY BASIC input validation.
def input_path = "sample_input.txt"

if (args.size() > 1) {
     println("Incorrect usage.")
     println("Expected: advent10a [path_to_file.txt]")
} else if (args.size() == 0) {
     println("Assuming default input sample_input.txt")
} else {
     input_path = args[0]
}

// Load the lines from the file into a list, and sort it in
//  ascending order.
File inputFile = new File(input_path)
def joltages = inputFile.readLines() as Integer[]
joltages.sort()

// Now, we need to count how many differences between
//  consecutive joltages are 1, and how many are 3.
//  Note that there is an implicit joltage adapter in our
//  laptop, so we start diff3 at 1. The joltage of the power
//  outlet is 0, so we start lastVal at 0 and allow our
//  loop to handle counting that one.
def diff3 = 1; // Our laptop adapter counts here.
def diff1 = 0;
def lastVal = 0;

// Count the difference distribution.
joltages.each {
     if (it - lastVal == 1) {
          diff1++
     } else if (it - lastVal == 3) {
          diff3++
     }
     lastVal = it
}

// Multiply to get the answer.
println(diff3*diff1)
