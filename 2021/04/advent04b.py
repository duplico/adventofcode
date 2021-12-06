from collections import namedtuple
import fileinput

BINGO_DIMENSION = 5

def main():
    bingo_cards = []
    for line in fileinput.input():
        # The first line is the list of bingo numbers
        if fileinput.isfirstline():
            bingo_numbers = list(map(int, line.strip().split(',')))
        elif not line.strip(): # Blank line; new bingo card.
            bingo_card = namedtuple('Bingocard', ['rows', 'cols', 'won'])
            bingo_card.rows = []
            bingo_card.cols = []
            bingo_card.won = False
            for i in range(BINGO_DIMENSION):
                bingo_card.cols.append(set())
            bingo_cards.append(bingo_card)
        else: # It's a row on a bingo card.
            card_numbers = line.strip().split()
            assert len(card_numbers) == BINGO_DIMENSION
            for i in range(BINGO_DIMENSION):
                # Add each number to its appropriate column set:
                bingo_card.cols[i].add(int(card_numbers[i]))
            # Add a set corresponding to the row to the row set:
            row = set(map(int, card_numbers))
            bingo_card.rows.append(row)
    
    print(f"Read {len(bingo_cards)} bingo cards and {len(bingo_numbers)} numbers.")

    final_message = ""

    for number in bingo_numbers:
        for card in bingo_cards:
            for run in card.rows + card.cols:
                # Ignore a card if it's already won.
                if card.won:
                    continue
                run.discard(number)
                if not run:
                    card.won = True
                    board_sum = sum(map(sum, card.rows))
                    final_message = f"Winning bingo card on {number}, remaining values totaling {board_sum}. Score: {number*board_sum}"
    
    print(final_message)

if __name__ == '__main__':
    main()
