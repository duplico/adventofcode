import sys
import string
import re

from collections import deque

instruction_match_str = r'move (?P<count>\d+) from (?P<src>\d+) to (?P<dest>\d+)'

def setup():
     pass

def part1(filename):
     stack_lines = []
     with open(filename) as f:
          while True:
               line = f.readline()
               if line.strip()[0] in string.digits:
                    stack_count = len(line.split())
                    break
               stack_lines.append(line)

          # Initialize a stack for each column
          stack = dict()
          for i in range(stack_count):
               stack[i+1] = deque()
          
          # Load up the initial stacks with the lines we already read:
          for line in stack_lines:
               for col in range(stack_count):
                    char = line[1+4*col]
                    if char != ' ':
                         # Add to the BEGINNING (like a reverse push)
                         stack[col+1].appendleft(char)
          
          # Throw away the blank line::
          f.readline()

          # The remaining lines are our instructions.
          for line in f.readlines():
               matches = re.match(instruction_match_str, line)
               count, src, dest = map(int, matches.groups())

               # Manipulate the stacks according to the instructions:
               while count:
                    count -= 1
                    stack[dest].append(stack[src].pop())
          
          # Finally, pop every stack and smash them together in order:
          print(''.join(map(deque.pop, (stack[i+1] for i in range(stack_count)))))

def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
