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
     translation = dict(
          A=ROCK, X=2,
          B=PAPER, Y=0,
          C=SCISSORS, Z=1
     )

     running_score = 0

     for line in open(filename):
          op_choice = translation[line[0]]
          my_choice = op_choice + translation[line[2]]
          if my_choice > 3:
               my_choice -= 3
          
          running_score += my_choice + game_result_score(op_choice, my_choice)
          
     print(running_score)

if __name__ == '__main__':
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
