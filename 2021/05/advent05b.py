import fileinput

from collections import namedtuple

def main():
    spikes = dict()
    point = namedtuple('point2d', ['x', 'y'])
    for line in fileinput.input():
        p1, p2 = line.split(' -> ')

        p1 = point(*map(lambda a: int(a), p1.split(',')))
        p2 = point(*map(lambda a: int(a), p2.split(',')))

        x = p1.x
        y = p1.y

        # print(f"{p1} {p2}")

        while True:
            spikes.setdefault((x, y), 0)
            spikes[(x, y)] += 1
            # print(f"Incrementing spike on {x} {y} to {spikes[(x,y)]}")

            if x == p2.x and y == p2.y:
                break

            if p1.x < p2.x:
                x = x+1
            elif p1.x > p2.x:
                x = x-1
            else:
                pass # Not diagonal, keep x the same

            if p1.y < p2.y:
                y = y+1
            elif p1.y > p2.y:
                y = y-1
            else:
                pass # Not diagonal, keep y the same.

    print(len([v for v in spikes.values() if v > 1]))


if __name__ == '__main__':
    main()
