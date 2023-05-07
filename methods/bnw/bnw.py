# Full implementation of BNW, can reference https://github.com/nevingeorge/Negative-Weight-SSSP
import math
from typing import Union
from methods.bnw.scale_down import scale_down
from methods.dijkstra import dijkstra
from utils.graph import Graph
from utils.bnw_utils import *

def bnw(G_in: Graph, s_in: Union[str, int], debug=False): # G_in = (V, E, w_in)
    """Main Procedure for BNW Algorithm

    Args:
        G_in: graph with integral, possibly negative edge weights in the range [-W, ... W]
        s_in: source node

    Returns:
        (1) shortest path distances from s_in to all nodes in G_in
        (2) shortest path tree
    """
    n = G_in.get_num_vertices()

    B = round_up_power_2(2*n) # rounds 2n to next power of 2
    phi: defaultdict[int, int] = defaultdict(int, {v: 0 for v in G_in.get_vertices()})
    for i in range(1, int(math.log(B, 2)+1)):
        # G_bar_phi = (V, E, w_bar_phi) where w_bar(e) = w_in(e) * 2n + phi(u) - phi(v)
        G_bar_phi = get_modified_graph(G_in, scale=2*n, phi=phi)
        psi = scale_down(G=G_bar_phi, Delta=n, B=(B // 2**i), n=n, debug=debug)
        phi = add_price_fns(phi, psi)

    phi_star = defaultdict(int, {v: phi[v] + 1 for v in phi})
    G_star = get_modified_graph(G_in, scale=2*n, phi=phi_star)
    _, sp_tree = dijkstra(G_star, s_in) # obtain the sp tree of G_in
    dist = sp_tree_to_dist(G_in, s_in, sp_tree)

    return dist, sp_tree

