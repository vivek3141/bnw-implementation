from graph import Graph
import heapq as hq

"""
Run dijkstra's algorithm on a graph
Input: Graph object, start node
Output: Dictionary of shortest paths from start node to all other nodes
"""
def dijkstra(graph, start):
    assert isinstance(graph, Graph)
    assert start in graph.get_vertices()

    dist = {v: float('inf') for v in graph.get_vertices()}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, node = hq.heappop(pq)

        for child, weight in graph.get_adj(node):
            if cur_dist + weight < dist[child]:
                dist[child] = cur_dist + weight
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


