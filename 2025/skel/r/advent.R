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
  lines <- lines[lines != ""]
  vprint("Read", length(lines), "lines from", filename)
  lines
}

# Read file as a character matrix (grid)
read_grid <- function(filename) {
  lines <- read_lines(filename)
  grid <- do.call(rbind, strsplit(lines, ""))
  vprint("Grid dimensions:", nrow(grid), "x", ncol(grid))
  grid
}

# Verbose print helper
vprint <- function(...) {
  if (verbose) {
    cat(..., "\n")
  }
}

part1 <- function(filename) {
  lines <- read_lines(filename)

  # TODO: Implement solution
  result <- 0

  cat("Part 1:", result, "\n")
}

part2 <- function(filename) {
  lines <- read_lines(filename)

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
