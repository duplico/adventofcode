import fileinput
from os.path import commonprefix

def main():
    digit_totals = None
    line_ct = 0

    for line in fileinput.input():
        if digit_totals == None:
            digit_totals = [0] * len(line.strip())
        
        for i in range(len(line.strip())):
            if line[i] == '1':
                digit_totals[i] += 1
        line_ct += 1

    ones = ''.join(map(lambda a: '1' if a>=line_ct/2 else '0', digit_totals))
    zeroes = ''.join(map(lambda a: '0' if a>=line_ct/2 else '1', digit_totals))

    best_zeroes = 0
    best_zero_count = 0

    best_ones = 0
    best_one_count = 0

    print(ones, zeroes)

    for line in fileinput.input():
        one_prefix = commonprefix([line.strip(), ones])
        if len(one_prefix) > best_one_count:
            best_ones = int(line, base=2)
            best_one_count = len(one_prefix)
        
        zero_prefix = commonprefix([line.strip(), zeroes])
        if len(zero_prefix) > best_zero_count:
            best_zeroes = int(line, base=2)
            best_zero_count = len(zero_prefix)

    print(best_ones, best_zeroes)

    print(best_ones * best_zeroes)

if __name__ == '__main__':
    main()
