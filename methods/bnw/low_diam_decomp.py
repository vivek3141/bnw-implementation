from typing import Union, Set
from numpy.random import choice, geometric
from utils.graph import Graph, SubGraph
from utils.bnw_utils import *


def ldd(G: Union[SubGraph, Graph], D: int, G_0: Graph, c=1, n=None) -> Set:
    """
    INPUT: an m-edge, n-vertex graph G = (V, E, w) with non-negative edge weight function
           w and a positive integer D
    OUTPUT: A set of edges E^rem with the following guarantees:
            - Each SCC of G \\ E^rem has weak diameter at most D; that is, if u,v are in the
              same SCC, then dist_G(u, v) ≤ D and dist_G(v, u) ≤ D.
            - For every e ∈ E, Pr[e ∈ E^rem] = O(w(e) * log^2(n) / D + n^(-10)). These
              probabilities are not guaranteed to be independent.

    Algorithm 3 (pg. 16) as described [here](https://arxiv.org/pdf/2203.03456.pdf#page=18).
    """
    if n is None:
        n = G.get_num_vertices()

    # Line 2: G_0 ← G, Erem ← ∅
    E_rem = set()

    ############################################
    # PHASE 1: mark vertices as light or heavy #
    ############################################

    # Line 3: k ← c ln(n) for large enough constant c
    k = min(int(c * log(n, 2)), G.get_num_vertices())

    # Line 4: S ← {s1, ..., sk}, where each s_i is a random node in V
    S = choice(list(G.get_vertices()), size=k) # sample w/ replacement

    # Line 5: For each si ∈ S compute ball_in(s_i, D/4) and ball_out(s_i, D/4)
    # Line 6: For each v ∈ V compute ball_in(v, D/4) ∩ S and ball_out(v, D/4) ∩ S
    balls_in = []
    balls_out = []
    member_in, member_out = defaultdict(set), defaultdict(set)

    for i in range(len(S)):
        s = S[i]
        ball_in = dijkstra_distance(D//4, s, G.get_rev)
        ball_out = dijkstra_distance(D//4, s, G.get_adj)
        balls_in += [set(ball_in)]
        balls_out += [set(ball_out)]
        for v in ball_in:
            member_out[v].add(s)
        for v in ball_out:
            member_in[v].add(s)

    # Line 7-10: Mark light nodes
    vertices = G.get_vertices()
    light_in = set()
    light_out = set()
    for v in vertices:
        if len(member_out[v]) < 0.6 * k:
            light_in.add(v)
        elif len(member_in[v]) < 0.6 * k:
            light_out.add(v)

    ###########################################################
    # PHASE 2: carve out balls until no light vertices remain #
    ###########################################################

    # Line 11: while G contains a node marked light
    light_all = light_in.union(light_out)
    while light_all:
        v = light_all.pop()

        # Line 12: Sample Rv ∼ Geo(p) for p = min{1, 80*log2(n)/D}
        p = min(1, 80 * log(n, 2) / D)
        R_v = geometric(p)

        # Line 13: Compute ball_*(v, Rv).
        edges = G.get_rev if v in light_in else G.get_adj
        ball = set(dijkstra_distance(R_v, v, edges))
        # Line 14: E_boundary ← boundary(ball_*(v, Rv))
        E_boundary = boundary(G, ball) if v in light_in else boundary_rev(G, ball)

        # Line 15: Terminate
        if R_v > D // 4 or len(ball) > 0.7 * len(vertices):
            return G.get_edges()

        # Line 16: Recurse
        E_recurse = ldd(SubGraph(G, ball), D, G_0, c=c, n=n)

        # Lines 17-18: Update E_rem and remove ball from
        E_rem = E_rem.union(E_boundary).union(E_recurse)
        G = SubGraph(G, G.get_vertices() - ball)
    
    # Lines 19-20: Terminate (check that remaining vertices have small weak diameter in initial input graph G_0)
    v = G.get_any_vertex()
    ball_in_v = set(dijkstra_distance(D//2, v, G_0.get_rev))
    ball_out_v = set(dijkstra_distance(D//2, v, G_0.get_adj))
    if (not G.get_vertices().issubset(ball_in_v)) or (not G.get_vertices().issubset(ball_in_v)):
        return G.get_edges()
        
    return E_rem
