import sys

def setup():
     pass

def part1(filename):
     total_ids = 0
     failed_ids = 0
     
     limits = dict(
          blue=14,
          red=12,
          green=13,
     )

     for line in open(filename):
          toks = line.split()
          pos = 2
          id = int(toks[1][:-1])
          total_ids += id

          while pos < len(toks):
               cnt = int(toks[pos])
               color = toks[pos+1]

               if color[-1] == ',':
                    color = color[:-1]
               elif color[-1] == ';':
                    color = color[:-1]
               
               if cnt > limits[color]:
                    failed_ids += id
                    break

               pos += 2

     print(total_ids - failed_ids)
               

def part2(filename):
     total = 0
     
     for line in open(filename):
          toks = line.split()
          pos = 2
          this_set = dict(
               blue=0,
               red=0,
               green=0
          )
          
          while True:
               cnt = int(toks[pos])
               color = toks[pos+1]

               if color[-1] == ',':
                    color = color[:-1]
               elif color[-1] == ';':
                    color = color[:-1]
               
               this_set[color] = max(this_set[color], cnt)
               
               pos += 2
               if pos >= len(toks):
                    power = this_set['red'] * this_set['green'] * this_set['blue']
                    total += power
                    break
     print(total)

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
