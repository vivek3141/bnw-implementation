import sys
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

    dist = bellman_ford(G, 0)
    assert dist == {0: 0, 1: -2, 2: 3, 3: 5, 4: 1, 5: -1}

def test_bnw():
    G = generate_negative_random_graph(1000)
    dist = bellman_ford(G, 0)
    dist2 = bnw(G, 0)
    assert dist == dist2

if __name__ == "__main__":
    test_bellman_ford()
    test_bnw()
    print("All tests passed!")
