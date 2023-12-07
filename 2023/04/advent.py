import sys
from pprint import pprint
from dataclasses import dataclass

@dataclass
class Scratchcard:
     winners: list
     havers: list
     value: int = None

def setup():
     global cards
     cards = dict()

def part1(filename):
     total_points = 0

     demarc_index = 0

     for line in open(filename):
          toks = line.strip().split()
          if not demarc_index:
               demarc_index = toks.index('|')
          winners = list(map(int, toks[2:demarc_index]))
          havers = list(map(int, toks[demarc_index+1:]))
          val = 0
          for haver in havers:
               if haver in winners:
                    val = val*2 if val else 1
          total_points += val
     print(total_points)

def card_count(id):
     global cards

     if id not in cards:
          return 1
     
     card = cards[id]

     if card.value is not None:
          return card.value

     won_cards = sum([1 for haver in card.havers if haver in card.winners])
     if won_cards == 0:
          card.value = 1
          return 1
     
     my_val = 0
     for i in range(won_cards):
          my_val += card_count(id+1+i)
     card.value = my_val + 1
     
     return card.value

def part2(filename):
     global cards
     demarc_index = 0

     for line in open(filename):
          toks = line.strip().split()
          if not demarc_index:
               demarc_index = toks.index('|')
          id = int(toks[1][:-1])
          cards[id] = Scratchcard(
               winners=list(map(int, toks[2:demarc_index])), 
               havers=list(map(int, toks[demarc_index+1:]))
          )
     
     print(sum(card_count(i) for i in cards.keys()))
          

if __name__ == '__main__':
     setup()
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
