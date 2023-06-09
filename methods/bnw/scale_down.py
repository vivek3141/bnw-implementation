from typing import Dict
from methods.bnw.elim_neg import elim_neg
from methods.bnw.fix_dag_edges import fix_dag_edges
from methods.bnw.low_diam_decomp import ldd
from utils.graph import Graph
from utils.find_sccs import find_sccs
from utils.bnw_utils import *
import time

def scale_down(G: Graph, Delta: int, B: int, n=None, debug=False) -> Dict:
    """
    INPUT REQUIREMENTS:
        (a) B is positive integer, w is integral, and w(e) ≥ −2B for all e ∈ E
        (b) If the graph G does not contain a negative-weight cycle then the input must satisfy
            η(G^B) ≤ ∆; that is, for every v ∈ V there is a shortest sv-path in G_s^B
            with at most ∆ negative edges
        (c) All vertices in G have constant out-degree

    OUTPUT: If it terminates, the algorithm returns an integral price function φ such that
        w_φ(e) ≥ -B for all e ∈ E

    Algorithm 1 (pg. 8) as described [here](https://arxiv.org/pdf/2203.03456.pdf#page=10).
    """
    if n == None:
        n = G.get_num_vertices()

    # Lines 1-2
    phi_2 = defaultdict(int, {v: 0 for v in G.get_vertices()})
    if Delta > 2:
        # Line 3
        d = Delta // 2
        G_geq0_B = get_modified_graph(G=G, B=B, is_max_0=True)

        #########################################################################
        # PHASE 0: Decompose V into SCCs V1, V2, ... with weak diameter dB in G #
        #########################################################################

        # Line 4
        start_time = time.time()
        Erem = ldd(G_geq0_B, d * B, G_geq0_B, n=n)
        if debug:
            print("LDD runtime:", time.time() - start_time)

        G_Erem = get_modified_graph(G, edges=filter(lambda edge: edge not in Erem, G.get_edges()))

        # Line 5
        sccs = find_sccs(G_Erem)
        scc_map = defaultdict(int)
        for idx in range(len(sccs)):
            scc = sccs[idx]
            for node in scc:
                scc_map[node] = idx

        #############################################################
        # PHASE 1: Make edges inside the SCCs G^B[V_i] non-negative #
        #############################################################

        # Line 6
        H = get_modified_graph(G, edges=filter(lambda edge: scc_map[edge[0]] == scc_map[edge[1]], G.get_edges()))

        # Line 7
        phi_1 = scale_down(G=H, Delta=d, B=B)

        #######################################################
        # PHASE 2: Make all edges in G^B \ E^rem non-negative #
        #######################################################
        G_phi1_B_Erem = get_modified_graph(G=G_Erem, B=B, phi=phi_1)
        
        start_time = time.time()
        psi = fix_dag_edges(G=G_phi1_B_Erem, SCCs=sccs)
        if debug:
            print("FixDAGEdges runtime:", time.time() - start_time)
        
        phi_2 = add_price_fns(phi_1, psi)

    # PHASE 3: Make all edges in G^B non-negative
    G_phi2_B = get_modified_graph(G=G, B=B, phi=phi_2)
    
    start_time = time.time()
    psi_prime = elim_neg(G_phi2_B)
    if debug:
        print("ElimNeg runtime:", time.time() - start_time, "\n")

    phi_3 = add_price_fns(phi_2, psi_prime)

    return phi_3

