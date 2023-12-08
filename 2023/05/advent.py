import sys
from pprint import pprint
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

@dataclass
class SeedRange:
     range_start: int
     range_cnt: int

     def range_end(self):
          return self.range_start + self.range_cnt - 1

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
               seeds_numbers = list(map(int, line.split()[1:]))
               for i in range(0, len(seeds_numbers), 2):
                    seeds.append(SeedRange(
                         range_start=seeds_numbers[i],
                         range_cnt=seeds_numbers[i+1]
                    ))
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

     # Pop the first seed_range and dst_map
     # While True:
     #  Is our seed range fully less than src range? Add it to next_seeds and pop seed_range.
     #  Is our seed range fully more than src range? Keep it, and pop dst_map
     #  Is our seed range is partially below the src map? Split it, adding the lower part to next_seeds, keeping the rest.
     #  Is our seed range is partially above the src map? Split it, keeping the overlap and pushing the rest onto seeds
     #  Else, our seed range is fully within the src map. Apply the src:dst map, add it to next_seeds, and pop seeds.

     next_seeds = seeds

     while maps:
          # And, look at sources, sorted by sources
          curr_maps = sorted(maps.pop(0), key=lambda a: a.src_start, reverse=True) # We want smallest last
          seeds = sorted(next_seeds, key=lambda a: a.range_start, reverse=True) # We want smallest last

          # pprint(seeds) 
          # pprint(curr_maps)

          # List to hold the subsequent resource value ranges
          next_seeds = []

          dst_map = curr_maps.pop()
          seed_range = seeds.pop()
          while True:
               # Is the seed range fully less than dst_map's sources?
               # print('Considering:')
               # pprint(seed_range)
               # pprint(dst_map)
               if seed_range.range_end() < dst_map.src_start:
                    # print("Preserving unmapped range.")
                    next_seeds.append(seed_range) # The numbers don't update.
                    # Next seeds, please.
                    if seeds:
                         seed_range = seeds.pop()
                         continue
                    else:
                         # No seeds left. We're done here.
                         break

               # Is the seed range fully above dst_map's sources?
               if seed_range.range_start > dst_map.src_start + dst_map.range_len-1:
                    # The seeds have gotten higher than the useful values of this mapping. Move on to the next.
                    # print("Moving on to next map range.")
                    if curr_maps:
                         dst_map = curr_maps.pop()
                         continue
                    else:
                         # No maps left. Need to load everything from seeds into next_seeds.
                         next_seeds.append(seed_range)
                         next_seeds += seeds
                         break
               
               # Is the seed range partially less than dst_map's sources?
               if seed_range.range_start < dst_map.src_start:
                    # print("Lower split of range.")
                    lower_partition_range = dst_map.src_start - seed_range.range_start
                    # Split the range.
                    # The earlier part goes straight into next_seeds
                    next_seeds.append(SeedRange(
                         range_start=seed_range.range_start,
                         range_cnt=lower_partition_range
                    ))
                    # The later part is for us to look at and match to dst_map, replacing the current value
                    # of seed_range:
                    seed_range = SeedRange(
                         range_start=seed_range.range_start + lower_partition_range,
                         range_cnt=seed_range.range_cnt - lower_partition_range
                    )
                    continue

               # Is the seed range partially more than dst_map's sources?
               if seed_range.range_end() > dst_map.src_start + dst_map.range_len - 1:
                    # print("Upper split of range.")
                    # Split the range. The later part goes back into the queue:
                    overlap_count = seed_range.range_end() - (dst_map.src_start + dst_map.range_len - 1)
                    seeds.append(SeedRange(
                         range_start=dst_map.src_start + dst_map.range_len,
                         range_cnt=overlap_count
                    ))
                    # And the overlapping part is an update to seed_range:
                    seed_range = SeedRange(
                         range_start=seed_range.range_start,
                         range_cnt=seed_range.range_cnt-overlap_count
                    )
                    continue

               # If we're here, the seed range is fully within dst_map.
               # We need to apply the src:dst map, add the resulting SeedRange to next_seeds, and pop seeds.
               # seed_rangs starts at src_start or higher.
               src_offset = seed_range.range_start - dst_map.src_start
               next_seeds.append(SeedRange(
                    range_start=dst_map.dst_start+src_offset,
                    range_cnt=seed_range.range_cnt
               ))
               # print("DIRECT MAP:", next_seeds[-1])
               if seeds:
                    seed_range = seeds.pop()
               else:
                    break
     # print()
     next_seeds.sort(key=lambda a: a.range_start)
     pprint(next_seeds[0].range_start)



if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
