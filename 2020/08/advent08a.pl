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

my $pc = 0,
my $ac = 0;

while ($pc < scalar @lines) {
     my ($reached, $op, $cnt) = ($lines[$pc] =~ /(!?)(nop|acc|jmp) \+?(\-?\d+)/);
     if ($reached eq '!') {
          print "Loop detected with ac=$ac\n";
          last;
     }

     $lines[$pc] = "!" . $lines[$pc];

     if ($op eq "acc") {
          $ac += $cnt;
     }

     $pc+= ($op eq "jmp")? $cnt : 1;
}

close($file_handle);
