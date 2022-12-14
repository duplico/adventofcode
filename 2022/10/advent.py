import sys

def setup():
     pass

def part1(filename):
     TEST_CYCLES = [20, 60, 100, 140, 180, 220]

     signal_str = 0
     cycle = 0
     x = 1

     for line in open(filename):
          instr = line.strip().split()
          
          # It just so happens that an instruction takes cycles equal to the
          #  the number of tokens it produces on a split, so take advantage
          #  of that to increment the clock.
          for _ in range(len(instr)):
               cycle += 1
               if cycle in TEST_CYCLES:
                    signal_str += cycle*x

          # Handle the addx instruction.
          if instr[0] == 'addx':
               x += int(instr[1])
     
     print(signal_str)

          

def part2(filename):
     screen = [[]]

     cycle = 0
     x = 1

     for line in open(filename):
          instr = line.strip().split()

          # It just so happens that an instruction takes cycles equal to the
          #  the number of tokens it produces on a split, so take advantage
          #  of that to increment the clock.
          for _ in range(len(instr)):
               xpos = cycle % 40
               if xpos == 0:
                    screen.append([])
               if x in [xpos-1, xpos, xpos+1]:
                    screen[cycle//40].append('#')
               else:
                    screen[cycle//40].append('.')

               cycle += 1

          # Handle the addx instruction.
          if instr[0] == 'addx':
               x += int(instr[1])
     
     for l in screen[:-1]:
          print(''.join(l))

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
