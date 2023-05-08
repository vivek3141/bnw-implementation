import numpy as np
import random
import argparse
from utils.graph import Graph
from utils.generate_graphs import generate_random_graph, generate_negative_random_graph
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

def test_bnw(graph_size=1000, debug=False):
    random.seed(1337)
    np.random.seed(1337)

    print("Test graphs with strictly non-negative edge weights")
    for i in range(1, 10):
        print(f"    Graph {i}:")
        G = generate_random_graph(graph_size)
        dist1, sp_tree1 = bellman_ford(G, 0)
        dist2, sp_tree2 = bnw(G, 0, debug)

        assert dist1 == dist2
        assert sp_tree1 == sp_tree2

    print("Test graphs with possibly negative edge weights")
    for i in range(1, 10):
        G = generate_negative_random_graph(graph_size)

        dist1, sp_tree1 = bellman_ford(G, 0)
        if dist1 == -1 and sp_tree1 == -1:
            print(f"Skipped i={i} because there exists a negative cycle.")
            continue
        dist2, sp_tree2 = bnw(G, 0, debug)

        print(sp_tree1, sp_tree2)

        assert dist1 == dist2
        assert sp_tree1 == sp_tree2
        print(f"Graph {i} Test Passed!")

    print("Test Negative Weight Graphs")
    for i in range(1, 10):
        G = generate_negative_random_graph(graph_size)

        dist1, sp_tree1 = bellman_ford(G, 0)
        if dist1 == -1 and sp_tree1 == -1:
            print(f"Skipped i={i} because there exists a negative cycle.")
            continue
        dist2, sp_tree2 = bnw(G, 0, debug)

        assert dist1 == dist2
        assert sp_tree1 == sp_tree2
        print(f"Graph {i} Test Passed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--graph_size', type=int, default=1000)
    parser.add_argument('--debug', action="store_true", default=False)
    args = parser.parse_args()

    test_bellman_ford()
    test_bnw(graph_size=args.graph_size, debug=args.debug)
    print("All tests passed!")
