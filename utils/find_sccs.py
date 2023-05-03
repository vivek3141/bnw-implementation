from utils.graph import Graph

"""
Run Tarjan's algorithm on a graph
Input: Graph object
Output: List of SCCs
"""
def find_sccs(graph):
    
    def find_component(v, disc, low, on_stack, stack):
        nonlocal graph
        nonlocal time
        nonlocal all_sccs
        
        disc[v] = time
        low[v] = time
        time += 1
        on_stack[v] = True
        stack.append(v)
        
        for (u, w) in graph.get_adj(v):
            if disc[u] == -1:
                find_component(u, disc, low, on_stack, stack)
                low[v] = min(low[v], low[u])
            elif on_stack[u]:
                low[v] = min(low[v], disc[u])
        
        curr_scc = []
        w = -1
        if disc[v] == low[v]:
            while w != v:
                w = stack.pop()
                curr_scc.append(w)
                on_stack[w] = False
        
        if curr_scc:
            all_sccs.append(curr_scc)

    time = 0
    disc = {v: -1 for v in graph.get_vertices()}
    low = {v: -1 for v in graph.get_vertices()}
    on_stack = {v: False for v in graph.get_vertices()}
    stack = []

    all_sccs = []
    for v in graph.get_vertices():
        if disc[v] == -1:
            find_component(v, disc, low, on_stack, stack)
    
    return all_sccs

if __name__ == '__main__':
    g1 = Graph()
    g1.add_edge(0, 1, 69)
    g1.add_edge(1, 2, 69)
    g1.add_edge(2, 0, 69)
    g1.add_edge(1, 3, 69)
    g1.add_edge(1, 4, 69)
    g1.add_edge(1, 6, 69)
    g1.add_edge(3, 5, 69)
    g1.add_edge(4, 5, 69)   

    print(f"SCCs of g1:", find_sccs(g1))
    
    g2 = Graph()
    g2.add_edge(0, 1, 69)
    g2.add_edge(0, 3, 69)
    g2.add_edge(1, 2, 69)
    g2.add_edge(1, 4, 69)
    g2.add_edge(2, 0, 69)
    g2.add_edge(2, 6, 69)
    g2.add_edge(3, 2, 69)
    g2.add_edge(4, 5, 69)
    g2.add_edge(4, 6, 69)
    g2.add_edge(5, 6, 69)
    g2.add_edge(5, 7, 69)
    g2.add_edge(5, 8, 69)
    g2.add_edge(5, 9, 69)
    g2.add_edge(6, 4, 69)
    g2.add_edge(7, 9, 69)
    g2.add_edge(8, 9, 69)
    g2.add_edge(9, 8, 69)

    print(f"SCCs of g2:", find_sccs(g2))