import sys
import numpy as np
import random
from utils.find_sccs import find_sccs
from utils.graph import *
from methods.bnw.low_diam_decomp import *
from methods.dijkstra import *

def test_ldd():
    n = 200
    sys.setrecursionlimit(n*10)
    random.seed(1337)
    np.random.seed(1337)
    G = generate_random_graph(n)
    D = 500
    E_res = ldd(G, D, n=n)
    new_G = Graph()
    for i in range(n):
        new_G.add_vertex(i)

    old_edges = set(G.get_edges())
    for edge in E_res:
        assert edge in old_edges
    for u, v, w in G.get_edges():
        if (u,v,w) not in E_res:
            new_G.add_edge(u, v, w)

    print(len(G.get_edges()), len(new_G.get_edges()), len(E_res), len(new_G.vertices))
    for scc in find_sccs(new_G):
        for node in scc:
            dist = dijkstra(new_G, node)
            for other in scc:
                assert dist[other] <= D

if __name__ == "__main__":
    test_ldd()
    print("All tests passed!")

