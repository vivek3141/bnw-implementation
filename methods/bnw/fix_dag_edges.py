from utils.graph import Graph
from utils.topo_sort import topo_sort
from utils.bnw_utils import create_scc_dag

def fix_dag_edges(G: Graph, SCCs: list): # maybe change SCCs to be dictionary?
    G_scc_dag = create_scc_dag(G, SCCs)
    topo_ordering = topo_sort(G_scc_dag) # topo_ordering will store labels to SCCs in topo order
    
    # also figure out how to do vertex to SCC mappings
    vertex_to_scc = # TODO
    
    mu = {j: 0 for j in topo_ordering}
    for u in G.get_vertices():
        for v, weight in G.get_adj(u):
            scc_u = vertex_to_scc[u]
            scc_v = vertex_to_scc[v]
            
            if scc_u != scc_v and weight < mu[topo_ordering[scc_v]]:
                mu[topo_ordering[scc_v]] = weight
    
    M = 0 # mu[topo_ordering[0]] = 0
    phi = {v: 0 for v in G.get_vertices()}
    for j in topo_ordering[1:]:
        M += mu[j] # M_j = sum_{k≤j} mu[k]
        for v in SCCs[j]: # all v ∈ V_j
            phi[v] = M
    
    return phi
        
            
            
    