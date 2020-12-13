proc open_file {input_file} {
     set fp [open $input_file r]
     set file [read $fp]
     close $fp
     return [split $file "\n"]
}

proc advent12a {input_file} {
     set instructions [open_file $input_file]

     # We will describe our starting location as (0,0).
     set x 0; # East is positive.
     set y 0; # North is positive.

     # Our boat or whatever starts facing East. We'll call that 0.
     # And we'll measure the direction we're pointing as clockwise degrees,
     #  where:
     #  0  -> East
     #  90 -> South
     # 180 -> West
     # 270 -> North
     #  etc.
     set heading 0

     foreach instruction $instructions {
          set op [string range $instruction 0 0]
          set num [string range $instruction 1 end]

          if { $instruction == "" } {
               continue
          }

          switch $op {
               N { incr y $num }
               S { incr y -$num }
               E { incr x $num }
               W { incr x -$num }
               L { set heading [expr ($heading + 360 - $num) % 360] }
               R { set heading [expr ($heading + $num) % 360] }
               F {
                    switch $heading {
                         0    { incr x $num }
                         90   { incr y -$num }
                         180  { incr x -$num }
                         270  { incr y $num }
                    }
               }
          }
     }
     
     set manhattan_distance [expr abs($x) + abs($y)]

     puts "Manhattan distance from start: $manhattan_distance"
}

if { $argc == 1 } {
     set input_file [lindex $argv 0]
} elseif { $argc == 0 } {
     set input_file sample_input.txt
} else {
     puts {Argument error. Expected: advent12a.tcl [input.txt]}
     exit 1
}

advent12a $input_file
