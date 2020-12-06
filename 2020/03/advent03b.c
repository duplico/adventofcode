#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

/// Given an offset and input file, calculate the number of "trees" hit.
int num_trees(uint16_t x_offset, uint16_t y_offset, char *input_file) {
     uint16_t trees = 0;
     uint16_t x_index = 0;
     uint16_t width = 0;
     uint16_t skip = y_offset;
     FILE *tree_file;

     tree_file = fopen(input_file, "r");
     if (tree_file == NULL) {
          // Error opening file.
          fprintf(stderr, "Error opening file.\n");
          exit(1);
     }

     // Fill up this buffer with nulls.
     char line[255] = {0,};

     // Read every line of the file, breaking from the loop when we get
     //  a null return value, indicating EOF.
     while (fgets(line, 254, tree_file)) {
          // If the second to last character of our running line buffer is
          //  not null, we take that as a failure to guarantee we're reading
          //  the whole width of the input file, which is an error.
          if (line[253] != 0x00) {
               fprintf(stderr, "File too wide for line buffer.\n");
               exit(1);
          }

          // If we haven't determined the width of the input, do that now:
          if (!width)
               while (line[width] == '.' || line[width] == '#')
                    width++;
          
          // Determine whether we need to check this line, or if we skip it.
          //  A y_offset of 1 should mean that we will check every line.
          if (skip != y_offset) {
               skip++;
               fprintf(stderr, "%s", line);
               continue;
          } else {
               skip = 1;
          }

          if (line[x_index] == '#') {
               // Tree!
               trees++;
               line[x_index] = 'X';
          } else {
               line[x_index] = 'O';
          }
          
          fprintf(stderr, "%s", line);

          // Increment x_index for the next iteration.
          x_index = (x_index + x_offset) % width;
     }

     fclose(tree_file);

     return trees;
}

int main(int argc, char *argv[]) {
     int32_t x_offset;
     int32_t y_offset;
     char **ptr;
     uint16_t *trees_each_run;
     uint64_t trees_multiplied;

     // Validate input (to the extent we can be bothered)
     if (argc < 4 || (argc % 2) != 0) {
          fprintf(stderr, "Argument count mismatch.\n");
          fprintf(stderr, "Expected: advent03a.c {input_file} {x_offset_1} {y_offset_1} [{x_offset_2} {y_offset_2}] ...  \n");
          exit(1);
     }

     uint8_t num_runs = (argc - 2) / 2;
     char *input_file = argv[1];
     trees_each_run = malloc(sizeof(uint16_t) * num_runs);

     // Start doing each of our tobogan runs or whatever.
     for (uint16_t run_num=1; run_num<=num_runs; run_num++) {
          // Read in X and Y offsets for the run.
          x_offset = strtol(argv[run_num*2], ptr, 10);
          if (x_offset > UINT16_MAX || x_offset < 0) {
               fprintf(stderr, "X offset over/underflow\n");
               exit(1);
          }

          y_offset = strtol(argv[run_num*2 + 1], ptr, 10);
          if (y_offset > UINT16_MAX || y_offset < 0) {
               fprintf(stderr, "Y offset over/underflow\n");
               exit(1);
          }

          trees_each_run[run_num-1] = num_trees((uint16_t) x_offset, (uint16_t) y_offset, input_file);
          
          printf("Run #%d Trees hit: %d\n", run_num, trees_each_run[run_num-1]);
     }

     trees_multiplied = 1;
     for (uint16_t i=0; i<num_runs; i++) {
          trees_multiplied *= trees_each_run[i];
     }

     free(trees_each_run);

     printf("Total trees hit product: %lu\n", trees_multiplied);

     return 0;
}
