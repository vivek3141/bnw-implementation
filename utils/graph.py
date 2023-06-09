from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list) # adjacency list
        self.rev = defaultdict(list) # adjacency list
        self.edge_weights = dict()
        self.vertices: set[int] = set()
        self.num_edges = 0

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, u, v, w):
        assert u != v, "No self-loops"

        self.vertices.add(u)
        self.vertices.add(v)

        self.adj[u].append((v, w))
        self.rev[v].append((u, w))
        self.edge_weights[(u, v)] = w
        self.num_edges += 1

    def get_adj(self, u):
        return self.adj[u]

    def get_rev(self, u):
        return self.rev[u]

    def get_vertices(self):
        return self.vertices

    def get_any_vertex(self):
        assert isinstance(self.vertices, set)
        v = None
        for v in self.vertices:
            break
        return v

    def get_edge_weight(self, u, v):
        return self.edge_weights[(u, v)]

    def get_edges(self):
        edges = []
        for u in self.adj:
            for v, w in self.adj[u]:
                edges.append((u, v, w))
        return edges

    def get_num_vertices(self):
        return len(self.vertices)
    
    def get_num_edges(self):
        return self.num_edges

    """
    Print graph of the format
    u: v1(w1), v2(w2), ...
    """
    def __str__(self):
        s = ""
        for u in sorted(list(self.vertices)):
            for v, w in self.get_adj(u):
                s += f"{u} {v} {w}\n"
        return s

class SubGraph:
    def __init__(self, parent: Graph, subset: set[int]):
        self.parent = parent
        self.subset = subset

    def add_edge(self):
        raise Exception("Cannot add edges on a sub-graph")

    def get_adj(self, u):
        return [edge for edge in self.parent.get_adj(u) if edge[0] in self.subset]

    def get_rev(self, u):
        return [edge for edge in self.parent.get_rev(u) if edge[0] in self.subset]

    def get_vertices(self):
        return self.subset

    def get_any_vertex(self):
        isinstance(self.subset, set)
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

    def __str__(self):
        s = ""
        for u in sorted(list(self.get_vertices())):
            for v, w in self.get_adj(u):
                s += f"{u} {v} {w}\n"
        return s
