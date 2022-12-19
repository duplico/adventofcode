import sys

from string import ascii_lowercase as lowers

import networkx as nx

def setup():
     pass

def reachable1(src, dest):
     src = src.replace('S','a').replace('E','z')
     dest = dest.replace('S','a').replace('E','z')
     
     if src == 'z':
          return True

     maxdest = lowers[lowers.index(src)+1]

     return dest <= maxdest     

def part1(filename):
     offsets = [ (-1, 0), (1, 0), (0, -1), (0, 1)]

     terrain = nx.DiGraph()

     terrain_strs = []
     for line in open(filename):
          terrain_strs.append(line.strip())
     
     rows = len(terrain_strs)
     cols = len(terrain_strs[0])

     for r in range(rows):
          for c in range(cols):
               for dr, dc in offsets:
                    if r+dr < 0 or r+dr >= rows or c+dc < 0 or c+dc >= cols:
                         continue
                    if reachable1(terrain_strs[r][c], terrain_strs[r+dr][c+dc]):
                         terrain.add_edge(
                              (r,c),
                              (r+dr,c+dc)
                         )
                    if terrain_strs[r][c] == 'S':
                         start_pos = (r,c)
                    elif terrain_strs[r][c] == 'E':
                         end_pos = (r,c)

     print(nx.shortest_path_length(terrain, start_pos, end_pos))


def part2(filename):
     offsets = [ (-1, 0), (1, 0), (0, -1), (0, 1)]

     terrain = nx.DiGraph()
     candidate_starts = []

     terrain_strs = []
     for line in open(filename):
          terrain_strs.append(line.strip().replace('S','a'))
     
     rows = len(terrain_strs)
     cols = len(terrain_strs[0])

     for r in range(rows):
          for c in range(cols):
               for dr, dc in offsets:
                    if r+dr < 0 or r+dr >= rows or c+dc < 0 or c+dc >= cols:
                         continue
                    if reachable1(terrain_strs[r][c], terrain_strs[r+dr][c+dc]):
                         terrain.add_edge(
                              (r,c),
                              (r+dr,c+dc)
                         )
                    
                    if terrain_strs[r][c] == 'a':
                         candidate_starts.append((r,c))
                    elif terrain_strs[r][c] == 'E':
                         end_pos = (r,c)

     lens = []
     for start_pos in candidate_starts:
          try:
               lens.append(nx.shortest_path_length(terrain, start_pos, end_pos))
          except nx.NetworkXNoPath:
               continue
     print(sorted(lens)[0])

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
