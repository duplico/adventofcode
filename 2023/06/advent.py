import sys

def setup():
     pass

def part1(filename):
     prod = 1
     with open(filename) as f:
          times = list(map(int, f.readline().strip().split()[1:]))
          distances = list(map(int, f.readline().strip().split()[1:]))
     for time, max_distance in zip(times, distances):
          # distance is (time-holdtime) * hold_time.
          # Let's try a linear search for the shortest hold and longest hold that will work.
          for hold_time in range(time):
               if (time - hold_time) * hold_time > max_distance:
                    lowest_hold = hold_time
                    break
          for hold_time in reversed(range(time)):
               if (time - hold_time) * hold_time > max_distance:
                    highest_hold = hold_time
                    break
          print(highest_hold, lowest_hold, highest_hold-lowest_hold+1)
          prod *= highest_hold-lowest_hold+1
     print(prod)

def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
