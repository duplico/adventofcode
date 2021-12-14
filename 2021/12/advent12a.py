import fileinput
import networkx as nx
import pylab

def path_count(graph: nx.Graph, curr_node: str, visited : tuple = ()) -> int:
    visited = visited + (curr_node,)
    # print(f"Path so far: {visited}")
    if curr_node == 'end':
        print(visited)
        return 1
    
    count = 0
    for adj in graph.adj[curr_node]:
        if adj == adj.upper() or adj not in visited:
            count += path_count(graph, adj, visited)
    return count

def main():
    cave_graph = nx.Graph()
    for line in fileinput.input():
        a, b = line.strip().split('-')
        cave_graph.add_edge(a,b)

    nx.draw(cave_graph, with_labels=True, node_size=800)
    pylab.savefig("advent12a.png")

    print(path_count(cave_graph, 'start'))
    

if __name__ == '__main__':
    main()