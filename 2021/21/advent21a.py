def main():
    # pos = [4-1, 8-1]
    pos = [10-1, 4-1]
    score = [0, 0]
    die_val = 1

    while max(score) < 1000:
        turn = (die_val+1)%2
        pos[turn] = (pos[turn] + die_val*3 + 3) % 10
        score[turn] += pos[turn]+1
        die_val += 3
        print("player", turn+1, "score", score[turn])

    die_val -= 1
    print(die_val, score, die_val*min(score))

if __name__ == '__main__':
    main()
