---
applyTo: "**/*.R,**/*.r"
---

# R Instructions for Advent of Code

## R Style for AoC

- Use vectorized operations over loops whenever possible
- Matrices are column-major (first index is row, second is column)
- Use `<-` for assignment (not `=` in function bodies)
- Use descriptive variable names in snake_case

## Useful Base R Functions

### Vector/Matrix Operations

```r
# Create sequences
1:10
seq(1, 10, by = 2)
rep(0, 10)

# Matrix creation
matrix(0, nrow = 5, ncol = 5)
do.call(rbind, list_of_vectors)

# Matrix indexing
grid[row, col]
grid[row, ]        # entire row
grid[, col]        # entire column
grid[grid == "X"]  # logical indexing

# Apply functions
apply(grid, 1, sum)  # apply to each row
apply(grid, 2, sum)  # apply to each column
sapply(list, func)   # apply and simplify
lapply(list, func)   # apply, return list
```

### String Operations

```r
# Split string into characters
strsplit("hello", "")[[1]]

# Pattern matching
grep("pattern", vec)           # indices of matches
grepl("pattern", vec)          # logical vector
gsub("old", "new", string)     # replace all
regmatches(s, gregexpr("\\d+", s))  # extract all matches

# String manipulation
paste(vec, collapse = ",")
substr(s, start, stop)
nchar(s)
trimws(s)
```

### Set Operations

```r
union(a, b)
intersect(a, b)
setdiff(a, b)
a %in% b  # element-wise membership
```

## Input Parsing Patterns

```r
# Read all lines
lines <- readLines(filename, warn = FALSE)

# Parse integers from each line
nums <- as.integer(lines)

# Parse space-separated integers
nums <- as.integer(strsplit(line, " ")[[1]])

# Extract all numbers from a line (including negatives)
nums <- as.integer(regmatches(line, gregexpr("-?\\d+", line))[[1]])

# Read as character grid
grid <- do.call(rbind, strsplit(lines, ""))

# Read paragraph-separated groups
content <- paste(readLines(filename), collapse = "\n")
groups <- strsplit(content, "\n\n")[[1]]
```

## Cellular Automata Patterns

```r
# Shift matrix for neighbor counting
shift_left  <- cbind(grid[, -1], 0)
shift_right <- cbind(0, grid[, -ncol(grid)])
shift_up    <- rbind(grid[-1, ], 0)
shift_down  <- rbind(0, grid[-nrow(grid), ])

# Count neighbors (for binary grid)
neighbors <- shift_left + shift_right + shift_up + shift_down

# Conway-style rules with logical indexing
next_grid <- grid
next_grid[neighbors == 3] <- 1
next_grid[neighbors < 2 | neighbors > 3] <- 0

# Pad a grid with zeros
pad_grid <- function(g, n = 1) {
  rows <- nrow(g)
  cols <- ncol(g)
  padded <- matrix(0, rows + 2*n, cols + 2*n)
  padded[(n+1):(n+rows), (n+1):(n+cols)] <- g
  padded
}
```

## Common Patterns

```r
# Memoization with environment
memo <- new.env()
solve <- function(state) {
  key <- paste(state, collapse = ",")
  if (exists(key, envir = memo)) return(get(key, envir = memo))
  # ... compute result ...
  assign(key, result, envir = memo)
  result
}

# BFS with queue
bfs <- function(start) {
  queue <- list(start)
  visited <- new.env()
  while (length(queue) > 0) {
    current <- queue[[1]]
    queue <- queue[-1]
    key <- paste(current, collapse = ",")
    if (exists(key, envir = visited)) next
    assign(key, TRUE, envir = visited)
    # ... process and add neighbors to queue ...
  }
}

# Iterate until stable
prev <- NULL
curr <- initial
while (!identical(prev, curr)) {
  prev <- curr
  curr <- step(curr)
}
```

## Performance Tips

- Preallocate vectors/matrices instead of growing them
- Use `vapply` over `sapply` when you know the output type
- Consider `data.table` for very large datasets
- Use `Rprof()` to profile slow code
- Matrix operations are much faster than loops
