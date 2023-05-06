from random import randint
from methods.bnw.low_diam_decomp import boundary
from utils.graph import Graph

# Generate a graph with 1000 vertices
G = Graph()

# Generate random edges with weights
edges = {}
for i in range(1000):
    for j in range(1000):
        if i != j:
            edges[(i, j)] = randint(1, 10)
            G.add_edge(i, j, edges[(i, j)])

# Generate a set of vertices
S = set()
for _ in range(100):
    S.add(randint(0, 999))

# Get the boundary edges
boundary_edges = boundary(G, S, G.get_adj) 

# Assert that the boundary edges are correct
for (s, u, w) in boundary_edges:
    assert s in S
    assert (s, u) in edges

print("Test passed!")
