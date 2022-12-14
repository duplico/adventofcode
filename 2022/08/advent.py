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

def pos_val(trees, row, col):
     val = 1

     # Look left
     v = 0
     c = col
     while c > 0:
          c -= 1
          v += 1
          if trees[row][c] >= trees[row][col]:
               break
     val *= v
     
     # Look right
     v = 0
     c = col
     while c < len(trees[0]) - 1:
          c += 1
          v += 1
          if trees[row][c] >= trees[row][col]:
               break
     val *= v

     # Look up
     v = 0
     r = row
     while r > 0:
          r -= 1
          v += 1
          if trees[r][col] >= trees[row][col]:
               break
     val *= v

     # Look down
     v = 0
     r = row
     while r < len(trees) - 1:
          r += 1
          v += 1
          if trees[r][col] >= trees[row][col]:
               break
     val *= v

     return val

def part2(filename):
     trees = []
     for line in open(filename):
          trees.append(line.strip())
     
     best_score = 0
     for r in range(len(trees)):
          for c in range(len(trees[r])):
               v = pos_val(trees, r, c)
               if v > best_score:
                    best_score = v
     
     print(best_score)

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
