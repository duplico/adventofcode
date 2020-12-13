# this is an absolute mess.

visible <- function(x) {
     # This function is used for smearing purposes.
     # It assumes the values in x are 1 for occupied, 0 for empty seat,
     #  and -1 for floor.
     # Smearing stops when it arrives at an unoccupied seat.
     
     smearing <- 0

     for (i in 1:length(x)) {
          next_smearing <- smearing
          if (x[i] == 0) {
               # Empty seat, stop smearing.
               next_smearing <- 0
          } else if (x[i] == 1) {
               # Occupied occupied seat, smear from it.
             next_smearing <- 1
          } # Else it's the floor, which doesn't change our smearing status.

          # Smear a 0 or 1 to the current element.
          x[i] <- smearing
          smearing <- next_smearing
     }
     return(x)
} # visible

shift_diag_right <- function(mat) {
     nr <- nrow(mat)
     nc <- ncol(mat)

     for( i in 2:nr ){
          mat[i,] <- c(rep(0,i-1), head(mat[i,], nc+1-i))
     }

     return(mat)
}

shift_diag_left <- function(mat) {
     nr <- nrow(mat)
     nc <- ncol(mat)

     for( i in 2:nr ){
          mat[i,] <- c(tail(mat[i,], nc+1-i), rep(0,i-1))
     }

     return(mat)
}

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

smear_right <- function(mat) {

     mat <- t(apply(mat, 1, visible)) # Smear any 1s we find all the way RIGHT
     # mat <- cbind(rep(0, r), mat[,-ncol(mat)]) # Shift values RIGHT into a new matrix

     return(mat)
}

smear_left <- function(mat) {
     mat <- t(apply(apply(apply(mat, 1, rev), 2, visible), 2, rev)) # Smear LEFT
     # mat <- cbind(mat[,-1], rep(0, nrow(mat))) # Shift values LEFT into a new matrix

     return(mat)
}

smear_up <- function(mat) {
     mat <- apply(apply(apply(mat, 2, rev), 2, visible), 2, rev) # Smear 1s all the way UP
     # mat <- rbind(mat[-1,], rep(0, ncol(mat))) # Shift values UP into a new matrix
     return(mat)
}

smear_down <- function(mat) {
     mat <- apply(mat, 2, visible) # Smear any 1s we find all the way DOWN
     # mat <- rbind(rep(0, ncol(mat)), mat[-nrow(mat),]) # Shift values DOWN into a new matrix
     return(mat)
}

lines <- scan("sample_input.txt", character(), quote="")
chars <- strsplit(lines, "")
seats <- do.call(rbind, chars)

# The boat's dimensions:
r <- nrow(seats)
c <- ncol(seats)

# Now we're playing a WEIRD game of Life, where adjacency is defined VERY
#  differently. The neighbor count is based on whether there are ANY 1s
#  at all in each cardinal direction, and in diagonal directions.
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

# So, we're off to see the wizard.
while (!all(curr_layout == prev_layout)) {

     # Ok, we're going to do something similar to part 1 here. For each
     #  cardinal direction, we need to produce a matrix where a 1 means
     #  there's an occupied cell in that direction. I'm going to call this
     #  "smearing" because we're basically looking for the first 1 and
     #  then putting that 1 everywhere after it.

     # First, we need to accomplish the smearing task. This is done with a series
     #  of gross-looking matrix operations, which boil down to applying the
     #  `visible` function row-wise or column-wise. For everything but top-down
     #  column-wise, this requires us to apply and then reverse a series of
     #  reversing and transposition actions.

     # We also need to keep our SHIFTING behavior, because this approach
     #  incorrectly counts each seat as visible to itself.

     # Annotate the floor with a -1 so smearing will work.
     curr_layout[floor == 1] <- -1
     
     print("===========")
     print("Current:")
     print(curr_layout)

     cnt_from_u <- smear_down(curr_layout)
     cnt_from_l <- smear_right(curr_layout)
     cnt_from_r <- smear_left(curr_layout)
     cnt_from_d <- smear_up(curr_layout)
     
     print("down")
     print(cnt_from_u)
     print("right")
     print(cnt_from_l)
     print("left")
     print(cnt_from_r)
     print("up")
     print(cnt_from_d)

     # Now, it's time for the diagonal ones. These are a little complicated,
     #  but work by shifting, smearing, and unshifting. For example, to smear
     #  diagonally down and to the right, we must shift every column up by
     #  its column number (minus one), smear to the right, and then shift
     #  back down. This will turn straight lines into the diagonals
     #  that we want.

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

     print("Neighbors:")
     print(neighbor_cnt)

     prev_layout <- curr_layout
     curr_layout <- next_layout
}

# How many butts are in seats once this thing stabilizes?
print(sum(curr_layout==1))
