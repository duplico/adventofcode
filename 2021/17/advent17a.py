import fileinput
import re
import math

match_str = r'^target area: x=(-?[0-9]+)\.\.(-?[0-9]+), y=(-?[0-9]+)\.\.(-?[0-9]+)$'

def y_reaches(v0, y_dest):
     y = 0
     v = v0

     assert y_dest < 0

     while y > y_dest:
          y += v0
          v0 -= 1
     
     return y == y_dest

def main():
     m = re.match(match_str, fileinput.input().readline().strip())
     # x0, x1, y0, y1 = re.match(match_str, fileinput.input().readline().strip())
     x0, x1, y0, y1 = map(int, [m.group(1), m.group(2), m.group(3), m.group(4)])

     # I'm inclined to ignore X entirely, since the only question we have is: how high can we go?

     # So the question is: for each value y in y0..y1, what's the highest parabola that
     #  passes through that y-value?

     # The high point, with positive v0_y as starting velocity, is (v0_y*(v0_y+1))/2

     # I really know there's a formula for this, but I can't figure it out.
     # I think it has to do with trying to find a root for the parabola related to
     #  the lowest point in the target square.

     vmax = 0
     for v_candidate in range(y0*y0): # Why this range?
          if y_reaches(v_candidate, y0):
               vmax = v_candidate
     print((vmax*(vmax+1))/2)


if __name__ == '__main__':
     main()
