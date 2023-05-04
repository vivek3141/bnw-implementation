from utils.graph import Graph
from utils.bnw_utils import *
import config
import math
from numpy.random import choice, geometric

# Implement Low Diameter Decomposition

def ldd(G: Graph, D: int, c=1):
    """
    INPUT: an m-edge, n-vertex graph G = (V, E, w) with non-negative edge weight function
           w and a positive integer D
    OUTPUT: A set of edges E^rem with the following guarantees:
            - Each SCC of G \ E^rem has weak diameter at most D; that is, if u,v are in the 
              same SCC, then dist_G(u, v) ≤ D and dist_G(v, u) ≤ D.
            - For every e ∈ E, Pr[e ∈ E^rem] = O(w(e) * log^2(n) / D + n^(-10)). These 
              probabilities are not guaranteed to be independent.
    """
    n = config.n # number of vertices in G_in, initialized in bnw.py
    G_0 = G
    E_rem = set()
    
    # PHASE 1: mark vertices as light or heavy
    k = int(c * math.log(n)) # TODO: need to choose constant c
    assert k <= G.get_num_vertices()
    S = choice(G.get_vertices(), size=k) # sample w/ replacement
    for s in S:
        # TODO: Compute Ball_G^in(s_i, D/4)
        # TODO: Compute Ball_G^out(s_i, D/4)
    for v in G.get_vertices():
        # TODO: compute Ball_G^in(v, D/4) ∩ S and Ball_G^out(v, D/4) ∩ S; using previous procedure
    in_light = set()
    out_light = set()
    heavy = set()
    for v in G.get_vertices():
        # TODO: if |Ball_G^in(v, D/4) ∩ S| ≤ .6k, mark v in-light
        # TODO: elif |Ball_G^out(v, D/4) ∩ S| ≤ .6k, mark v out-light
        # TODO: else: mark v heavy
    
    # PHASE 2: carve out balls until no light vertices remain
    
    all_light = in_light.union(out_light)
    while shared_elems(G.get_vertices(), all_light): # while G contains a light node
        p = min(1, 80 * math.log(n, 2) / D)
        R_v = geometric(p)
        # compute Ball_G^*(v, R_v)
        # if R_v > D // 4 or |Ball_G^*(V, R_v| > 0.7|V(G)| then return E^rem = E(G) and terminate

        # Compute boundary edges of ball: E_boundary = boundary(ball=Ball_G^*(v, R_v), setting="all")
        # Recurse on ball:                E_recurse = ldd(G=G[Ball_G^*(v, R_v)], D)
        # Update E_rem:                   E_rem = E_rem.union(E_boundary).union(E_recurse)
        # Remove ball from G:             G = remove_ball(G=G, ball=Ball_G^*(v, R_v))
    
    # CLEAN UP: check that remaining vertices have small weak diameter in initial input graph G_0
    
    v_arbitrary = G.get_any_vertex()
    # if Ball_G0^in(v, D/2) doesn't contain V(G) or Ball_G0^out(v, D/2) doesn't contain V(G), then 
    # return E^rem = E(G) and terminate
    
    return E_rem
