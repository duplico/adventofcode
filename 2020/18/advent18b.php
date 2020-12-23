<?php

function do_math($a1, $op, $a2) {
     if ($op == '+') {
          return $a1 + $a2;
     } else if ($op === "*") {
          return $a1 * $a2;
     } else {
          echo "ERROR!!!! INVALID OPERATOR!\n";
          exit(1);
     }
}

function tokenize_str($line) {     
     $pattern = "/\+|\*|\d+|\(|\)/";
     preg_match_all($pattern, $line, $toks);
     return $toks[0];
}

function eval_adventmath($toks) {
     $first_paren = array_search("(", $toks);
     $first_add = array_search("+", $toks);
     if (count($toks) == 1) {
          // we have a single value!
          return intval($toks[0]);
     } else if ($first_paren === false && $first_add === false) {
          // Base-ish case: there are no parens, and no adds, 
          // so let's just do some math.
          $pc = 0;
          $val = intval($toks[0]);
          while ($pc+2 < count($toks)) {
               $val = do_math($val, $toks[$pc+1], intval($toks[$pc+2]));
               $pc += 2;
          }
          return $val;
     } else if ($first_paren === false) {
          // There are no parens here, but there is some addition.
          // Find the first addition, resolve it, and recurse.
          // The first addition is $toks[$first_add-1] + $toks[$first_add+1].
          $new_val = do_math(intval($toks[$first_add-1]), "+", intval($toks[$first_add+1]));
          array_splice($toks, $first_add-1, 3, $new_val);
          return eval_adventmath($toks);
     } else {
          // There are parens.
          // Find the first open paren, and its matching close paren, and
          //  replace that in the string with the value of its contents:
          $nesting_level = 1;
          $paren_len = 1;
          while (true) {
               if ($toks[$first_paren + $paren_len] == '(') {
                    $nesting_level += 1;
               } else if ($toks[$first_paren + $paren_len] == ')') {
                    $nesting_level -= 1;
                    if ($nesting_level == 0) {
                         // then we're going to extract and replace the
                         //  parenthetical at indices $first_paren..$last_paren
                         array_splice($toks, $first_paren, $paren_len+1, eval_adventmath(array_slice($toks, $first_paren+1, $paren_len-1)));
                         return eval_adventmath($toks);
                    }
               }
               $paren_len++;
          }
     }
}

$file = fopen("input.txt", "r");
$line = "";
$sum = 0;
while (!feof($file)) {
     $sum += eval_adventmath(tokenize_str(fgets($file)));
}
echo $sum . "\n";
