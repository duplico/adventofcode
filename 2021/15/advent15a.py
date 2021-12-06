import fileinput
import networkx as nx

def main():
     cave_graph = nx.Graph()

     # Make a 2D char list of the input grid:
     cave_grid = [list(line.strip()) for line in fileinput.input()]

     # Load up a grid-shaped graph with weights according to risk levels:
     for row in range(len(cave_grid)):
          for col in range(len(cave_grid[row])):
               weight = int(cave_grid[row][col])
               if row:
                    cave_graph.add_edge((row, col), (row-1, col), weight=weight)
               if col:
                    cave_graph.add_edge((row, col), (row, col-1), weight=weight)
     
     dest_row = row
     dest_col = col

     print(nx.shortest_path(cave_graph, (0,0), (dest_row,dest_col), 'weight'))

     print(nx.shortest_path_length(cave_graph, (0,0), (dest_row,dest_col), 'weight'))


if __name__ == '__main__':
     main()
