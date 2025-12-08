#!/usr/bin/env Rscript
#
# Advent of Code solution
# Usage: Rscript advent.R <part> <filename> [-v] [--gif]
#

suppressPackageStartupMessages(library(optparse))

# Global flags
verbose <- FALSE
make_gif <- FALSE

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
  grid <- read_grid(filename)
  splits <- 0

  # Set up GIF generation if requested
  if (make_gif) {
    tmp_dir <- tempdir()
    frame_files <- c()
    frame_num <- 0

    # Helper to render grid as a PNG frame
    render_frame <- function(g, title) {
      frame_num <<- frame_num + 1
      tmp_file <- file.path(tmp_dir, sprintf("frame_%04d.png", frame_num))
      frame_files <<- c(frame_files, tmp_file)

      # Scale up for visibility
      scale <- 10
      width <- ncol(g) * scale
      height <- nrow(g) * scale

      png(tmp_file, width = width, height = height + 30)
      par(mar = c(0, 0, 1.5, 0))

      # Convert grid to numeric: S=3, ^=2, |=1, .=0
      mat <- matrix(0, nrow(g), ncol(g))
      mat[g == "|"] <- 1
      mat[g == "^"] <- 2
      mat[g == "S"] <- 3

      # Colors: white for ., blue for S, red for ^, green for |
      cols <- c("white", "#33cc33", "#ff3333", "#3366ff")
      image(t(mat[rev(seq_len(nrow(mat))), ]),
        col = cols, zlim = c(0, 3),
        axes = FALSE, main = title
      )
      dev.off()
    }

    # Capture initial state
    render_frame(grid, "Initial Grid")
  }

  # Locate the "S" starting point on the first row of the grid
  start_col <- which(grid[1, ] == "S")
  grid[2, start_col] <- "|" # Emit a vertical line from the start point

  vprint("Starting point at row 1, column", start_col)

  if (make_gif) {
    render_frame(grid, "Step 1: Start")
  }

  # Now, starting at row 3 and until we reach the end of the grid,
  #  find all "|" characters in row-1, for each col i where one is found:
  #   * If there is a "." in the current row, emit a pipe line at column i
  #   * If there is a "^" instead, emit vertical lines at column i-1 and i+1
  #     and add 1 to our running total of splits.
  for (r in 3:nrow(grid)) {
    # Find all columns in the previous row that have "|"
    pipe_cols <- which(grid[r - 1, ] == "|")

    for (i in pipe_cols) {
      if (grid[r, i] == ".") {
        # Emit horizontal line
        grid[r, i] <- "|"
      } else if (grid[r, i] == "^") {
        # Emit vertical lines at adjacent columns
        if (i > 1) grid[r, i - 1] <- "|"
        if (i < ncol(grid)) grid[r, i + 1] <- "|"
        splits <- splits + 1
      }
    }

    if (make_gif) {
      render_frame(grid, paste("Row", r, "- Splits:", splits))
    }
  }

  # Write out the gif using gifski
  if (make_gif) {
    suppressPackageStartupMessages(library(gifski))
    cat("Combining", length(frame_files), "frames into GIF...\n")
    gifski(frame_files, "part1.gif", delay = 0.2, progress = TRUE)
    cat("Wrote animation to part1.gif\n")
    # Clean up temp files
    unlink(frame_files)
  }

  cat("Part 1:", splits, "\n")
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
    ),
    make_option(c("-g", "--gif"),
      action = "store_true", default = FALSE,
      help = "Generate animated GIF"
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
  make_gif <<- args$options$gif

  if (part == "1") {
    part1(filename)
  } else if (part == "2") {
    part2(filename)
  } else {
    stop(paste("Unknown part:", part, "- use 1 or 2"))
  }
}

main()
