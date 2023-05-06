from random import randint
from methods.bnw.low_diam_decomp import dijkstra_distance
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

# Set the maximum distance to 100
D = 100

# Choose a random source vertex
source = randint(0, 999)

# Perform Dijkstra's algorithm
distances = dijkstra_distance(G, D, source, G.get_adj) 

# Assert that the distances are correct
for vertex in G.vertices:
    if vertex == source:
        assert distances[vertex] == 0
    elif vertex in distances:
        assert distances[vertex] <= D
    else:
        assert vertex not in G.vertices

print("Tests Passed!")

