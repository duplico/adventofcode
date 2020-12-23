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
     return explode(" ", $line);
}

function eval_adventmath($line) {
     // $line = str_replace(' ', '', $line);
     $first_paren = strpos($line, '(');
     $toks = tokenize_str($line);
     if ($first_paren === false) {
          // Base-ish case: there are no parens, so let's just do
          //  some math.
          $pc = 0;
          $val = intval($toks[0]);
          while ($pc+2 < count($toks)) {
               $val = do_math($val, $toks[$pc+1], intval($toks[$pc+2]));
               $pc += 2;
          }
          return $val;
     } else {
          // There are parens.
          // Find the first open paren, and its matching close paren, and
          //  replace that in the string with the value of its contents:
          $nesting_level = 1;
          $paren_len = 1;
          while (true) {
               if (substr($line, $first_paren + $paren_len, 1) == '(') {
                    $nesting_level += 1;
               } else if (substr($line, $first_paren + $paren_len, 1) == ')') {
                    $nesting_level -= 1;
                    if ($nesting_level == 0) {
                         // then we're going to extract and replace the
                         //  parenthetical at indices $first_paren..$last_paren
                         $line = substr($line, 0, $first_paren) . eval_adventmath(substr($line, $first_paren+1, $paren_len-1)) . substr($line, $first_paren+$paren_len+1);
                         return eval_adventmath($line);
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
     $sum += eval_adventmath(fgets($file));
}

echo $sum . "\n";
