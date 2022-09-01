from collections import defaultdict

def main():
    # pos = [4-1, 8-1]
    pos = [10-1, 4-1]
    score = [0, 0]
    die_val = 1

    wins = [0, 0]
    position_counts = [{pos[0]: 1}, {pos[1]: 1}]
    score_counts = [defaultdict(lambda: 0), defaultdict(lambda: 0)]

    # First, use brute force to calculate how many dice combinations
    #  can result in each summed dice values, generating a dict like
    #  roll_counts[roll_total_value] = number_of_ways_to_get_it
    roll_counts = defaultdict(lambda: 0)
    for d1 in range(1,4):
        for d2 in range(1,4):
            for d3 in range(1,4):
                roll_counts[d1+d2+d3] += 1
    
    # Now, play all the games and branch them simultaneously.
    while True:
        for roll_val, roll_count in roll_counts.items:
            pass

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
