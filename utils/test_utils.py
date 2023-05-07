import numpy as np
import random
from utils.graph import Graph
from utils.constants import INF
from utils.topo_sort import topo_sort
from methods.bellman_ford import bellman_ford

def generate_random_graph(n: int):
    G = Graph()
    for i in range(n):
        G.add_vertex(i)

    p = 1.3 * np.log(n) / n
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                G.add_edge(i, j, random.randint(10, 100))

    return G

def generate_negative_random_graph(n: int, W: int =1000, cycles=True):
    """Generates a negative random graph with no negative cycles

    Args:
        n (int): Number of vertices in the graph.
        W (int, optional): Maximum magnitude of any edge weight. Defaults to 1000.
        cycles (bool, optional): Whether or not we generate (positive) cycles. Defaults to True.

    Returns:
        _type_: _description_
    """
    G = Graph()
    for i in range(n):
        G.add_vertex(i)

    p = 1.3 * np.log(n) / n
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                G.add_edge(i, j, random.randint(-W, W))
              
    topo_order = topo_sort(G)
    # dist = {v: INF for v in topo_order}
    # dist[topo_order[0]] = 0
    # for v in topo_order:
    #     if dist[v] != INF:
    #         for u, w in G.get_adj(v):
    #             if dist[v] + w < dist[u]:
    #                 dist[u] = dist[v] + w
    # assert dist==bellman_ford(G, topo_order[0])
    dist, _ = bellman_ford(G, topo_order[0])
    
    # introduce back edges to form non-negative cycles
    for i in range(n):
        for j in range(i+1, n):
            if (j in dist) and (i in dist):
                if dist[i] - dist[j] > W: # dist[j] - dist[i] < -W
                    continue
                else:
                    left = max(dist[i] - dist[j], -W)
                    right = W
            # elif (j in dist) or (i in dist):
                # need to figure out what to do with connecting components
            else:
                continue
                
            if random.random() < p:
                G.add_edge(j, i, random.randint(left, right))
    
    return G

