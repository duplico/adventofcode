use strict;
use warnings;

my $file = $ARGV[0];
my @lines;

if (not defined $file) {
     $file = "sample_input.txt";
}

# Load the file into RAM.
open(my $file_handle, '<', $file) or die "Input file open fialed.";
chomp(@lines = <$file_handle>);

my $attempt = 0;

for my $i (0..scalar @lines-1) {
     if ($lines[$i] =~ /nop|jmp/) {
          $lines[$i] =~ s/nop/tmp/;
          $lines[$i] =~ s/jmp/nop/;
          $lines[$i] =~ s/tmp/jmp/;

          my $pc = 0,
          my $ac = 0;
          while ($pc < scalar @lines) {
               my ($reached, $op, $cnt) = ($lines[$pc] =~ /(\d*)(nop|acc|jmp) ([\+\-]\d+)/);
               if ($reached eq $attempt) {
                    print "Loop detected at pc=$pc with ac=$ac\n";
                    $attempt++;
                    last;
               }

               $lines[$pc] = "$attempt$op $cnt";

               if ($op eq "acc") {
                    $ac += $cnt;
               }

               $pc+= ($op eq "jmp")? $cnt : 1;
          }

          if ($pc == scalar @lines) {
               print "No loop detected, pc=$pc ac=$ac\n";
               last
          }
          
          $lines[$i] =~ s/nop/tmp/;
          $lines[$i] =~ s/jmp/nop/;
          $lines[$i] =~ s/tmp/jmp/;
     }
}

close($file_handle);
