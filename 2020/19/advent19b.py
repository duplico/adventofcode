import re

rules = dict()

# I am... not proud of this.
def rule_regex(rule, depth = 15):
     if re.match('"[ab]"', rule):
          # Base case.
          return rule[1]
     else:
          # We need to split it and process sub-rules.
          or_rules = [subrule.strip() for subrule in rule.split("|")]
          or_rule_texts = []
          for or_rule in or_rules:
               rule_elements = []
               for rule_element in or_rule.split():
                    if rule == rules[rule_element] and depth > 0:
                         rule_elements.append(rule_regex(rules[rule_element], depth-1))
                    elif rule != rules[rule_element]:
                         rule_elements.append(rule_regex(rules[rule_element]))
               or_rule_texts.append("(" + "".join(rule_elements) + ")")
          return "(" + "|".join(or_rule_texts) + ")"

def main():
     textlines = []

     reading_rules = True

     for line in open("input2.txt"):
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
