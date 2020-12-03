#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

/// Given an offset and input file, calculate the number of "trees" hit.
int num_trees(uint16_t x_offset, char *input_file) {
     uint16_t trees = 0;
     uint16_t x_index = 0;
     uint16_t width = 0;
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
          
          if (line[x_index] == '#') {
               // Tree!
               trees++;
          }

          // Increment x_index for the next iteration.
          x_index = (x_index + x_offset) % width;
     }

     fclose(tree_file);

     return trees;
}

int main(int argc, char *argv[]) {
     int32_t x_offset;
     char *ptr;

     if (argc != 3) {
          fprintf(stderr, "Argument count mismatch.\n");
          fprintf(stderr, "Expected: advent03a.c {x_offset} {input_file}\n");
          exit(1);
     }

     x_offset = strtol(argv[1], ptr, 10);
     if (x_offset > UINT16_MAX) {
          fprintf(stderr, "X offset too wide\n");
          exit(1);
     }

     char *input_file = argv[2];
     // TODO: Add input file variable here:
     printf("Trees hit: %d\n", num_trees((uint16_t) x_offset, input_file));
     
     return 0;
}
