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
     priority_sum = 0
     elf_number = 0
     for line in open(filename):
          line = line.strip()
          if not elf_number:
               shared = set(line)
          else:
               shared = shared.intersection(set(line))
          
          elf_number += 1
          if elf_number == 3:
               elf_number = 0
               priority_sum += priorities[shared.pop()]
     print(priority_sum)

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
