# Run all experiments and compare different neg-sssp methods

"""
1. BNW [Jonny]
2. Bellman-Ford [Jonny]
3. Dijkstra's (only non-negative edge weights) [Jonny]
4. Linear-Programming
5. Johnson-Dijktra
6. Gabow's Scaling (only non-negative edge weights)
7. Goldberg
8. Min-Cost Max-Flow (modified for SSSP)
9. Hybrid SSSP: https://journals.tubitak.gov.tr/elektrik/vol27/iss4/20/  
10. Genetic Algorithm: https://ieeexplore.ieee.org/abstract/document/4230957
11. LQ Algorithm: https://ieeexplore.ieee.org/abstract/document/4730916

[Probably not] Linear Time Undirected SSSP (using word RAM): https://dl.acm.org/doi/abs/10.1145/316542.316548
[Probably not] Average Linear Time Directed SSSP (using word RAM): https://dl.acm.org/doi/abs/10.5555/365411.365784
"""