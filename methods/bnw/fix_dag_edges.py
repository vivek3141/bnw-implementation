from typing import Dict
from collections import defaultdict
from utils.graph import Graph
from utils.topo_sort import topo_sort
from utils.bnw_utils import create_scc_dag

def fix_dag_edges(G: Graph, SCCs: list) -> Dict: # maybe change SCCs to be dictionary?
    vertex_to_scc = defaultdict(int)
    for i in range(len(SCCs)):
        scc = SCCs[i]
        for node in scc:
            vertex_to_scc[node] = i

    G_scc_dag = create_scc_dag(G, vertex_to_scc)
    topo_ordering = topo_sort(G_scc_dag) # topo_ordering will store labels to SCCs in topo order

    mu = {j: 0 for j in topo_ordering}
    for u in G.get_vertices():
        for v, weight in G.get_adj(u):
            scc_u = vertex_to_scc[u]
            scc_v = vertex_to_scc[v]

            if scc_u != scc_v and weight < mu[scc_v]:
                mu[scc_v] = weight

    M = 0 # mu[topo_ordering[0]] = 0
    phi = {v: 0 for v in G.get_vertices()}
    for j in topo_ordering[1:]:
        M += mu[j] # M_j = sum_{k≤j} mu[k]
        for v in SCCs[j]: # all v ∈ V_j
            phi[v] = M

    return phi




