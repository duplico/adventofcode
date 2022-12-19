import sys

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

move_order = [
     Point(0,1),
     Point(-1,1),
     Point(1,1)
]

class SandSettled(Exception):
     pass

class SandMoved(Exception):
     pass

class SandOffMap(Exception):
     pass

def setup():
     pass

def part1(filename):
     material_coords = []
     
     left_side = 500
     right_side = 500
     depth = 0

     for line in open(filename):
          toks = line.strip().split('->')
          for i in range(1, len(toks)):
               # Draw the line between toks[i-1] and toks[i]
               x1,y1 = map(int, toks[i-1].strip().split(','))
               x2,y2 = map(int, toks[i].strip().split(','))

               assert x1==x2 or y1==y2

               depth = max(depth, y1, y2)
               left_side = min(left_side, x1, x2)
               right_side = max(right_side, x1, x2)

               for x in range(min(x1,x2), max(x1,x2)+1):
                    material_coords.append(Point(x,y1))
               
               for y in range(min(y1,y2), max(y1,y2)+1):
                    material_coords.append(Point(x1,y))

     sand_count = 0     
     try:
          while True: # Generate infinite sand.
               sand_pos = Point(500,0)
               try:
                    while True: # Move the sand piece down
                         try:
                              for move in move_order:
                                   candidate_pos = Point(
                                        x = sand_pos.x + move.x,
                                        y = sand_pos.y + move.y
                                   )
                                   if candidate_pos.y > depth or candidate_pos.x < left_side or candidate_pos.x > right_side:
                                        raise SandOffMap()
                                   if candidate_pos not in material_coords:
                                        # Sand can move there.
                                        sand_pos = candidate_pos
                                        raise SandMoved()
                              # If we're here, we tried every move, and none were valid.
                              # So the sand has settled.
                              raise SandSettled()
                         except SandMoved:
                              continue # Continue trying to move the sand.
               except SandSettled:
                    material_coords.append(sand_pos)
                    sand_count += 1
                    continue # Continue the sand-generation loop.
     except SandOffMap:
          pass # We're done.

     print(sand_count)


def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
