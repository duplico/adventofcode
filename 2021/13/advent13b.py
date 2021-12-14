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
    
    # The dimensions must be odd (so maxes must be even):
    if max_x % 2:
        max_x +=1
    if  max_y % 2:
        max_y += 1
    # NB: This is going to render transposed from the figures on the website.
    dotfield = np.zeros((max_x+1, max_y+1), dtype=np.int0)

    for x,y in dots:
        dotfield[x,y] = 1

    # Do the first fold.
    for fold_dir, fold_pos in folds:
        if fold_dir == 'x':
            # the part we'll be folding "onto":
            hold_field = dotfield[:fold_pos]
            # the part we'll flip and fold:
            fold_field = np.flipud(dotfield[fold_pos+1:])
        else:
            hold_field = dotfield[:, :fold_pos]
            fold_field = np.fliplr(dotfield[:, fold_pos+1:])
        
        # Do an OR to see where the dots shine through:
        dotfield = np.logical_or(hold_field, fold_field).astype(int)

    # print(np.array2string(np.transpose(dotfield), max_line_width=250))

    # Printing it as an int array doesn't look great. Let's do ASCII art instead.
    for row in np.transpose(dotfield):
        for val in row:
            print('#' if val else ' ', end='')
        print()

if __name__ == '__main__':
    main()
