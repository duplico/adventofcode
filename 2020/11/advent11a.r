lines <- scan("input.txt", character(), quote="")
chars <- strsplit(lines, "")
seats <- do.call(rbind, chars)

# The boat's dimensions:
r <- nrow(seats)
c <- ncol(seats)

# So, this is basically like Conway's Game of Life, with some extra twists.
# There's floors and seats. Seats follow modified Life rules:
#  If its neighbor count is 0, it becomes full (1)
#  If its neighbor count is 4+, it empties     (0)
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

     # Ok, this next part is really fiddly. We're going to make 8 new matrices
     #  by shifting the values in curr_layout around: in each cardinal direction,
     #  and then also in every diagonal direction. Because curr_layout contains
     #  only 0s and 1s, summing these resulting matrices together will yield a
     #  matrix where each value is the number of NEIGHBORS of that seat position.

     cnt_from_l <- cbind(rep(0, r), curr_layout[,-c]) # Shift values RIGHT into a new matrix
     cnt_from_r <- cbind(curr_layout[,-1], rep(0, r)) # Shift values LEFT into a new matrix
     cnt_from_u <- rbind(rep(0, c), curr_layout[-r,]) # Shift values DOWN into a new matrix
     cnt_from_d <- rbind(curr_layout[-1,], rep(0, c)) # Shift values UP into a new matrix

     cnt_from_lu <- rbind(rep(0, c), cbind(rep(0, r-1), curr_layout[-r,-c])) # RIGHT+DOWN
     cnt_from_ld <- rbind(cbind(rep(0, r-1), curr_layout[-1,-c]), rep(0, c)) # RIGHT+UP
     cnt_from_ru <- rbind(rep(0, c), cbind(curr_layout[-r,-1], rep(0, r-1)))  # LEFT+DOWN
     cnt_from_rd <- rbind(cbind(curr_layout[-1,-1], rep(0, r-1)), rep(0, c)) # LEFT+UP

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
