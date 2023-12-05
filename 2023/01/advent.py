import sys

digit_spellings = dict(
     one=1,
     two=2,
     three=3,
     four=4,
     five=5,
     six=6,
     seven=7,
     eight=8,
     nine=9,
     zero=0
)

def setup():
     pass

def part1(filename):
     cal = 0
     for line in open(filename):
          line_digits = [ch for ch in line if ch.isdigit()]
          cal += int(line_digits[0])*10 + int(line_digits[-1])
     print(cal)


def part2(filename):
     cal = 0
     for line in open(filename):
          line_digits = []
          for i in range(len(line)):
               if line[i].isdigit():
                    line_digits.append(int(line[i]))
               else:
                    for spelling, digit in digit_spellings.items():
                         if line[i:].startswith(spelling):
                              line_digits.append(digit)
          cal += int(line_digits[0])*10 + int(line_digits[-1])
     print(cal)


if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
