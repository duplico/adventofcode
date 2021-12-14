import fileinput
import numpy as np
from numpy.core.numeric import count_nonzero

def main():
    folds: list[tuple[str, int]] = []
    dots: list[tuple[int, int]] = []
    max_x = 0
    max_y = 0

    for line in fileinput.input():
        line = line.strip()
        if not line:
            continue

        if line.startswith('fold'):
            direction = line[11]
            position = int(line.split('=')[1])
            folds.append((direction, position))
        else:
            x, y = map(int, line.split(','))
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            dots.append((x,y))
    
    # NB: This is going to render transposed from the figures on the website.
    dotfield = np.zeros((max_x+1, max_y+1), dtype=np.int0)

    for x,y in dots:
        dotfield[x,y] = 1

    # Do the first fold.
    fold_dir, fold_pos = folds[0]
    if fold_dir == 'x':
        # the part we'll be folding "onto":
        hold_field = dotfield[:fold_pos]
        # the part we'll flip and fold:
        fold_field = np.flipud(dotfield[fold_pos+1:])
    else:
        hold_field = dotfield[:, :fold_pos]
        fold_field = np.fliplr(dotfield[:, fold_pos+1:])
    
    # Do an OR to see where the dots shine through:
    folded_field = np.logical_or(hold_field, fold_field)

    # How many non-zeroes are there after the first fold?
    print(np.count_nonzero(folded_field))

if __name__ == '__main__':
    main()
