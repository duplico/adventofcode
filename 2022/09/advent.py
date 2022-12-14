import sys
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def setup():
     pass

def next_point1(head, tail):
     x = tail.x
     y = tail.y

     # If they're overlapping or neighboring (including diagonally),
     #  don't move!
     if abs(head.y - tail.y) <= 1 and abs(head.x - tail.x) <= 1:
          return tail

     # If we're here, we know we need to move.

     if head.x == tail.x and abs(head.y - tail.y) > 1: # Left/right
          y += 1 if head.y > tail.y else -1
     elif head.y == tail.y and abs(head.x - tail.x) > 1: # Up/down
          x += 1 if head.x > tail.x else -1
     else: # Diagonal! Do both!
          y += 1 if head.y > tail.y else -1
          x += 1 if head.x > tail.x else -1

     return Point(x, y)

def part1(filename):
     head = Point(0, 0)
     tail = Point(0, 0)
     visited_points = set([tail])
     
     for line in open(filename):
          dir, dist = line.strip().split()
          dist = int(dist)

          for _ in range(dist):
               if dir == 'R':
                    head = head._replace(x=head.x+1)
               elif dir == 'L':
                    head = head._replace(x=head.x-1)
               elif dir == 'U':
                    head = head._replace(y=head.y+1)
               elif dir == 'D':
                    head = head._replace(y=head.y-1)
               tail = next_point1(head, tail)
               visited_points.add(tail)
     
     print(len(visited_points))


def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
