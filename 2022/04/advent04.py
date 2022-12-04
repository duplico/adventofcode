import sys
import re

def setup():
     pass

def part1(filename):
     contained_count = 0
     for line in open(filename):
          start1,end1,start2,end2 = tuple(map(int, re.split('-|,', line.strip())))
          if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
               contained_count += 1
     print(contained_count)

def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
