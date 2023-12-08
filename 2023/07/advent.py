import sys

FIVE_OF_A_KIND=6
FOUR_OF_A_KIND=5
FULL_HOUSE=4
THREE_OF_A_KIND=3
TWO_PAIR=2
PAIR=1
HIGH_CARD=0

def hand_face_value(hand: str):
     has_3 = False
     has_2 = False
     for card in set(hand):
          if hand.count(card) == 5:
               return FIVE_OF_A_KIND
          if hand.count(card) == 4:
               return FOUR_OF_A_KIND
          if hand.count(card) == 3:
               if has_2:
                    return FULL_HOUSE
               has_3 = True
               continue
          if hand.count(card) == 2:
               if has_2:
                    return TWO_PAIR
               elif has_3:
                    return FULL_HOUSE
               has_2 = True
               continue
     if has_3:
          return THREE_OF_A_KIND
     if has_2:
          return PAIR
     return HIGH_CARD
          

def hand_tie_breaker_value(hand: str):
     hex_hand = hand.replace('A', 'e').replace('K', 'd').replace('Q', 'c').replace('J', 'b').replace('T','a')
     hex_hand = str(hand_face_value(hand)) + hex_hand
     return int(hex_hand, 16)


def setup():
     pass

def part1(filename):
     hands = dict()
     for line in open(filename):
          hand, bid = line.split()
          hands[hand] = int(bid)
     
     score = 0
     rank = 1
     for hand in sorted(hands.keys(), key=hand_tie_breaker_value):
          score += hands[hand] * rank
          rank += 1
     print(score)

def part2(filename):
     pass

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
