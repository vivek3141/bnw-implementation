import unittest
from utils.graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(0, 1, 5)
        self.graph.add_edge(0, 2, 3)
        self.graph.add_edge(1, 2, 2)
        self.graph.add_edge(1, 3, 6)
        self.graph.add_edge(2, 3, 7)

    def test_get_adj(self):
        self.assertEqual(self.graph.get_adj(0), [(1, 5), (2, 3)])
        self.assertEqual(self.graph.get_adj(1), [(2, 2), (3, 6)])
        self.assertEqual(self.graph.get_adj(2), [(3, 7)])
        self.assertEqual(self.graph.get_adj(3), [])

    def test_get_vertices(self):
        self.assertEqual(self.graph.get_vertices(), {0, 1, 2, 3})

    def test_get_edges(self):
        self.assertEqual(self.graph.get_edges(), [(0, 1, 5), (0, 2, 3), (1, 2, 2), (1, 3, 6), (2, 3, 7)])

    def test_get_num_vertices(self):
        self.assertEqual(self.graph.get_num_vertices(), 4)

    def test_str(self):
        expected_output = "0: 1(5), 2(3), \n1: 2(2), 3(6), \n2: 3(7), \n3: \n"
        self.assertEqual(str(self.graph), expected_output)

if __name__ == '__main__':
    unittest.main()

