from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list) # adjacency list
        self.rev = defaultdict(list) # adjacency list
        self.vertices = set()
        self.num_vertices = 0

        # self.weight_scale = 1
        # self.weight_shift = 0

    def add_edge(self, u, v, w):
        assert u != v, "No self-loops"

        if u not in self.vertices:
            self.vertices.add(u)
            self.num_vertices += 1
        if v not in self.vertices:
            self.vertices.add(v)
            self.num_vertices += 1

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
        return self.num_vertices

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

class SubGraph(Graph):
    def __init__(self, parent: Graph, subset: set()):
        self.parent = parent
        self.subset = subset

    def add_edge(self, u, v, w):
        raise Exception("Cannot add edges on a sub-graph")

    def get_adj(self, u):
        return [edge for edge in self.parent.adj[u] if edge[0] in self.subset]

    def get_rev(self, u):
        return [edge for edge in self.parent.rev[u] if edge[0] in self.subset]

    def get_vertices(self):
        return self.subset

    def get_any_vertex(self):
        assert self.subset
        for v in self.subset:
            break
        return v

    def get_edges(self):
        edges = []
        for u in self.vertices():
            for v, w in self.get_adj(u):
                edges.append((u, v, w))
        return edges

    def get_num_vertices(self):
        return len(self.subset)

