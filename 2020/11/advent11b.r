library(caTools)

# Given a vector of seats, smear across the vector.
visible <- function(x) {
     # It assumes the values in x are 1 for occupied, 0 for empty seat,
     #  and -1 for floor.
     # Smearing stops when it arrives at an unoccupied seat.
     
     # We start at the edge of the boat, so nothing is visible in this
     # direction:
     smearing <- 0

     # For every seat in the vector:
     for (i in 1:length(x)) {
          if (x[i] == 0) {
               # Empty seat, which blocks our view; so will not smear
               #  anything past it.
               next_smearing <- 0
          } else if (x[i] == 1) {
               # Occupied seat, smear from it (regardless of current
               #  smearing status)
             next_smearing <- 1
          } else {
               # Else it's the floor, which doesn't change our smearing status.
               next_smearing <- smearing
          }

          # Smear a 0 or 1 to the current element.
          x[i] <- smearing

          smearing <- next_smearing
     }
     return(x)
} # visible


# These functions do a column-wise shift up or down on a matrix.
#  Every column is shifted by (col_num-1) rows. So,
#  The first column is not shifted. The second column is shifted
#  up or down by 1 row, the third by 2, and so on. This has the
#  effect of transforming a matrix that represents rectangular
#  relationships between seats into one that represents diagonal
#  relationships.
shift_diag_down <- function(mat) {
     nr <- nrow(mat)
     nc <- ncol(mat)

     for( i in 2:nc ){
          mat[,i] <- c(rep(0,i-1), head(mat[,i], nr+1-i))
     }

     return(mat)
}
shift_diag_up <- function(mat) {
     nr <- nrow(mat)
     nc <- ncol(mat)

     for( i in 2:nc ){
          mat[,i] <- c(tail(mat[,i], nr+1-i), rep(0,i-1))
     }

     return(mat)
}

# These helper functions accomplish what I'm calling "smearing," with a series
#  of gross-looking matrix operations, which boil down to applying the
#  `visible` function row-wise or column-wise. For everything but top-down
#  column-wise, this requires us to apply and then reverse a series of
#  reversing and transposition actions.
smear_right <- function(mat) {
     t(apply(mat, 1, visible)) # Smear any 1s we find all the way RIGHT
}
smear_left <- function(mat) {
     t(apply(apply(apply(mat, 1, rev), 2, visible), 2, rev)) # Smear LEFT
}
smear_up <- function(mat) {
     apply(apply(apply(mat, 2, rev), 2, visible), 2, rev)
}
smear_down <- function(mat) {
     apply(mat, 2, visible) # Smear any 1s we find all the way DOWN
}

###############
# Here begins the program logic,
#  which really should be in a procedure. Oh well.

lines <- scan("input.txt", character(), quote="")
chars <- strsplit(lines, "")
seats <- do.call(rbind, chars)

# The boat's dimensions:
r <- nrow(seats)
c <- ncol(seats)

# Now we're playing a WEIRD game of Life, where adjacency is defined VERY
#  differently. The neighbor count is based on whether there are ANY 1s
#  visible in each cardinal direction, and in diagonal directions,
#  except that our "visibility" may be blocked by an empty seat.
# Then, we use these rules:
#  If its neighbor count is 0, it becomes full (1)
#  If its neighbor count is 5+, it empties     (0)
#  Otherwise, no change.
# Floors are always empty and never change.

# Let's make a MASK out of the floors, in which 0 is not a floor, and
#  1 is a floor.
floor <- matrix(0, r, c)
floor[seats=="."] <- 1

curr_layout <- matrix(0, r, c) # Boats start empty.
prev_layout <- matrix(2, r, c) # Create an invalid "previous" layout

# Now we've got a floor mask (floor), and a matrix of where people are
#  sitting (curr_layout), and a matrix of where people were previously
#  sitting (prev_layout), which is invalid for the first run so we'll always
#  loop at least once.

gif_storage = array(0, c(r,c,100))
steps <- 0

# So, we're off to see the wizard.
while (!all(curr_layout == prev_layout)) {

     steps <- steps+1
     # Ok, we're going to do something similar to part 1 here. For each
     #  cardinal direction, we need to produce a matrix where a 1 means
     #  there's an occupied cell in that direction. I'm going to call this
     #  "smearing" because we're looking for 1s and then smearing them in
     #  some direction until we find an empty seat to mark with it.

     # Annotate the floor with a -1. Our smearing visibility function depends
     #  upon the following key:
     #  Empty seat = 0
     #  Full seat = 1
     #  Floor = -1
     curr_layout[floor == 1] <- -1

     # Cardinal directions.
     cnt_from_u <- smear_down(curr_layout)
     cnt_from_l <- smear_right(curr_layout)
     cnt_from_r <- smear_left(curr_layout)
     cnt_from_d <- smear_up(curr_layout)

     # Now, it's time for the diagonal ones. These are a little complicated.
     #  We solve these by transforming the matrix: we double its vertical size,
     #  then shift each column up or down according to its index. In this
     #  transformed matrix, a left/right or up/down relationship between
     #  entries corresponds to a DIAGONAL relationship in the source matrix.
     # After the transformation, we apply a horizontal smearing function to
     #  the matrix.
     # Then, we reverse the diagonal transformation and trim off the excess
     #  rows.
     #
     # For example, take the following grid, and assume we wish to smear
     #  diagonally down and to the right to achieve the Goal grid:
     #
     # Original     Goal
     # 111          000
     # 000          011
     # 001          001
     #
     # To achieve this, we expand it vertically and shift each column but
     #  the first up according to its position; then we smear to the right,
     #  then reverse the shift:
     #
     # Shifted      Smeared        Unshifted and truncated
     # 001          000            000
     # 010          001            011
     # 101          011            001
     # 000          000
     # 000          000

     cnt_from_lu <- rbind(matrix(0,r,c), curr_layout)
     cnt_from_lu <- shift_diag_down(smear_right(shift_diag_up(cnt_from_lu)))[-1:-r,]

     cnt_from_ru <- rbind(curr_layout, matrix(0,r,c))
     cnt_from_ru <- shift_diag_up(smear_left(shift_diag_down(cnt_from_ru)))[1:r,]

     cnt_from_rd <- rbind(matrix(0,r,c), curr_layout)
     cnt_from_rd <- shift_diag_down(smear_left(shift_diag_up(cnt_from_rd)))[-1:-r,]

     cnt_from_ld <- rbind(curr_layout, matrix(0,r,c))
     cnt_from_ld <- shift_diag_up(smear_right(shift_diag_down(cnt_from_ld)))[1:r,]

     # Sum these up.
     neighbor_cnt <- cnt_from_l + cnt_from_r + cnt_from_u + cnt_from_d +
                    cnt_from_lu + cnt_from_ld + cnt_from_ru + cnt_from_rd

     gif_storage[,,steps] <- neighbor_cnt
     gif_storage[,,steps][floor == 1] <- 0

     # Use our current layout as the starting point for the next one:
     next_layout <- curr_layout

     # Logical subscripting makes this next part easy!
     #  If a seat's neighbor count is 0, it becomes full (1)
     next_layout[neighbor_cnt == 0] <- 1
     #  If its neighbor count is 5+, it empties     (0)
     next_layout[neighbor_cnt >= 5] <- 0
     #  Otherwise, no change.

     # However! Nobody is allowed to sit on the floor. Mask it off.
     next_layout[floor == 1] <- 0
     curr_layout[floor == 1] <- 0 # Clean up our -1s

     prev_layout <- curr_layout
     curr_layout <- next_layout
}

gif_storage <- gif_storage[,,1:steps]/max(gif_storage)
write.gif(gif_storage, "part2.gif", col="jet", delay=10)

# How many butts are in seats once this thing stabilizes?
print(sum(curr_layout==1))
