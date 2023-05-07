from typing import Dict
from utils.graph import Graph
from copy import deepcopy
import heapq as hq


def elim_neg(G: Graph) -> Dict:
    G_s = deepcopy(G) # not sure if this works lol
    for v in G.get_vertices():
        G_s.add_edge(-1, v, 0)

    dist = {v: 999999999999999999 for v in G_s.get_vertices()}
    dist[-1] = 0

    pq: list[tuple[int,int]] = [(0, -1)]

    while pq:
        marked = set()

        # Dijkstra Phase
        while pq:
            _, v = hq.heappop(pq)
            marked.add(v)

            for x, weight in G_s.get_adj(v):
                if weight >= 0:
                    if dist[v] + weight < dist[x]:
                        dist[x] = dist[v] + weight
                        hq.heappush(pq, (dist[x], x))
                        marked.add(x)

        # Bellman-Ford Phase
        for v in marked:
            for x, weight in G_s.get_adj(v):
                if weight < 0: # E^neg(G)
                    if dist[v] + weight < dist[x]:
                        dist[x] = dist[v] + weight
                        hq.heappush(pq, (dist[x], x))

        # note that we unmark all vertices at end of stage

    phi = {v: dist[v] for v in G.get_vertices()}
    return phi
