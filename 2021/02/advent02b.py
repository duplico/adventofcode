import fileinput
from operator import add

# Limitation: We can't change both aim and xz at the same time:
commands = dict(
    forward=(1, 1, 0),
    down=(0, 0, 1),
    up=(0, 0, -1)
)

def main():
    # This would be better as a NamedTuple:
    position_xza = (0, 0, 0)

    for line in fileinput.input():
        direction, amount = line.split()
        amount = int(amount)

        change_vector = (
            commands[direction][0] * amount,
            commands[direction][1] * position_xza[2] * amount,
            commands[direction][2] * amount
        )

        position_xza = tuple(map(add, position_xza, change_vector))

        print(line.strip(), '->', position_xza)

    print(position_xza[0]*position_xza[1])

if __name__ == '__main__':
    main()