---
applyTo: "**/*.tcl"
---

# Tcl Instructions for Advent of Code

## Tcl Style for AoC

- "Everything is a string" - embrace Tcl's simplicity
- Use procedures (`proc`) for reusable logic
- Leverage `lmap`, `lsort`, `lsearch` for list operations
- Use `dict` for key-value data structures
- Regular expressions with `regexp` are powerful

## Tcl 8.7+ Features

- `lmap` - transform lists (like map in other languages)
- `string cat` - concatenation
- `try`/`finally` for error handling
- `coroutine` for generators/iterators
- `oo::class` for object-oriented patterns

## Input Parsing Patterns

```tcl
# Read all lines
set f [open $filename r]
set lines [split [read $f] \n]
close $f

# Filter empty lines
set lines [lmap line $lines {if {$line ne ""} {set line} else continue}]

# Parse integers from a line
set nums [regexp -all -inline {\d+} $line]

# Read paragraph-separated groups
set groups [split [read $f] \n\n]

# Grid as list of lists
set grid [lmap line $lines {split $line ""}]
```

## Useful Patterns

```tcl
# List operations
lindex $list $i        ;# access element
llength $list          ;# list length
lrange $list $start $end
lsort -integer $list   ;# sort numerically
lsearch $list $val     ;# find index
lmap x $list {expr {$x * 2}}  ;# transform

# Dict operations
dict set d key value
dict get $d key
dict exists $d key
dict for {k v} $d { ... }

# String operations
string index $s $i
string range $s $start $end
string map {old new} $s
```

## Math and Expressions

```tcl
# Use expr for math
set result [expr {$a + $b}]
set result [expr {$x > $y ? $x : $y}]

# Tcllib math
package require math::combinatorics
```

## Running Solutions

```bash
tclsh advent.tcl input.txt
# Or with arguments
tclsh advent.tcl 1 input.txt   ;# part 1
tclsh advent.tcl 2 input.txt   ;# part 2
```

## Suggested Packages (Tcllib)

- **struct::set**: Set operations
- **struct::graph**: Graph data structures
- **math::combinatorics**: Permutations, combinations
- **cmdline**: Command-line argument parsing
