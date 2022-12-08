import sys

def setup():
     pass

def part1(filename):
     # Read the whole stream into a buffer.
     with open(filename) as f:
          stream = f.readline().strip()
     
     # Use built-in set type cast to remove duplicates and compare size to original.
     window_pos = 4
     while len(set(stream[window_pos-4:window_pos])) != len(stream[window_pos-4:window_pos]):
          window_pos += 1
     
     # When did we bail?
     print(window_pos)

def part2(filename):
     # Read the whole stream into a buffer.
     with open(filename) as f:
          stream = f.readline().strip()
     
     # Use built-in set type cast to remove duplicates and compare size to original.
     window_pos = 14
     while len(set(stream[window_pos-14:window_pos])) != len(stream[window_pos-14:window_pos]):
          window_pos += 1

     # When did we bail?
     print(window_pos)

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
