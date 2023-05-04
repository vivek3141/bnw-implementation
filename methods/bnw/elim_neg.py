from utils.graph import Graph
from copy import deepcopy
import heapq as hq


def elim_neg(G: Graph):
    G_s = deepcopy(G) # not sure if this works lol
    for v in G.get_vertices():
        G_s.add_edge("s", v, 0)
    
    d = {v: float("inf") for v in G_s.get_vertices()}
    d["s"] = 0
    
    pq = [(0, "s")]
    in_pq = {v: False for v in G_s.get_vertices()}
    in_pq["s"] = True
    
    while pq:
        marked = set()
        
        # Dijkstra Phase
        while pq:
            _, v = hq.heappop(pq)
            in_pq[v] = False
            marked.add(v)

            for x, weight in G_s.get_adj(v) if weight >= 0: # E \ E^neg(G)
                if dist[v] + weight < dist[x]:
                    if in_pq[x]:
                        pq.remove((dist[x], x))
                        
                    dist[x] = dist[v] + weight
                    hq.heappush(pq, (dist[x], x))
                    
                    in_pq[x] = True
                    marked.add(x)
        
        # Bellman-Ford Phase 
        for v in marked:
            for x, weight in G_s.get_adj(v) if weight < 0: # E^neg(G)
                if dist[v] + weight < dist[x]:
                    if in_pq[x]:
                        pq.remove((dist[x], x))
                    
                    dist[x] = dist[v] + weight
                    hq.heappush(pq, (dist[x], x))
                    
                    in_pq[x] = True
        
        # note that we unmark all vertices at end of stage
    
    phi = {v: d[v] for v in G.get_vertices()}
    return phi