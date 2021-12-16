import fileinput
import networkx as nx
import pylab

def main():
     cave_graph = nx.DiGraph()

     # Make a 2D char list of the input grid:
     cave_grid = [list(line.strip()) for line in fileinput.input()]

     cave_graph.add_node((0,0))

     # Load up a grid-shaped graph with weights according to risk levels:
     for row in range(len(cave_grid)):
          for col in range(len(cave_grid[row])):
               weight = int(cave_grid[row][col])
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
