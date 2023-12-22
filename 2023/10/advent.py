import sys

pipe_connections = {
     '|' : [(-1, 0), (1, 0)],
     '-' : [(0, -1), (0, 1)],
     'L' : [(-1, 0), (0, 1)],
     'J' : [(-1, 0), (0, -1)],
     '7' : [(0, -1), (1, 0)],
     'F' : [(0, 1), (1, 0)],
     '.' : [],
     'S' : []
}

inverted = {
     (-1, 0): (1, 0),
     (1, 0): (-1, 0),
     (0, -1): (0, 1),
     (0, 1): (0, -1)
}

pipe_map = []

def connects(pipe_piece, delta):
     return delta in pipe_connections[pipe_piece]

def get_delta(pipe_piece, src_delta):
     if src_delta not in pipe_connections[pipe_piece]:
          return False

     return pipe_connections[pipe_piece][1 if pipe_connections[pipe_piece][0] == src_delta else 0]

sys.setrecursionlimit(100000) # lol.
def loop_len(pipes: list, running_len: int, coords: tuple[int, int], src_delta: tuple[int, int]):
     pipe_piece = pipes[coords[0]][coords[1]]

     # Base case: loop completed.
     if pipe_piece == 'S':
          # Complete the pipe map with the appropriate piece shape.
          for pipe_piece, deltas in pipe_connections.items():
               if not deltas:
                    continue
               if pipe_map[coords[0] + deltas[0][0]][coords[1] + deltas[0][1]] != '.' and pipe_map[coords[0] + deltas[1][0]][coords[1] + deltas[1][1]] != '.':
                    pipe_map[coords[0]][coords[1]] = pipe_piece
                    break
          return running_len
     
     pipe_map[coords[0]][coords[1]] = pipe_piece
     
     # Otherwise, find what our pipe connects to.
     delta = get_delta(pipe_piece, src_delta)
     return loop_len(
          pipes,
          running_len+1,
          (coords[0] + delta[0], coords[1] + delta[1]),
          inverted[delta]
     )

def setup():
     pass

def part1(filename):
     starting_r = 0
     starting_c = -1
     pipes = []

     for line in open(filename):
          pipes.append(list(line.strip()))
          pipe_map.append(list('.'*len(line.strip())))
          if 'S' in line:
               starting_c = line.find('S')
          if starting_c == -1:
               starting_r += 1

     # We have our starting position. We need to decide which
     #  coordinates to use to start following our loop.
     
     for delta in [(1,0), (0,1), (-1, 0), (0, -1)]:
          coords = (
               starting_r + delta[0],
               starting_c + delta[1]
          )

          src_delta = inverted[delta]
          try:
               pipe_piece = pipes[coords[0]][coords[1]]
          except IndexError:
               continue
          
          if connects(pipe_piece, src_delta):
               break

     print(loop_len(
          pipes,
          1,
          coords,
          src_delta
     )/2)

def part2(filename):
     part1(filename)
     for line in pipe_map:
          print(''.join(line))

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
