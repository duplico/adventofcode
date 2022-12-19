import sys
from functools import cmp_to_key

def setup():
     pass

class CorrectOrder(Exception):
     pass

def cmp1(left, right):
     if type(left) == int and type(right) == int:
          return left-right
     
     if type(left) == int:
          left = [left]
     if type(right) == int:
          right = [right]

     # Both sides are now lists.
     for k in range(len(left)):
          if k >= len(right):
               # right list ran out of items first
               return 1 # left is larger.
          val = cmp1(left[k], right[k])
          if val == 0:
               continue
          return val
     # Left list ran out of items.
     # Were they the same size?
     if len(left) == len(right):
          return 0
     return -1 # Right is larger.

def part1(filename):
     index = 1

     correct_indices = []

     with open(filename) as f:
          while True:
               try:
                    p1 = eval(f.readline().strip())
               except SyntaxError: # EOF
                    break
               p2 = eval(f.readline().strip())
               cmp = cmp1(p1, p2)
               if cmp < 0:
                    correct_indices.append(index)
               index += 1
               f.readline()
     print(correct_indices)
     print(sum(correct_indices))

def part2(filename):
     index = 1
     all_packets = []
     for line in open(filename):
          if not line.strip():
               continue
          all_packets.append(eval(line))
     all_packets.append([[2]])
     all_packets.append([[6]])

     all_packets.sort(key=cmp_to_key(cmp1))

     decoder = all_packets.index([[2]])+1
     decoder *= all_packets.index([[6]])+1

     print(decoder)

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
