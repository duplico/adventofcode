import sys
import string

priorities = dict()

def setup():
     i=1
     for char in string.ascii_letters:
          priorities[char] = i
          i += 1

def part1(filename):
     priority_sum = 0
     for line in open(filename):
          line = line.strip()
          half = int(len(line)/2)
          left = set(line[:half])
          right = set(line[half:])
          shared = left.intersection(right)
          priority_sum += priorities[shared.pop()]
     print(priority_sum)


def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
