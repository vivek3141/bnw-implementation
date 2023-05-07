from typing import Callable
from math import log, ceil
from utils.graph import Graph, SubGraph
from collections import defaultdict
import heapq as hq

def get_modified_graph(G: Graph, scale=1, B=0, is_max_0=False, edges=None, phi=defaultdict(int)):
    G_modified = Graph()

    # Use edges of input G by default
    if not edges:
        edges = G.get_edges()

    for u, v, w in edges:
        w_new = w * scale # apply scaling
        if B and w_new < 0: # if B > 0, then do w^B(e) = w(e) + B if w(e) < 0
            w_new += B
        if is_max_0: # if applicable, take max of w(e) and 0
            w_new = max(0, w_new)
        w_new += phi[u] - phi[v] # apply price function, by default phi=0

        G_modified.add_edge(u, v, w_new)

    return G_modified

def round_up_power_2(x: int):
    return int(2 ** ceil(log(2*x, 2)))

def add_price_fns(phi1, phi2):
    assert len(phi1) == len(phi2)
    return defaultdict(int, {v: phi1[v] + phi2[v] for v in phi1.keys()})

"""
Helper Methods for Low-Diameter Decomposition (LDD)
"""

def shared_elems(set1: set, set2: set):
    return any([elem in set2 for elem in set1])

def dijkstra_distance(D: int, source: int, edges: Callable[[int], list[tuple[int,int]]]):
    dist = {}
    pq = [(0, source)]

    while pq:
        cur_dist, node = hq.heappop(pq)
        if node in dist:
            continue
        dist[node] = cur_dist
        for child, weight in edges(node):
            if child not in dist and dist[node] + weight <= D:
                hq.heappush(pq, (cur_dist + weight, child))

    return dist

def boundary(G: Graph | SubGraph, S: set):
    edges = set()
    for s in S:
        for u, w in G.get_adj(s):
            edges.add((s, u, w))
    return edges

def boundary_rev(G: Graph | SubGraph, S: set):
    edges = set()
    for s in S:
        for u, w in G.get_rev(s):
            edges.add((u, s, w))
    return edges

"""
Helper Methods for Fix-DAG-Edges
"""

def create_scc_dag(G: Graph, SCCs: list) -> Graph:
    # TODO: returns DAG of SCCs
    pass
