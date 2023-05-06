from utils.graph import *
from methods.bnw.low_diam_decomp import *


def test_dijkstra_distance():
    G = Graph()
    G.add_edge(1, 2, 5)
    G.add_edge(2, 3, 3)
    G.add_edge(1, 3, 9)
    D = 10
    source = 1
    expected_result = {1: 0, 2: 5, 3: 8}
    assert dijkstra_distance(G, D, source, G.get_adj) == expected_result

def test_boundary():
    G = Graph()
    G.add_edge(1, 2, 5)
    G.add_edge(2, 3, 3)
    edges = G.get_edges()
    S = {1, 3}
    expected_result = {(1, 2, 5), (1, 3, 9)}
    assert boundary(G, S, G.get_adj) == expected_result

def test_ldd():
    G = Graph()
    G.add_edge(0, 1, 5)
    G.add_edge(1, 2, 3)
    G.add_edge(0, 2, 9)
    D = int(23)
    c = 1
    n = G.get_num_vertices()
    expected_result = {(0, 1, 5), (1, 2, 3)}
    result = ldd(G, D, c, n)
    print(result)
    assert ldd(G, D, c, n) == expected_result

if __name__ == "__main__":
    test_dijkstra_distance()
#    test_boundary()
#    test_ldd()
    print("All tests passed!")

