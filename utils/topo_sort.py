from utils.graph import Graph

def topo_sort(graph: Graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor, _ in graph.get_adj(node):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph.get_vertices():
        if node not in visited:
            dfs(node)

    return stack[::-1]

