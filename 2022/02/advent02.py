import sys

ROCK =     1
PAPER =    2
SCISSORS = 3

def game_result_score(opponent, me):
     if opponent == me:
          # Draw
          return 3
     elif (opponent % 3) + 1 == me:
          # 2 beats 1, 3 beats 2, 1 beats 3
          return 6
     else:
          return 0

def part1(filename):
     translation = dict(
          A=ROCK, X=ROCK,
          B=PAPER, Y=PAPER,
          C=SCISSORS, Z=SCISSORS
     )

     running_score = 0

     for line in open(filename):
          running_score += translation[line[2]]
          running_score += game_result_score(
               translation[line[0]],
               translation[line[2]]
          )
     print(running_score)


def part2(filename):
     pass

if __name__ == '__main__':
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
