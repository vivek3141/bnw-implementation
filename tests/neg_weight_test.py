import numpy as np
import random
from utils.graph import *
from methods.bellman_ford import bellman_ford
from methods.bnw.bnw import bnw

def test_bellman_ford():
    G = Graph()
    G.add_edge(0, 2, 3)
    G.add_edge(0, 4, 3)
    G.add_edge(0, 5, -1)
    G.add_edge(1, 4, 4)
    G.add_edge(4, 1, -3)
    G.add_edge(1, 5, 3)
    G.add_edge(2, 3, 2)
    G.add_edge(2, 4, -2)
    G.add_edge(4, 5, -1)
    G.add_edge(3, 1, 2)

    dist, _ = bellman_ford(G, 0)
    assert dist == {0: 0, 1: -2, 2: 3, 3: 5, 4: 1, 5: -1}

def test_bnw():
    random.seed(1337)
    np.random.seed(1337)

    G = generate_negative_random_graph(20)
    dist1, sp_tree1 = bellman_ford(G, 0)
    dist2, sp_tree2 = bnw(G, 0)
    print("Shortest Path Distances:")
    print("BF:", dist1)
    print("BNW:", dist2)
    
    print("\nShortest Path Trees:")
    print("BF:", sp_tree1)
    print("BNW", sp_tree2, "\n")
    
    assert dist1 == dist2
    assert sp_tree1 == sp_tree2

if __name__ == "__main__":
    test_bellman_ford()
    test_bnw()
    print("All tests passed!")
