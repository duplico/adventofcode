import sys

def setup():
     pass

def part1(filename):
     with open(filename) as f:
          stream = f.readline().strip()
     
     window_pos = 4
     while len(set(stream[window_pos-4:window_pos])) != len(stream[window_pos-4:window_pos]):
          window_pos += 1
     print(window_pos)

def part2(filename):
     with open(filename) as f:
          stream = f.readline().strip()
     
     window_pos = 14
     while len(set(stream[window_pos-14:window_pos])) != len(stream[window_pos-14:window_pos]):
          window_pos += 1
     print(window_pos)

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
