import numpy as np
import argparse
import os
import random
import timeit
import tqdm
from collections import defaultdict
from methods.bnw.bnw import bnw
from methods.bellman_ford import bellman_ford
from methods import dijkstra
from utils.graph import Graph
from utils.generate_graphs import generate_random_graph, generate_negative_random_graph

def squish(value, start, end):
    """
    Squishes start <= value <= end linearly between 0 and 1
    """
    return (value - start) / (end - start)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run size experiments')
    parser.add_argument('--neg', action='store_true', help='Generate negative weights')
    parser.add_argument('--method', type=str, default='bnw', help='Method to use')
    parser.add_argument('--n', type=int, default=100, help='Number of nodes')
    parser.add_argument('--W', type=int, default=1000, help='Maximum absolute weight')
    parser.add_argument('--seed', type=int, default=None, help='Random seed')
    parser.add_argument('--num_trials', type=int, default=1000, help='Number of trials')
    parser.add_argument('--output', type=str, default='size.csv', help='Output file')
    args = parser.parse_args()

    if args.neg:
        generate_random_graph = generate_negative_random_graph

    if args.seed is not None:
        np.random.seed(args.seed)
        random.seed(args.seed)

    if args.method == 'bnw':
        method = bnw
    elif args.method == 'bellman_ford':
        method = bellman_ford
    elif args.method == 'dijkstra':
        method = dijkstra
    else:
        raise ValueError('Invalid method')
    
    if os.path.exists(args.output):
        raise ValueError('Output file already exists')

    times = defaultdict(list)
    for i in tqdm.tqdm(range(args.num_trials)):
        g = generate_random_graph(args.n, squish(i, 0, args.num_trials), args.W)
        if args.neg and bellman_ford(g, 0) == (-1, -1):
            continue
        start = random.randint(0, args.n - 1)
        times[g.get_num_edges()].append(timeit.timeit(lambda: method(g, start), number=1))

    # Write to file
    with open(args.output, 'w') as f:
        for m, t in times.items():
            f.write(f'{m},{np.mean(t)}\n')
            f.flush()

