import fileinput
import networkx as nx
import numpy as np

def main():
     cave_graph = nx.DiGraph()

     # Make a 2D int list of the input grid:
     cave_grid_orig = np.array([list(map(int, line.strip())) for line in fileinput.input()])
     orig_rows, orig_cols = cave_grid_orig.shape

     # Create the new array.
     cave_grid = np.zeros((orig_rows*5,orig_cols*5), dtype=np.int8)

     # Paste the original into the top-left.
     cave_grid[0:orig_rows,0:orig_cols] = cave_grid_orig
     
     # Add the funky rows:
     for i in range(1,5):
          cave_grid[i*orig_rows:(i+1)*orig_rows,0:orig_cols] = cave_grid[(i-1)*orig_rows:i*orig_rows, 0:orig_cols]%9 + 1

     # Now add the funky columns:
     for i in range(1,5):
          cave_grid[:,i*orig_cols:(i+1)*orig_cols] = cave_grid[:, (i-1)*orig_cols:i*orig_cols]%9 + 1

     # Now we have the whole new gigantic cave grid.

     cave_graph.add_node((0,0))

     # Load up a grid-shaped graph with weights according to risk levels:
     for row in range(orig_rows*5):
          for col in range(orig_cols*5):
               weight = int(cave_grid[row,col])
               # Add all (up to) 4 weights INTO (row, col):
               # (row-1, col) -> (row, col)
               # (row, col-1) -> (row, col)
               # (row+1, col) -> (row, col)
               # (row, col+1) -> (row, col)
               for row_d, col_d in [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]:
                    try:
                         if row_d<0 or col_d<0:
                              raise IndexError()
                         cave_graph.add_edge((row_d, col_d), (row, col), weight=weight)
                         # print(f"Adding {weight}-weight to {row}, {col} from {row_d},{col_d}")
                    except IndexError:
                         continue

     dest_row = row
     dest_col = col

     # shortest_path = nx.shortest_path(cave_graph, (0,0), (dest_row,dest_col), 'weight')
     print(nx.shortest_path_length(cave_graph, (0,0), (dest_row,dest_col), 'weight'))



if __name__ == '__main__':
     main()
