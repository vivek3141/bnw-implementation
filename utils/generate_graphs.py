import numpy as np
import argparse
import os
import random
import time
from utils.graph import Graph
from utils.constants import INF
from utils.topo_sort import topo_sort
from methods.bellman_ford import bellman_ford

def generate_random_graph(n: int, p: float =None, W: int=1000):
    if not p:
        p = 1.3 * np.log(n) / n

    G = Graph()
    for i in range(n):
        G.add_vertex(i)

    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                G.add_edge(i, j, random.randint(0, W))

    return G

def generate_negative_random_graph(n: int, p: float=None, W: int =1000, cycles=True):
    """Generates a negative random graph with no negative cycles

    Args:
        n (int): Number of vertices in the graph.
        W (int, optional): Maximum magnitude of any edge weight. Defaults to 1000.
        cycles (bool, optional): Whether or not we generate (positive) cycles. Defaults to True.

    Returns:
        _type_: _description_
    """
    if not p:
        p = 1.3 * np.log(n) / n

    G = Graph()
    for i in range(n):
        G.add_vertex(i)

    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                G.add_edge(i, j, random.randint(-W, W))

    topo_order = topo_sort(G) # TODO: tbh not sure if this works completely correctly
    dist = {v: INF for v in topo_order}
    dist[topo_order[0]] = 0
    for v in topo_order:
        if dist[v] != INF:
            for u, w in G.get_adj(v):
                if dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w
    # assert dist==bellman_ford(G, topo_order[0])
    # dist, _ = bellman_ford(G, topo_order[0])

    # introduce back edges to form non-negative cycles
    for i in range(n):
        for j in range(i+1, n):
            if dist[j] != INF  and dist[i] != INF:
                if dist[i] - dist[j] > W: # dist[j] - dist[i] < -W
                    continue
                else:
                    left = max(dist[i] - dist[j], -W)
                    right = W
            # elif (j in dist) or (i in dist):
                # need to figure out what to do with connecting components
            else:
                continue

            if random.random() < p:
                G.add_edge(j, i, random.randint(left, right))

    return G

def generate_benchmark_graphs(graph_sizes: list, Ws: int, samples: int, dir: str="input_graphs/"):
    for n in graph_sizes:
        for W in Ws:
            start_time = time.time()

            for i in range(samples):
                # Generate non-negative weight graphs

                G_sparse = generate_random_graph(n=n, p=1.3*np.log(n)/n, W=W)
                write_graph_file(G=G_sparse, file_name=f"nonneg_sparse_n={n}_W={W}_sample={i}.txt", dir=dir)

                G_dense = generate_random_graph(n=n, p=n**(-0.5), W=W)
                write_graph_file(G=G_dense, file_name=f"nonneg_dense_n={n}_W={W}_sample={i}.txt", dir=dir)

                # Generate possibly negative weight graphs

                G_sparse = generate_negative_random_graph(n=n, p=1.3 * np.log(n) / n, W=W)
                write_graph_file(G=G_sparse, file_name=f"neg_sparse_n={n}_W={W}_sample={i}.txt", dir=dir)

                G_dense = generate_negative_random_graph(n=n, p=n**(-0.5), W=W)
                write_graph_file(G=G_dense, file_name=f"neg_dense_n={n}_W={W}_sample={i}.txt", dir=dir)

            print(f"Finished generating graphs with (n={n}, W={W}); took {time.time() - start_time} seconds")


def write_graph_file(G: Graph, file_name: str, dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(dir + file_name, "w") as f:
        for u, v, w in G.get_edges():
            f.write(f"{u} {v} {w}\n")


if __name__ == "__main__":
    random.seed(1337)
    np.random.seed(1337)

    parser = argparse.ArgumentParser()
    parser.add_argument('--graph_sizes', type=list, default=[10**i for i in range(1, 5)])
    parser.add_argument('--Ws', type=list, default=[10**i for i in range(1, 10)])
    parser.add_argument('--samples', type=int, default=100)
    args = parser.parse_args()

    generate_benchmark_graphs(graph_sizes=args.graph_sizes, Ws=args.Ws, samples=args.samples,)
