import fileinput
from operator import add

commands = dict(
    forward=(1, 0),
    down=(0,1),
    up=(0,-1)
)

def main():
    position_xz = (0, 0)

    for line in fileinput.input():
        direction, amount = line.split()
        amount = int(amount)

        change_vector = map(lambda a: a*amount, commands[direction])
        position_xz = tuple(map(add, position_xz, change_vector))

    print(position_xz[0]*position_xz[1])

if __name__ == '__main__':
    main()