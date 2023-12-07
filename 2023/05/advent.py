import sys
from dataclasses import dataclass

@dataclass
class Mapping:
     src_start: int
     dst_start: int
     range_len: int
     
     def in_range(self, i):
          return i >= self.src_start and i < self.src_start + self.range_len

     def mapping(self, i):
          if self.in_range(i):
               return self.dst_start + i - self.src_start
          else:
               return i

maps = []

def setup():
     pass

def finalvalue(val_cur: int):
     _maps = maps.copy()

     while _maps:
          map_cur = _maps.pop(0)
          for map in map_cur:
               if map.in_range(val_cur):
                    val_cur = map.mapping(val_cur)
                    break
     return val_cur


def part1(filename):
     seeds = []
     map_cur = []
     global maps
     for line in open(filename):
          line = line.strip()

          # Blank lines are skipped.
          if not line:
               continue

          if line.startswith('seeds'):
               # The seed list.
               seeds = list(map(int, line.split()[1:]))
          elif line.endswith('map:'):
               # It's a new map.
               if map_cur:
                    maps.append(map_cur)
               map_cur = []
          else:
               # It's a range.
               dst_start, src_start, count = map(int, line.split())
               map_cur.append(Mapping(src_start=src_start, dst_start=dst_start, range_len=count))
     maps.append(map_cur)
     
     print(seeds)
     print(min(list(map(finalvalue, seeds))))

     # seeds.sort(key=finalvalue)
          

def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
