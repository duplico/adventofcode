import fileinput
import networkx as nx
import pylab

def path_count(graph: nx.Graph, curr_node: str, visited : tuple = (), small_doubled: bool = False) -> int:
    visited = visited + (curr_node,)
    # print(f"Path so far: {visited}")
    if curr_node == 'end':
        # print(visited)
        return 1
    
    count = 0
    for adj in graph.adj[curr_node]:
        if adj == 'start':
            # We can't visit start multiple times:
            continue
        elif adj == adj.lower() and adj in visited and small_doubled:
            # We can't double-visit more than one small cave:
            continue
        elif adj == adj.lower() and adj in visited:
            # We can explore this one, but we can't double-visit more smalls:
            count += path_count(graph, adj, visited, True)
        else:
            # We can explore this one, and it's not a double-visit:
            count += path_count(graph, adj, visited, small_doubled)
    return count

def main():
    cave_graph = nx.Graph()
    for line in fileinput.input():
        a, b = line.strip().split('-')
        cave_graph.add_edge(a,b)

    nx.draw(cave_graph, with_labels=True, node_size=800)
    pylab.savefig("advent12b.png")

    print(path_count(cave_graph, 'start'))
    

if __name__ == '__main__':
    main()