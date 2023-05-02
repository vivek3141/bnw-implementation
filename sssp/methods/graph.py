from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list) # adjacency list

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))

    def get_adj(self, u):
        return self.adj[u]

    def get_vertices(self):
        return list(self.adj.keys())
    
    def get_edges(self):
        edges = []
        for u in self.adj:
            for v, w in self.adj[u]:
                edges.append((u, v, w))
        return edges

    def get_num_vertices(self):
        return len(self.adj)
    
    """
    Print graph of the format
    u: v1(w1), v2(w2), ...
    """
    def __str__(self):
        s = ""
        for u in self.adj:
            s += str(u) + ": "
            for v, w in self.adj[u]:
                s += str(v) + "(" + str(w) + "), "
            s += "\n"
        return s
 
