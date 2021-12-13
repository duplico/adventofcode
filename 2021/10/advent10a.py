import fileinput

open_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def main():
    error_score = 0

    for line in fileinput.input():
        nests = []
        for char in line.strip():
            if char in open_close.keys():
                nests.append(char)
            else:
                assert char in open_close.values()
                if open_close[nests.pop()] != char:
                    error_score += scores[char]
                    break # Break out of `for char in line`
                
    print(error_score)

if __name__ == '__main__':
    main()