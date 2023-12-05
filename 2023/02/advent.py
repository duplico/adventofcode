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
          id = int(toks[1][:-1])
          new_set = False
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
                    new_set = True
               else:
                    new_set = True
               
               this_set[color] = cnt
               
               if new_set:
                    print(id, pos, this_set)
                    if this_set['blue'] > 14 or this_set['red'] > 12 or this_set['green'] > 13:
                         break

                    this_set = dict(
                         blue=0,
                         red=0,
                         green=0
                    )
                    new_set = False
               
               pos += 2
               if pos > len(toks):
                    total += id
                    break
     print(total)

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
