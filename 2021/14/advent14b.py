import fileinput
from collections import Counter

STEP_COUNT = 40

insertion_rules = dict()

def main():
     line_input = fileinput.input()

     polymer = line_input.readline().strip()
     # Throw away the blank second line
     line_input.readline()
     
     # The rest are insertion rules.
     for line in line_input:
          sandwich, meat = line.strip().split(' -> ')
          insertion_rules[sandwich] = meat

     for _ in range(STEP_COUNT):
          print(_)
          polymer_next = ''
          for i in range(len(polymer)-1):
               # Check each pair, and if it's a valid insertion,
               #  put in the first part of the pair and the insertion.
               # Otherwise just put in the current character in the
               #  existing polymer chain.
               pair = polymer[i:i+2]
               polymer_next += pair[0]
               if pair in insertion_rules:
                    polymer_next += insertion_rules[pair]
          # Add the last character, which the loop didn't pick up.
          polymer_next += polymer[-1]
          polymer = polymer_next
     
     # Our solution is count(most common letter) - count(least common)
     polymer_counts = Counter(polymer).most_common()
     print(polymer_counts[0][1] - polymer_counts[-1][1])
     
if __name__ == '__main__':
     main()
