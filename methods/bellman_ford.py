from collections import defaultdict
from utils.graph import Graph

"""
Run the Bellman-Ford algorithm on a graph
Input: Graph object, source node
Output: Dictionary of shortest paths from source node to all other nodes
"""
def bellman_ford(graph, source):
    assert isinstance(graph, Graph)
    assert source in graph.get_vertices()

    dist: dict[int, int] = {}
    prev = {v:v for v in graph.get_vertices()}
    dist[source] = 0

    # Run through |V|-1 iterations of relaxing all edges
    for _ in range(graph.get_num_vertices()-1):
        for u, v, w in graph.get_edges():
            if u in dist and (v not in dist or dist[u] + w < dist[v]):
                dist[v] = dist[u] + w
                prev[v] = u

    # If can still update distances, then there exists a neg cycle
    for u, v, w in graph.get_edges():
        if u in dist and v in dist and dist[u] + w < dist[v]:
            return -1

    # Create shortest path tree from prev
    sp_tree = defaultdict(set)
    for curr_node, prev_node in prev.items():
        if curr_node != prev_node:
            sp_tree[prev_node].add(curr_node)

    return dist, sp_tree


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'D', 1)
    g.add_edge('B', 'E', 6)
    g.add_edge('C', 'D', 6)
    g.add_edge('C', 'E', 3)
    g.add_edge('D', 'E', 4)
    g.add_edge('D', 'F', 8)
    g.add_edge('E', 'F', 5)

    print(bellman_ford(g, 'A'))


