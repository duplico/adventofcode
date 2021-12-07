import fileinput

from collections import namedtuple

def main():
    spikes = dict()
    point = namedtuple('point2d', ['x', 'y'])
    for line in fileinput.input():
        p1, p2 = line.split(' -> ')

        p1 = point(*map(lambda a: int(a), p1.split(',')))
        p2 = point(*map(lambda a: int(a), p2.split(',')))
        
        # Only consider horizontal or vertical lines:
        if p1.x == p2.x:
            # print(p1, p2)
            x = p1.x
            for y in range(min(p1.y, p2.y), max(p1.y, p2.y)+1):
                spikes.setdefault((x, y), 0)
                spikes[(x, y)] += 1
                # print(f"Incrementing spike on {x} {y} to {spikes[(x,y)]}")
        elif p1.y == p2.y:            
            # print(p1, p2)
            y = p1.y
            for x in range(min(p1.x, p2.x), max(p1.x, p2.x)+1):
                spikes.setdefault((x, y), 0)
                spikes[(x, y)] += 1
                # print(f"Incrementing spike on {x} {y} to {spikes[(x,y)]}")
        else:
            pass # Diagonal.
            # print(f"Ignoring {p1} {p2}")

    print(len([v for v in spikes.values() if v > 1]))


if __name__ == '__main__':
    main()
