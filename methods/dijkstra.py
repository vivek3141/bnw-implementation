from utils.graph import Graph
from collections import defaultdict
import heapq as hq

def dijkstra(graph: Graph, source):
    """Run Dijkstra's algorithm (with binary heap) on a graph
    
    Args: 
        graph: input graph
        source: source node
        
    Returns: 
        dist: Dictionary of shortest path distances from source node to all other nodes
        prev: Dictionary of previous node in SSSP tree
    """
    assert isinstance(graph, Graph)
    assert source in graph.get_vertices()

    dist = {v: 1e20 for v in graph.get_vertices()}
    visited = {v: False for v in graph.get_vertices()}
    prev = {v: v for v in graph.get_vertices()}
    pq = [(0, source)]

    while pq:
        cur_dist, node = hq.heappop(pq)
        visited[node] = True

        for child, weight in graph.get_adj(node):
            if not visited[child] and cur_dist + weight < dist[child]:
                dist[child] = cur_dist + weight
                prev[child] = node
                
                hq.heappush(pq, (dist[child], child))
    
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

    print(dijkstra(g, 'A'))


