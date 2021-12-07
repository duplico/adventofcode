import fileinput
from collections import namedtuple

def main():
    starting_positions = fileinput.input().readline().strip().split(',')
    starting_positions = list(map(int, starting_positions))

    best_pos = 0
    best_pos_fuel = None

    for dest_pos in range(min(starting_positions), max(starting_positions)+1):
        pos_fuel = 0
        for src_pos in starting_positions:
            pos_fuel += abs(src_pos - dest_pos)
        if not best_pos_fuel or pos_fuel < best_pos_fuel:
            best_pos_fuel = pos_fuel
            best_pos = dest_pos
    
    print(f"Best position is {best_pos}, using {best_pos_fuel} fuel.")

if __name__ == '__main__':
    main()