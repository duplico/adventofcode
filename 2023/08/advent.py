import sys
import math

def setup():
     pass

def part1(filename):
     network = dict()
     with open(filename) as f:
          directions = list(f.readline().strip())
          f.readline()

          nodes = f.readlines()
     for line in nodes:
          src = line[0:3]
          left = line[7:10]
          right = line[12:15]

          network[src] = dict(
               L=left,
               R=right
          )
     
     curr_pos = 'AAA'
     steps = 0
     dir_i = 0

     while curr_pos != 'ZZZ':
          curr_pos = network[curr_pos][directions[dir_i]]
          steps += 1
          dir_i = (dir_i + 1) % len(directions)
     
     print(steps)

def part2(filename):
     network = dict()
     curr_nodes = set()

     with open(filename) as f:
          directions = list(f.readline().strip())
          f.readline()

          nodes = f.readlines()
     for line in nodes:
          src = line[0:3]
          left = line[7:10]
          right = line[12:15]

          network[src] = dict(
               L=left,
               R=right
          )
          if src[2] == 'A':
               curr_nodes.add(src)
     
     steps = 0
     dir_i = 0

     print(curr_nodes)
     end_steps = []

     while curr_nodes:
          steps += 1
          next_nodes = set()
          for node in curr_nodes:
               next = network[node][directions[dir_i]]
               if next[2] == 'Z':
                    end_steps.append(steps)
               else:
                    next_nodes.add(next)
          dir_i = (dir_i + 1) % len(directions)
          curr_nodes = next_nodes
     
     print(end_steps)
     print(math.lcm(*end_steps))

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
