from utils.graph import Graph, SubGraph
from utils.bnw_utils import *
import math
from numpy.random import choice, geometric
import heapq as hq

def dijkstra_distance(G: Graph, D: int, source: int, edges):
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

def boundary(G: Graph, S: set, edges):
    ret_edges = set()
    for s in S:
        for u, w in edges(s):
            ret_edges.add((s, u, w))
    return ret_edges


def ldd(G: Graph, D: int, c=1, n=None):
    """
    INPUT: an m-edge, n-vertex graph G = (V, E, w) with non-negative edge weight function
           w and a positive integer D
    OUTPUT: A set of edges E^rem with the following guarantees:
            - Each SCC of G \ E^rem has weak diameter at most D; that is, if u,v are in the
              same SCC, then dist_G(u, v) ≤ D and dist_G(v, u) ≤ D.
            - For every e ∈ E, Pr[e ∈ E^rem] = O(w(e) * log^2(n) / D + n^(-10)). These
              probabilities are not guaranteed to be independent.

    Algorithm 3 (pg. 16) as described in [this paper](https://arxiv.org/pdf/2203.03456.pdf).
    """
    if n is None:
        n = G.get_num_vertices()

    # Line 2: G_0 ← G, Erem ← ∅
    G_0 = G
    E_rem = set()

    ############################################
    # PHASE 1: mark vertices as light or heavy #
    ############################################

    # Line 3: k ← c ln(n) for large enough constant c
    k = min(int(c * math.log(n)), G.get_num_vertices())

    # Line 4: S ← {s1, ..., sk}, where each s_i is a random node in V
    S = choice(list(G.get_vertices()), size=k) # sample w/ replacement

    # Line 5: For each si ∈ S compute ball_in(s_i, D/4) and ball_out(s_i, D/4)
    # Line 6: For each v ∈ V compute ball_in(v, D/4) ∩ S and ball_out(v, D/4) ∩ S
    balls_in = []
    balls_out = []
    member_in, member_out = defaultdict(set), defaultdict(set)

    for i in range(len(S)):
        s = S[i]
        ball_in = dijkstra_distance(G, D//4, s, G.get_rev)
        ball_out = dijkstra_distance(G, D//4, s, G.get_adj)
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
        if len(member_in[v]) < 0.6 * k:
            light_in.add(v)
        elif len(member_out[v]) < 0.6 * k:
            light_out.add(v)

    ###########################################################
    # PHASE 2: carve out balls until no light vertices remain #
    ###########################################################

    # Line 11: while G contains a node marked light
    light_all = light_in.union(light_out)
    while light_all:
        v = light_all.pop()

        # Line 12: Sample Rv ∼ Geo(p) for p = min{1, 80*log2(n)/D}
        p = min(1, 80 * math.log(n, 2) / D)
        R_v = geometric(p)

        # Line 13: Compute ball_*(v, Rv).
        # Line 14: E_boundary ← boundary(ball_*(v, Rv))
        edges = G.get_rev if v in light_in else G.get_adj
        ball = set(dijkstra_distance(G, R_v, v, edges))
        E_boundary = boundary(G, ball, edges)

        # Line 15: Terminate
        if R_v > D // 4 or len(ball) > 0.7 * len(vertices):
            return G.get_edges()

        # Line 16: Recurse
        E_recurse = ldd(SubGraph(G_0, ball), D, c=c, n=n)

        E_rem = E_rem.union(E_boundary).union(E_recurse)
        G = SubGraph(G_0, vertices)

    return E_rem
