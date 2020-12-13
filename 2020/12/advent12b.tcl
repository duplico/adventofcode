proc open_file {input_file} {
     set fp [open $input_file r]
     set file [read $fp]
     close $fp
     return [split $file "\n"]
}

proc advent12b {input_file} {
     set instructions [open_file $input_file]

     # We will describe our starting location as (0,0).
     set x 0; # East is positive.
     set y 0; # North is positive.

     #  Our boat or whatever starts with this waypoint:
     set wp_x 10
     set wp_y 1

     # If we need to rotate we'll use this to decide how.
     set heading 0

     foreach instruction $instructions {
          set op [string range $instruction 0 0]
          set num [string range $instruction 1 end]

          if { $instruction == "" } {
               continue
          }

          switch $op {
               N { incr wp_y $num }
               S { incr wp_y -$num }
               E { incr wp_x $num }
               W { incr wp_x -$num }
               L { set heading $num }
               R { set heading [expr 360-$num] }
               F {
                    # We go to the waypoint $num times.
                    incr x [expr $num * $wp_x]
                    incr y [expr $num * $wp_y]
               }
          }

          # Update the waypoint if we're rotating:
          while {$heading != 0} {
               set ny $wp_y
               set nx $wp_x
               # Rotate 90 deg to the left.
               set nx [expr -$wp_y]
               set ny $wp_x

               incr heading -90
               set wp_y $ny
               set wp_x $nx
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
     puts {Argument error. Expected: advent12b.tcl [input.txt]}
     exit 1
}

advent12b $input_file
