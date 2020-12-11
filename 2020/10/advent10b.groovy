// Handle reading the file path from the command line, and do some
//  VERY BASIC input validation.
def input_path = "sample_input.txt"

if (args.size() > 1) {
     println("Incorrect usage.")
     println("Expected: advent10b [path_to_file.txt]")
} else if (args.size() == 0) {
     println("Assuming default input sample_input.txt")
} else {
     input_path = args[0]
}

// Load the lines from the file into a list, and sort it in
//  DESCENDING order, as we'll be starting from the laptop
//  this time.
def joltages = new File(input_path).collect {it as Integer}

joltages.sort() { -it }
joltages << 0 // Add 0 to the list because that's our ultimate goal.

// This will be a dictionary of how many ways we can reach each
//  joltage value. Our ultimate answer will be how many ways to
//  reach joltage 0.
// There is only one way to reach the highest-joltage adapter, and
//  that is directly from our laptop.
def waysToReach = [:]
waysToReach.put(joltages[0], 1)

// Now, load up all the rest of our joltages into waysToReach:
joltages[1..<joltages.size()].each {
     waysToReach.put(it, 0l)
}

// For each joltage adapter, in descending order:
joltages.each {
     // Consider joltages between 1 and 3 jolts (inclusive)
     //  below the current adapter's joltage.
     for (nextJoltage in (it-3)..<it) {
          // If it's >= 0 and in our list, then it's a joltage we need
          //  to consider.
          if (nextJoltage >= 0 && waysToReach.containsKey(nextJoltage)) {
               waysToReach[nextJoltage] += waysToReach[it]
          }
     }
}

println("Ways to reach 0: ${waysToReach[0]}")
