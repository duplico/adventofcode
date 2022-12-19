import sys
import types
from typing import ClassVar, Dict

from dataclasses import dataclass

from sympy.ntheory import factorint

def add(a, b): 
     return a+b

def mul(a, b): 
     return a*b

class WorryNumber():
     def __init__(self, num: int = 0, factors: dict = None):
          if factors:
               self.factors = factors
          else:
               self.factors = factorint(num)
     
     def val(self):
          v = 1
          for factor, exp in self.factors.items():
               v *= factor**exp
          return v

     def add(self, num: 'WorryNumber'):
          return WorryNumber(self.val() + num.val())
          
     def mul(self, num: 'WorryNumber'):
          factors = self.factors.copy()
          for factor, product in num.factors.items():
               factors.setdefault(factor, 0)
               factors[factor] += product
          return WorryNumber(factors=factors)
     
     def divides(self, divisor):
          # DIVISOR MUST BE PRIME.
          return divisor in self.factors

     def __repr__(self):
          return(repr(self.factors))
          # return repr(self.val())

@dataclass(order=True, kw_only=True)
class Monkey():
     all_monkeys: ClassVar[Dict[int, 'Monkey']] = dict()

     inspected_count: int = 0

     num: int
     items: list
     operation: str
     operand: int
     divisor: int
     true_dest: int
     false_dest: int

     def __post_init__(self):
          Monkey.all_monkeys[self.num] = self
          self.operand_worry = -1 if self.operand == -1 else WorryNumber(self.operand)
          for i in range(2,self.divisor):
               if self.divisor % i == 0:
                    raise ValueError("Invalid non-prime divisor %d in monkey %d." % (self.divisor, self.num))

     def take_turn(self, debug=False, div_by_3=True):
          assert self.true_dest != self.num
          assert self.false_dest != self.num

          if debug:
               print('Monkey %d' % self.num)

          for item in self.items:
               self.inspected_count += 1
               
               # Monkey inspects an item with worry level of item
               # Worry level is self.operation-ed by self.operand
               operand = item if self.operand_worry == -1 else self.operand_worry
               if self.operation == '*':
                    # mult
                    worry_level = item.mul(operand)
               else:
                    worry_level = item.add(operand)
               
               if debug:
                    print(' Monkey inspects an item with a worry level of %d' % item.val())
                    print('  Worry level is %s by %d to %d' % (str(self.operation), 
                                                               item.val() if self.operand == -1 else self.operand,
                                                               worry_level.val()))

               if div_by_3:
                    # Monkey gets bored with item. Worry level is divided by 3.
                    worry_level = WorryNumber(num = worry_level.val() // 3)
                    if debug:
                         print('  Monkey gets bored with item. Worry level is divided by 3 to %d' % worry_level.val())

               # Test worry level against self.divisor:
               if worry_level.divides(self.divisor):
                    Monkey.all_monkeys[self.true_dest].items.append(worry_level)
                    if debug:
                         print('  Item with worry level %d is thrown to monkey %d' % (worry_level.val(), self.true_dest))
               else:
                    Monkey.all_monkeys[self.false_dest].items.append(worry_level)
                    if debug:
                         print('  Item with worry level %d is thrown to monkey %d' % (worry_level.val(), self.false_dest))

          self.items = []
     
     def __str__(self) -> str:
          return 'Monkey %d inspected items %d times' % (self.num, self.inspected_count)

def setup(filename):
     with open(filename) as f:
          while True:
               l = f.readline()
               # Break if we've run out of monkeys
               if not l:
                    break

               # Read the values from each line, without using regex.
               num = int(l.strip().split()[1][:-1])
               items = list(map(int, f.readline().strip().split(maxsplit=2)[2].split(',')))

               operator, operand = f.readline().strip().split()[-2:]

               # operator = mul if operator == '*' else add
               operand = -1 if operand == 'old' else int(operand)
               
               test_divisor = int(f.readline().strip().split()[-1])
               true_target = int(f.readline().strip().split()[-1])
               false_target = int(f.readline().strip().split()[-1])
               
               # Throw away blank line.
               f.readline()

               # Now make the monkey.
               _ = Monkey(
                    num=num,
                    items=list(map(WorryNumber, items)),
                    operation=operator,
                    operand=operand,
                    divisor=test_divisor,
                    true_dest=true_target,
                    false_dest=false_target
               )

def part1(filename):
     # Run 20 rounds
     for round in range(20):
          # With a turn for each monkey in order.
          for monkey_no in range(len(Monkey.all_monkeys.keys())):
               Monkey.all_monkeys[monkey_no].take_turn(debug=True)
     sorted_monkeys = sorted(Monkey.all_monkeys.values())
     print(sorted_monkeys[-2].inspected_count * sorted_monkeys[-1].inspected_count)

def part2(filename):
     for round in range(20):
          # With a turn for each monkey in order.
          for monkey_no in range(len(Monkey.all_monkeys.keys())):
               Monkey.all_monkeys[monkey_no].take_turn(debug=False, div_by_3=False)
     sorted_monkeys = sorted(Monkey.all_monkeys.values())

     print(list(map(lambda a: (a.num, a.inspected_count), Monkey.all_monkeys.values())))

     print(sorted_monkeys[-2].inspected_count * sorted_monkeys[-1].inspected_count)

if __name__ == '__main__':
     setup(sys.argv[2])
     if sys.argv[1] == '1':
          part1(sys.argv[2])
     else:
          part2(sys.argv[2])
