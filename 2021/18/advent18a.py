import fileinput
import math

class Split(Exception):
     pass

class Explode(Exception):
     pass

def sf_reduce(val):
     toks = val.copy()
     exploded = True
     while exploded:
          exploded, toks = sf_explode(toks)
          if not exploded:
               split, toks = sf_split(toks)
               if split:
                    # Need to do another iteration of the loop, so set:
                    exploded = True
     return toks

def sf_explode(val):
     """Returns an exploded token string if an explosion is needed, otherwise False"""
     toks = val.copy() # TODO: in-place edits?

     nest_depth = 0

     # If any pair is nexted inside four pairs, the leftmost such pair EXPLODES.
     for pc in range(len(toks)):
          if toks[pc] == '[':
               nest_depth += 1
          elif toks[pc] == ']':
               nest_depth -= 1
          
          if nest_depth == 5:
               # Need to explode this pair.
               lval = toks[pc+1]
               rval = toks[pc+3]

               # print("Must explode", sf_to_list(toks[pc:pc+5]))
               # Our tokens are:
               # [ lval , rval ]
               #pc  +1 +2  +3 +4

               # To explode a pair, add its left value to the number to the left of
               #  the pair; and the right to the one to the right. Then replace the
               #  pair with a '0' token.

               pc_l = pc
               pc_r = pc+4
               while pc_l:
                    pc_l -= 1
                    if toks[pc_l] not in ['[', ']', ',']:
                         toks[pc_l] += lval
                         break
               while pc_r < len(toks):
                    if toks[pc_r] not in ['[', ']', ',']:
                         toks[pc_r] += rval
                         break
                    pc_r += 1

               toks_out = toks[:pc] + [0] + toks[pc+5:]
               # print(sf_to_list(toks_out))
               return True, toks_out
     return False, toks

def sf_split(val):
     toks = val.copy()
     # If any regular number is 10 or greater, the leftmost such regular number SPLITS.
     # To split a regular number n, replace it with a pair: [floor(n/2), ceil(n/2)]
     for pc in range(len(toks)):
          if toks[pc] not in ['[', ']', ','] and toks[pc] > 9:
               # Need to split.
               # print("Must split", toks[pc])
               # Replace toks[pc] with f"[{math.floor(toks[pc]/2)},{math.ceil(toks[pc]/2)}]"
               toks = toks[:pc] + sf_tokenize(f"[{math.floor(toks[pc]/2)},{math.ceil(toks[pc]/2)}]") + toks[pc+1:]
               # print(sf_to_list(toks))
               return True, toks
     return False, toks

def sf_to_list(toks):
     # NB: This is dumb and bad; do not do this:
     return eval(''.join(map(str, toks)))

def sf_magnitude(val):
     if type(val) == int:
          return val
     else:
          return 3*sf_magnitude(val[0]) + 2*sf_magnitude(val[1])

def sf_tokenize(val: str) -> list:
     toks = []
     curr_tok = ''
     for char in val:
          if char in '[],':
               if curr_tok:
                    toks.append(int(curr_tok))
                    curr_tok = ''
               toks.append(char)
          else:
               curr_tok += char
     return toks

def main():
     reader = fileinput.input()
     toks = sf_tokenize(reader.readline().strip())

     for line in reader:
          # print("left", toks)
          augend = sf_tokenize(line.strip())
          # print("right", augend)
          toks = ['['] + toks + [','] + augend + [']']
          # print('combined', sf_to_list(toks))
          toks = sf_reduce(toks)
     print(sf_to_list(toks))
     print(sf_magnitude(sf_to_list(toks)))

if __name__ == '__main__':
     main()
