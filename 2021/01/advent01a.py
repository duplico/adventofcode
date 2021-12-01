import fileinput

def main():
    previous_depth = None
    depth_increases = 0
    for line in fileinput.input():
        next_depth = int(line)
        if previous_depth and next_depth > previous_depth:
            depth_increases += 1
        previous_depth = next_depth
    print(depth_increases)

if __name__ == '__main__':
    main()