from utils.graph import Graph
import heapq as hq

def dijkstra(graph, source):
    """
    Run Dijkstra's algorithm (with binary heap) on a graph
    Input: Graph object, source node
    Output: Dictionary of shortest paths from source node to all other nodes
    """
    assert isinstance(graph, Graph)
    assert source in graph.get_vertices()

    dist = {}
    pq = [(0, source)]

    while pq:
        cur_dist, node = hq.heappop(pq)
        if node in dist:
            continue
        dist[node] = cur_dist
        for child, weight in graph.get_adj(node):
            if child not in dist:
                hq.heappush(pq, (cur_dist + weight, child))

    return dist

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


