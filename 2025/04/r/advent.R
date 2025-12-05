#!/usr/bin/env Rscript
#
# Advent of Code solution
# Usage: Rscript advent.R <part> <filename> [-v]
#

suppressPackageStartupMessages(library(optparse))

# Global verbose flag
verbose <- FALSE

# Read all lines from a file
read_lines <- function(filename) {
  lines <- readLines(filename, warn = FALSE)
  lines <- trimws(lines)
  lines[lines != ""]
}

# Read file as a character matrix (grid)
read_grid <- function(filename) {
  lines <- read_lines(filename)
  do.call(rbind, strsplit(lines, ""))
}

# Verbose print helper
vprint <- function(...) {
  if (verbose) {
    cat(..., "\n")
  }
}

# Shift helpers
shift_left  <- function(m) cbind(m[, -1], 0)
shift_right <- function(m) cbind(0, m[, -ncol(m)])
shift_up    <- function(m) rbind(m[-1, ], 0)
shift_down  <- function(m) rbind(0, m[-nrow(m), ])

# Diagonals are just compositions
shift_ul <- function(m) shift_up(shift_left(m))
shift_ur <- function(m) shift_up(shift_right(m))
shift_dl <- function(m) shift_down(shift_left(m))
shift_dr <- function(m) shift_down(shift_right(m))

part1 <- function(filename) {
  lines <- read_lines(filename)

  vprint("Read", length(lines), "lines from", filename)

  # Read the input into a grid, mapping '@' to 1 and '.' to 0
  grid <- read_grid(filename)
  grid_num <- matrix(0, nrow(grid), ncol(grid))
  grid_num[grid == "@"] <- 1

  # For every grid cell do the following: if 0, skip. If a number,
  # set it to the sum of adjacent cells.

  # We'll do this by creating 8 shifted versions of the grid and summing them, then
  #  adding that to the original grid so that a cell counts itself for adjacency purposes.
  grid_neighbor_count <-
    shift_left(grid_num) +
    shift_right(grid_num) +
    shift_up(grid_num) +
    shift_down(grid_num) +
    shift_ul(grid_num) +
    shift_ur(grid_num) +
    shift_dl(grid_num) +
    shift_dr(grid_num) +
    grid_num
  
  # Multiple by the original grid to zero out cells that were originally 0
  new_grid <- grid_num * grid_neighbor_count
  
  # Note: This approach means that we need to check for cells above 0 and
  #       below *5* (not 4) because a cell with 4 neighbors would have counted itself.

  # Optional: print the grids if verbose
  if (verbose) {
    # Print grid_neighbor_count
    cat("Neighbor counts:\n")
    for (i in 1:nrow(new_grid)) {
      cat(paste(new_grid[i, ], collapse = " "), "\n")
    }

    # Generate a new grid, where cells with value 0 become '.',
    #  cells >0 and <4 become 'x', and cells >=4 become '@'.
    new_grid_char <- matrix(".", nrow(new_grid), ncol(new_grid))
    new_grid_char[new_grid > 0 & new_grid < 5] <- "x"
    new_grid_char[new_grid >= 5] <- "@"
    cat("Generated grid:\n")
    for (i in 1:nrow(new_grid_char)) {
      cat(paste(new_grid_char[i, ], collapse = ""), "\n")
    }
  }

  # Count how many cells have 0 < value < 4, and store that as the result.
  result <- sum(new_grid < 5 & new_grid > 0)

  cat("Part 1:", result, "\n")
}

part2 <- function(filename) {
  lines <- read_lines(filename)

  vprint("Read", length(lines), "lines from", filename)

  # TODO: Implement solution
  result <- 0

  cat("Part 2:", result, "\n")
}

main <- function() {
  option_list <- list(
    make_option(c("-v", "--verbose"),
      action = "store_true", default = FALSE,
      help = "Enable verbose output"
    )
  )

  parser <- OptionParser(
    usage = "usage: %prog [options] <part> <filename>",
    option_list = option_list
  )

  args <- parse_args(parser, positional_arguments = 2)

  part <- args$args[1]
  filename <- args$args[2]
  verbose <<- args$options$verbose

  if (part == "1") {
    part1(filename)
  } else if (part == "2") {
    part2(filename)
  } else {
    stop(paste("Unknown part:", part, "- use 1 or 2"))
  }
}

main()
