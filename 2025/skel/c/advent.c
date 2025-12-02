/*
 * Advent of Code solution
 * Usage: ./advent <part> <filename> [-v]
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LINE 1024
#define MAX_LINES 10000

static int verbose = 0;

/* Read all lines from file into array, returns line count */
int read_lines(const char *filename, char lines[][MAX_LINE]) {
    FILE *f = fopen(filename, "r");
    if (!f) {
        perror("fopen");
        exit(1);
    }

    int count = 0;
    while (fgets(lines[count], MAX_LINE, f) && count < MAX_LINES) {
        /* Strip trailing newline */
        lines[count][strcspn(lines[count], "\n")] = 0;
        count++;
    }

    fclose(f);
    return count;
}

void part1(const char *filename) {
    char lines[MAX_LINES][MAX_LINE];
    int line_count = read_lines(filename, lines);

    if (verbose) {
        printf("Read %d lines from %s\n", line_count, filename);
    }

    /* TODO: Implement solution */
    int result = 0;

    printf("Part 1: %d\n", result);
}

void part2(const char *filename) {
    char lines[MAX_LINES][MAX_LINE];
    int line_count = read_lines(filename, lines);

    if (verbose) {
        printf("Read %d lines from %s\n", line_count, filename);
    }

    /* TODO: Implement solution */
    int result = 0;

    printf("Part 2: %d\n", result);
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s <part> <filename> [-v]\n", argv[0]);
        return 1;
    }

    int part = atoi(argv[1]);
    const char *filename = argv[2];

    /* Check for verbose flag */
    for (int i = 3; i < argc; i++) {
        if (strcmp(argv[i], "-v") == 0) {
            verbose = 1;
        }
    }

    switch (part) {
        case 1:
            part1(filename);
            break;
        case 2:
            part2(filename);
            break;
        default:
            fprintf(stderr, "Unknown part: %d. Use 1 or 2.\n", part);
            return 1;
    }

    return 0;
}
