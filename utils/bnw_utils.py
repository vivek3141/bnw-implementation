from typing import Callable, Union, List, Tuple, Dict
from math import log, ceil
from utils.graph import Graph, SubGraph
from collections import defaultdict, deque
import heapq as hq

def get_modified_graph(G: Graph, scale=1, B=0, is_max_0=False, edges=None, phi=defaultdict(int)):
    G_modified = Graph()

    # Use edges of input G by default
    if not edges:
        edges = G.get_edges()

    for vertex in G.get_vertices():
        G_modified.add_vertex(vertex)

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

def sp_tree_to_dist(G: Graph, source: Union[str, int], sp_tree: Dict) -> Dict:
    dist = {source: 0}
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        if node in sp_tree:
            for child in sp_tree[node]:
                dist[child] = dist[node] + G.get_edge_weight(node, child)
                q.append(child)

    return dist


"""
Helper Methods for Low-Diameter Decomposition (LDD)
"""

def shared_elems(set1: set, set2: set):
    return any([elem in set2 for elem in set1])

def dijkstra_distance(D: int, source: int, edges: Callable[[int], List[Tuple[int,int]]]):
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

def boundary(G: Union[Graph, SubGraph], S: set):
    edges = set()
    for s in S:
        for u, w in G.get_adj(s):
            edges.add((s, u, w))
    return edges

def boundary_rev(G: Union[Graph, SubGraph], S: set):
    edges = set()
    for s in S:
        for u, w in G.get_rev(s):
            edges.add((u, s, w))
    return edges

"""
Helper Methods for Fix-DAG-Edges
"""

def create_scc_dag(G: Graph, vertex_to_scc: defaultdict[int, int]) -> Graph:
    dag = Graph()
    seen = set()
    for u, v, _ in G.get_edges():
        uu = vertex_to_scc[u]
        vv = vertex_to_scc[v]
        if (uu, vv) in seen:
            continue
        seen.add((uu, vv))
        if uu != vv:
            dag.add_edge(uu, vv, 1)
    return dag

