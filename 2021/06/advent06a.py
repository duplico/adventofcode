import fileinput
from collections import namedtuple

def main():
    starting_fish = fileinput.input().readline().strip().split(',')
    starting_fish = list(map(int, starting_fish))

    fish_current = {x: 0 for x in range(8+1)}

    for fish_life in starting_fish:
        fish_current[fish_life] += 1

    for i in range(80):
        fish_next = {x: 0 for x in range(8+1)}

        for life, count in fish_current.items():
            if life == 0:
                fish_next[8] += count
                fish_next[6] += count
            else:
                fish_next[life-1] += count
        
        fish_current = fish_next

    print(sum(fish_current.values()))

if __name__ == '__main__':
    main()