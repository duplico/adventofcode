import fileinput
from operator import add

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

    ones = int(''.join(map(lambda a: '1' if a>line_ct/2 else '0', digit_totals)), base=2)
    zeroes = int(''.join(map(lambda a: '0' if a>line_ct/2 else '1', digit_totals)), base=2)

    print(ones*zeroes)

if __name__ == '__main__':
    main()
