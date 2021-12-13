import fileinput

def risk_score(row, col, heightmap) -> int:
    for row_d, col_d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        try:
            if row+row_d < 0 or col+col_d < 0:
                raise IndexError() # Disallow negative indices.
            if heightmap[row+row_d][col+col_d] <= heightmap[row][col]:
                return 0
        except IndexError:
            pass # Runoff at ({row+row_d}, {col+col_d})
    return heightmap[row][col] + 1

def main():
    risk_total = 0
    heightmap = list(list(map(int, input.strip())) for input in fileinput.input())
    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            risk_total += risk_score(row, col, heightmap)

    print(risk_total)


if __name__ == '__main__':
    main()
