from graph import *
import math

# Implement Low Diameter Decomposition

def pre_LDD(G: Graph):
    # TODO: computes SCCs of G and runs LDD only on SCCs that have large weak diameter
    return

def has_large_diam(G: Graph, s: int, D: int):
    # TODO: determine whether or not the given graph has diameter larger than D
    return

def LDD(G: Graph, D: int):
    # TODO: outputs a set of edges e_sep with the following guarantees:
    # 1. each SCC of G \ e_sep has weak diameter at most D
    # 2. for all e in E, Pr[e in e_sep] = O(w(e) * (logn)^(2/D) + n^(-10))
    return

def reversed_edges():
    # TODO: return set of reversed edges
    return

def geo_prob(n: int, r: int):
    # TODO: need to figure out wtf this is LMFAO
    return min(1, (math.log(n) ** 2) / r)

def random_trim():
    # TODO: idk what this does lmao
    return

def get_subgraph(G: Graph, ball: list, setting: bool):
    # TODO: if setting=True, returns subgraph of G containing only vertices in ball
    #       if setting=False, returns subgraph of G containing only vertices outside ball
    return

def vertex_union(v_set1: list, v_set2: list):
    return list(set(v_set1).union(set(v_set2)))

def edge_union(e_set1: list, _eset2: list):
    # TODO: union the two edge sets
    return

def diff_vertex(v_set1: list, v_set2: list):
    # TODO: returns a vertex in v_set1 that is not in v_set2, or None if they are equal
    return

def create_G_rev(G: Graph):
    # TODO: creates copy of G with all edges reversed
    return

def layer_range(G: Graph, G_rev: Graph, s: int, D: int):
    # TODO: runs layer range on G and G_rev in parallel
    return 

def layer_range_util():
    # TODO: runs a single iteration of layer range
    return

def same_canonical_range():
    # TODO: checks whether Vol_G(s, i- ceil[D/(3logn)]) and Vol_G(S, i) are in the same canonical range
    return

def create_layer(G: Graph, ball: list):
    # TODO: creates {(u, v) in E_H | u in V_H(s, r) and v not in V_H(s, r)}
    return

def volume(G: Graph, s: int, r: int):
    # TODO: outputs all vertices in G within distance r from source s (using Dijkstra's)

def dijkstra(G: Graph, s: int):
    # TODO: run Dijkstra's with source s
    return

 