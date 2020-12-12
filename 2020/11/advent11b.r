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

     # Then, for the diagonal version we will take those and SHIFT them,
     #  row-wise, to turn the straight lines into diagonal ones.
     #  That is, for instance, row 1 isn't shifted at all; row 2 is shifted
     #  by 1 element, row 3 by 2, etc.

     # First, we need to accomplish the smearing task. This is done with a series
     #  of gross-looking matrix operations, which boil down to applying the
     #  `cummax` function row-wise or column-wise. For everything but top-down
     #  column-wise, this requires us to apply and then reverse a series of
     #  reversing and transposition actions.

     # We also need to keep our SHIFTING behavior, because this approach
     #  incorrectly counts each seat as visible to itself.

     cnt_from_u <- apply(curr_layout, 2, cummax) # Smear any 1s we find all the way DOWN
     cnt_from_u <- rbind(rep(0, c), cnt_from_u[-r,]) # Shift values DOWN into a new matrix

     cnt_from_l <- t(apply(curr_layout, 1, cummax)) # Smear any 1s we find all the way RIGHT
     cnt_from_l <- cbind(rep(0, r), cnt_from_l[,-c]) # Shift values RIGHT into a new matrix

     cnt_from_r <- t(apply(apply(apply(curr_layout, 1, rev), 2, cummax), 2, rev)) # Smear LEFT
     cnt_from_r <- cbind(cnt_from_r[,-1], rep(0, r)) # Shift values LEFT into a new matrix

     cnt_from_d <- apply(apply(apply(curr_layout, 2, rev), 2, cummax), 2, rev) # Smear 1s all the way UP
     cnt_from_d <- rbind(cnt_from_d[-1,], rep(0, c)) # Shift values UP into a new matrix

     # Here's an example of how to do that shifting. Note that it creates a warning.
     # Shift UP:
     # a2 <- matrix(cnt_from_r, ncol = c, nrow = r + 1)[1:r, ]
     # a2[col(a2) + row(a2) > r + 1] <- 0

     # Sum these up.
     neighbor_cnt <- cnt_from_l + cnt_from_r + cnt_from_u + cnt_from_d +
                    cnt_from_lu + cnt_from_ld + cnt_from_ru + cnt_from_rd

     # Use our current layout as the starting point for the next one:
     next_layout <- curr_layout

     # Logical subscripting makes this next part easy!
     #  If a seat's neighbor count is 0, it becomes full (1)
     next_layout[neighbor_cnt == 0] <- 1
     #  If its neighbor count is 4+, it empties     (0)
     next_layout[neighbor_cnt >= 4] <- 0
     #  Otherwise, no change.

     # However! Nobody is allowed to sit on the floor. Mask it off.
     next_layout[floor == 1] <- 0

     prev_layout <- curr_layout
     curr_layout <- next_layout
}

# How many butts are in seats once this thing stabilizes?
print(sum(curr_layout==1))
