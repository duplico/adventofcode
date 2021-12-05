import fileinput
from collections import namedtuple

digit_map = {
     2: 1,
     3: 7,
     4: 4,
     7: 8,
}

def known_digit(digit: str) -> bool:
     if len(digit) in digit_map:
          return True
     return False

def main():
     known_digit_count = 0
     for line in fileinput.input():
          ten_digits, output_digits = line.split(' | ')
          ten_digits = ten_digits.split()
          output_digits = output_digits.split()
          for output_digit in output_digits:
               if known_digit(output_digit):
                    known_digit_count += 1
    
     print(f"Known output digit count: {known_digit_count}")

if __name__ == '__main__':
    main()
