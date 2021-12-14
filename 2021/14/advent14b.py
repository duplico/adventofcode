import fileinput
from collections import Counter, defaultdict

STEP_COUNT = 40

insertion_rules = dict()

def main():
     line_input = fileinput.input()

     # First line is the initial polymer
     polymer = line_input.readline().strip()
     # Throw away the blank second line
     line_input.readline()
     
     # The rest are insertion rules.
     for line in line_input:
          sandwich, meat = line.strip().split(' -> ')
          insertion_rules[sandwich] = meat

     # Load up a dictionary with counts of all the pairs in the polymer:
     polymer_pairs = defaultdict(lambda: 0)
     for i in range(len(polymer)-1):
          pair = polymer[i:i+2]
          polymer_pairs[pair] += 1

     # Repeatedly update the polymer_pairs dict STEP_COUNT times:
     for _ in range(STEP_COUNT):
          polymer_pairs_next = defaultdict(lambda: 0)

          for pair, count in polymer_pairs.items():
               insertion = insertion_rules[pair]
               # print(f"Replacing {count} pairs of {pair} with {pair[0]+insertion} and {insertion+pair[1]}")
               polymer_pairs_next[pair[0]+insertion] += count
               polymer_pairs_next[insertion+pair[1]] += count
          polymer_pairs = polymer_pairs_next

     # Now get the count of every polymer, by looking at the first item in every pair.
     polymer_counts = defaultdict(lambda: 0)
     for pair, count in polymer_pairs.items():
          polymer_counts[pair[0]] += count
     # The method above skips the very last polymer in the chain, so
     #  add it separately:
     polymer_counts[polymer[-1]] += 1

     # Generate a list of the polymers, in the order of least to most common.
     ordered_counts = sorted(polymer_counts.keys(), key=polymer_counts.get)
     # Our solution is count(most common letter) - count(least common)
     print(polymer_counts[ordered_counts[-1]] - polymer_counts[ordered_counts[0]])

     
if __name__ == '__main__':
     main()
