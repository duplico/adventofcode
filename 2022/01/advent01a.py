import sys

def main(filename):
     most_calories = 0
     running_cals = 0

     for line in open(filename):
          if line.strip():
               running_cals += int(line.strip())
          else:
               if running_cals > most_calories:
                    most_calories = running_cals
               running_cals = 0
     
     if running_cals > most_calories:
          most_calories = running_cals
     
     print(most_calories)


if __name__ == '__main__':
     main(sys.argv[1])
