import sys

def setup():
     pass

def part1(filename):
     trees = []
     for line in open(filename):
          trees.append(line.strip())
     
     visible_tress = set()

     for row in range(len(trees)):
          tallest = -1
          # Left to right:
          for col in range(len(trees[row])):
               tree = int(trees[row][col])
               if tree > tallest:
                    tallest = tree
                    visible_tress.add((row, col))
          tallest = -1
          # Right to left:
          for col in range(len(trees[row]))[::-1]:
               tree = int(trees[row][col])
               if tree > tallest:
                    tallest = tree
                    visible_tress.add((row, col))

     for col in range(len(trees[0])):
          tallest = -1
          # Top to bottom:
          for row in range(len(trees[col])):
               tree = int(trees[row][col])
               if tree > tallest:
                    tallest = tree
                    visible_tress.add((row, col))
          tallest = -1
          # Bottom to top
          for row in range(len(trees[col]))[::-1]:
               tree = int(trees[row][col])
               if tree > tallest:
                    tallest = tree
                    visible_tress.add((row, col))
                    
     print(len(visible_tress))


def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
