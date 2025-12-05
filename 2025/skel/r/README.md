# Advent of Code - R Solution

## Dependencies

This solution uses the `optparse` package for command-line argument parsing.

```r
install.packages("optparse")
```

## Running

```bash
# Part 1
Rscript advent.R 1 ../input.txt
Rscript advent.R 1 ../input.txt -v    # verbose

# Part 2
Rscript advent.R 2 ../input.txt

# With sample input
Rscript advent.R 1 ../sample_input.txt
```

## Interactive REPL

```r
# Start R in this directory
R

# Source the file (without running main)
# Comment out the main() call at the bottom first, or:
source("advent.R")

# Then call functions directly
lines <- read_lines("../sample_input.txt")
grid <- read_grid("../sample_input.txt")
```

## Useful Packages

For more complex puzzles, consider:

```r
# Matrix operations (sparse matrices)
install.packages("Matrix")

# Faster data manipulation
install.packages("data.table")

# String manipulation
install.packages("stringr")

# Functional programming
install.packages("purrr")
```
