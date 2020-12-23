import re

rules = dict()

def rule_regex(rule):
     if re.match('"[ab]"', rule):
          # Base case.
          return rule[1]
     else:
          # We need to split it and process sub-rules.
          or_rules = [subrule.strip() for subrule in rule.split("|")]
          or_rule_texts = []
          for or_rule in or_rules:
               or_rule_texts.append("(" + "".join([rule_regex(rules[rule_element]) for rule_element in or_rule.split()]) + ")")
          return "(" + "|".join(or_rule_texts) + ")"

def main():
     textlines = []

     reading_rules = True

     for line in open("input.txt"):
          if not line.strip():
               reading_rules = False
          
          if reading_rules:
               rule_number, rule_text = line.strip().split(': ')
               rules[rule_number] = rule_text
               pass
          else:
               textlines.append(line)
     
     master_matcher = re.compile("^" + rule_regex(rules["0"]) + "$")
     match_count = 0
     for line in textlines:
          if master_matcher.match(line):
               match_count += 1
     print(match_count)

if __name__ == '__main__':
     main()
