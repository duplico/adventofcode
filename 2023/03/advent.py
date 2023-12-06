import sys

def setup():
     pass

def part1(filename):
     parts = 0
     lines = []
     for line in open(filename):
          lines.append(line.strip())
     
     for row in range(len(lines)):
          col = 0
          line = lines[row]     
          number_string = ''
          is_part = False
          while True:
               if line[col].isdigit():
                    number_string += line[col]
                    if not is_part:
                         for dr in (-1,0,1):
                              for dc in (-1,0,1):
                                   try:
                                        if lines[row+dr][col+dc] != '.' and not lines[row+dr][col+dc].isdigit():
                                             is_part = True
                                   except IndexError:
                                        pass # Ignore index out of bounds.
               
               if number_string and (col+1 == len(line) or not line[col].isdigit()):
                    # The number is over.
                    if is_part:
                         parts += int(number_string)
                    number_string = ''
                    is_part = False

               col += 1
               if col == len(line):
                    break
     print(parts)

def part2(filename):
     gears = dict()
     lines = []
     for line in open(filename):
          lines.append(line.strip())
     
     for row in range(len(lines)):
          col = 0
          line = lines[row]     
          number_string = ''
          gear_coords = set()
          while True:
               if line[col].isdigit():
                    number_string += line[col]
                    for dr in (-1,0,1):
                         for dc in (-1,0,1):
                              try:
                                   if lines[row+dr][col+dc] == '*':
                                        gear_coords.add((row+dr, col+dc))
                              except IndexError:
                                   pass # Ignore index out of bounds.
               
               if number_string and (col+1 == len(line) or not line[col].isdigit()):
                    # The number is over.
                    for coord in gear_coords:
                         gears.setdefault(coord, [])
                         gears[coord].append(int(number_string))
                    gear_coords = set()
                    number_string = ''

               col += 1
               if col == len(line):
                    break
     gear_total = 0
     for parts in gears.values():
          if len(parts) == 2:
               gear_total += parts[0] * parts[1]
     print(gear_total)

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
