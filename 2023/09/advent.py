import sys

def setup():
     pass

ZERO_SET = set([0])

def next_val(l : list):
     if set(l) == ZERO_SET:
          return 0
     
     return l[-1] + next_val(list(
          l[i] - l[i-1] for i in range(1, len(l))
     ))

def part1(filename):
     next_val_total = 0

     for line in open(filename):
          vals = list(map(int, line.strip().split()))
          next_val_total += next_val(vals)

     print(next_val_total)

def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
