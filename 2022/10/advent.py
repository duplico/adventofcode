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
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
