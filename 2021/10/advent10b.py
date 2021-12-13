import fileinput

open_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def main():
    line_scores = []
    for line in fileinput.input():
        nests = []
        for char in line.strip():
            if char in open_close.keys():
                nests.append(char)
            else:
                assert char in open_close.values()
                if open_close[nests.pop()] != char:
                    nests = [] # Clear `nests` so we ignore it later
                    break # Break out of `for char in line`
                
        if not nests:
            continue # Ignore correct lines and error lines

        line_score = 0
        # If we're here, this is an incomplete line, so let's complete it!

        while len(nests): # While there's still something open, close it:
            line_score *= 5
            line_score += scores[open_close[nests.pop()]]
        line_scores.append(line_score)

    print(sorted(line_scores)[int(len(line_scores)/2)])

if __name__ == '__main__':
    main()