import fileinput
from scipy.ndimage import label
from numpy import asarray, count_nonzero
from math import prod

def main():
    # Make a map of basins delineated by 9s:
    heightmap = asarray(list(list(map(lambda a: 0 if a == '9' else 1, input.strip())) for input in fileinput.input()))
    labeled_basins, num_basins = label(heightmap)
    basin_sizes = [count_nonzero(labeled_basins == i+1) for i in range(num_basins)]

    print(prod(sorted(basin_sizes)[-3:]))




if __name__ == '__main__':
    main()
