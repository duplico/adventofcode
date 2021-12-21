import fileinput
import re
import math

match_str = r'^target area: x=(-?[0-9]+)\.\.(-?[0-9]+), y=(-?[0-9]+)\.\.(-?[0-9]+)$'

def reaches_range(vx, vy, x_dests, y_dests):
     x,y = 0,0
     y_dest_min = min(y_dests)
     x_dest_max = max(x_dests)

     while y >= y_dest_min and x <= x_dest_max:
          x += vx
          y += vy

          vy -= 1
          if vx: vx -= 1

          if x in x_dests and y in y_dests:
               return True
     return False

def main():
     m = re.match(match_str, fileinput.input().readline().strip())
     x0, x1, y0, y1 = map(int, [m.group(1), m.group(2), m.group(3), m.group(4)])

     # The lowest vx that can reach the square is:
     #  (I'm sure there's a way to math this, but I can't think of it)
     #  (the quadratic formula was so long ago...)
     vx_min = 0
     while (vx_min * (vx_min + 1))/2 < x0:
          vx_min += 1
     
     vx_max = x1

     print(vx_min, vx_max)

     v_solutions = 0
     for vx_candidate in range(vx_min, vx_max+1):
          for vy_candidate in range(y0, y0*y0): # Why this range?
               if reaches_range(vx_candidate, vy_candidate, range(x0,x1+1), range(y0,y1+1)):
                    v_solutions += 1
     print(v_solutions)


if __name__ == '__main__':
     main()
