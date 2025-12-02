#!/usr/bin/env tclsh
#
# Advent of Code solution
# Usage: tclsh advent.tcl <part> <filename> [-v]
#

package require Tcl 8.6

# Global verbose flag
set verbose 0

# Read all lines from a file
proc read_lines {filename} {
    set f [open $filename r]
    set content [read $f]
    close $f
    # Split into lines and filter empty
    set lines [split [string trim $content] \n]
    return $lines
}

proc part1 {filename} {
    global verbose
    set lines [read_lines $filename]

    if {$verbose} {
        puts "Read [llength $lines] lines from $filename"
    }

    # TODO: Implement solution
    set result 0

    puts "Part 1: $result"
}

proc part2 {filename} {
    global verbose
    set lines [read_lines $filename]

    if {$verbose} {
        puts "Read [llength $lines] lines from $filename"
    }

    # TODO: Implement solution
    set result 0

    puts "Part 2: $result"
}

proc main {argv} {
    global verbose

    if {[llength $argv] < 2} {
        puts stderr "Usage: tclsh advent.tcl <part> <filename> \[-v\]"
        exit 1
    }

    set part [lindex $argv 0]
    set filename [lindex $argv 1]

    # Check for verbose flag
    if {[lsearch $argv "-v"] >= 0} {
        set verbose 1
    }

    switch $part {
        1 { part1 $filename }
        2 { part2 $filename }
        default {
            puts stderr "Unknown part: $part. Use 1 or 2."
            exit 1
        }
    }
}

main $argv
