import random
import numpy as np
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list) # adjacency list
        self.rev = defaultdict(list) # adjacency list
        self.vertices: set[int] = set()

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, u, v, w):
        assert u != v, "No self-loops"

        self.vertices.add(u)
        self.vertices.add(v)

        self.adj[u].append((v, w))
        self.rev[v].append((u, w))

    def get_adj(self, u):
        return self.adj[u]

    def get_rev(self, u):
        return self.rev[u]

    def get_vertices(self):
        return self.vertices

    def get_any_vertex(self):
        assert self.vertices
        v = None
        for v in self.vertices:
            break
        return v

    def get_edges(self):
        edges = []
        for u in self.adj:
            for v, w in self.adj[u]:
                edges.append((u, v, w))
        return edges

    def get_num_vertices(self):
        return len(self.vertices)

    """
    Print graph of the format
    u: v1(w1), v2(w2), ...
    """
    def __str__(self):
        s = ""
        for u in sorted(list(self.vertices)):
            s += str(u) + ": "
            for v, w in self.get_adj(u):
                s += str(v) + "(" + str(w) + "), "
            s += "\n"
        return s

class SubGraph:
    def __init__(self, parent: Graph, subset: set[int]):
        self.parent = parent
        self.subset = subset

    def add_edge(self):
        raise Exception("Cannot add edges on a sub-graph")

    def get_adj(self, u):
        return [edge for edge in self.parent.adj[u] if edge[0] in self.subset]

    def get_rev(self, u):
        return [edge for edge in self.parent.rev[u] if edge[0] in self.subset]

    def get_vertices(self):
        return self.subset

    def get_any_vertex(self):
        assert self.subset
        v = None
        for v in self.subset:
            break
        return v

    def get_edges(self):
        edges = []
        for u in self.get_vertices():
            for v, w in self.get_adj(u):
                edges.append((u, v, w))
        return edges

    def get_num_vertices(self):
        return len(self.subset)

def generate_random_graph(n: int):
    G = Graph()
    for i in range(n):
        G.add_vertex(i)

    p = 1.3 * np.log(n) / n
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                G.add_edge(i, j, random.randint(10, 100))

    return G

def generate_negative_random_graph(n: int):
    G = Graph()
    for i in range(n):
        G.add_vertex(i)

    p = 1.3 * np.log(n) / n
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                G.add_edge(i, j, random.randint(-10, 100))

    return G

