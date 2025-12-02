# Advent of Code - Tcl Solution

## Running

```bash
# Part 1
tclsh advent.tcl 1 ../input.txt
tclsh advent.tcl 1 ../input.txt -v    # verbose

# Part 2
tclsh advent.tcl 2 ../input.txt

# With sample input
tclsh advent.tcl 1 ../sample_input.txt
```

## Interactive REPL

```bash
tclsh
% source advent.tcl
% part1 "../sample_input.txt"
```

## Tcllib Packages

If you need additional packages from Tcllib:

```bash
# On Ubuntu/Debian
sudo apt install tcllib

# Then in your script
package require struct::set
package require math::combinatorics
```
