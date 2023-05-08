# Run all experiments and compare different neg-sssp methods
from glob import glob
import argparse
from methods.bnw.bnw import bnw
from methods import dijkstra
from methods import mcmf

# /input_graphs/neg_dense_n=10_W=10_sample=0.txt

def run_n_benchmarks(graph_sizes: list, default_W=1000, input_graph_dir="input_graphs/*"):
    bf_runtimes = {}
    bnw_runtimes = {}
    
    graph_files = {n: [] for n in graph_sizes}
    for file_name in glob(input_graph_dir):
        for n in graph_sizes:
            if f"_sparse_n={n}_W={default_W}_" in file_name:
                graph_files[n].append(file_name)
                print(n, file_name)

# def run_W_benchmarks(Ws: list, input_graph_dir="input_graphs/"):
    
# def run_density_benchmarks(densities: list, input_graph_dir="input_graphs/")
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--graph_sizes", type=list, default=[10**i for i in range(1, 4)])
    parser.add_argument("--Ws", type=list, default=[10**i for i in range(1, 10)])
    parser.add_argument("--densities", type=list, default=["dense", "sparse"])
    args = parser.parse_args()
    
    run_n_benchmarks(graph_sizes=args.graph_sizes)
    # parser.add_argument("--samples", type=int, default=100)
    
    
    



