import fileinput
from more_itertools import sliding_window

def main():
    previous_depth = None
    depth_increases = 0
    window_sums = map(sum, sliding_window((int(line) for line in fileinput.input()), 3))
    
    for next_depth in window_sums:
        if previous_depth and next_depth > previous_depth:
            depth_increases += 1
        previous_depth = next_depth
    print(depth_increases)

if __name__ == '__main__':
    main()