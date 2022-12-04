import sys
import bisect

def main(filename):
     calories = []
     running_cals = 0

     for line in open(filename):
          if line.strip():
               running_cals += int(line.strip())
          else:
               calories.append(running_cals)
               running_cals = 0
     
     calories.append(running_cals)
     calories.sort()

     print(sum(calories[-3:]))


if __name__ == '__main__':
     main(sys.argv[1])
