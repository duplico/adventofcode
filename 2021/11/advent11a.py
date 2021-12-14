import fileinput
import numpy as np

def main():
    total_flashes = 0
    # Read the octopus grid into a 2D numpy array:
    octo_grid = np.asarray(list(list(map(int, input.strip())) for input in fileinput.input()))

    for round in range(100):
        # This holds the boolean values of whether an octopus flashes in this round
        #  or not, set at the same time as it increments its neighbors:
        octo_flashes = np.full_like(octo_grid, False)

        # Increment all octo values.
        octo_grid += 1

        while True:
            # Values over 10 that haven't flashed yet:
            this_octo_flashes = np.logical_and(octo_grid >= 10, np.logical_not(octo_flashes))

            # The round is over when there are no more NEW octopus flashes
            if not this_octo_flashes.any():
                # Zero out every octopus that flashed.
                octo_grid = np.where(octo_grid >= 10, 0, octo_grid)
                break

            # Otherwise, some new octopus flashes happened. Let's increment all their neighbors.
            # NOTE: This could probably be done with a filter or something that I can't think of
            #       how to use.
            # For every row,col that needs to flash:
            for row, col in np.transpose(this_octo_flashes.nonzero()):
                for row_d in [row-1, row, row+1]:
                    for col_d in [col-1, col, col+1]:
                        try:
                            if row_d == row and col_d == col:
                                continue
                            if row_d <0 or col_d<0:
                                raise IndexError()
                            octo_grid[row_d,col_d] += 1
                        except IndexError:
                            continue
            
            # Everything that flashed this sub-round is logical ORed into the
            # octo_flashes array so it won't flash again even if incremented.
            octo_flashes = np.logical_or(octo_flashes, this_octo_flashes)

        total_flashes += np.count_nonzero(octo_flashes)
        
    print(total_flashes)

if __name__ == '__main__':
    main()
