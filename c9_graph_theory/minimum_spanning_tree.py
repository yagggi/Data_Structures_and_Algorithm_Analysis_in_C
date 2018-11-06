from topology_sort import NonOrientedGraph
from shortest_path_problem import WeightedPath, inf, make_value


class WeightedNonOrientedGraph(NonOrientedGraph):

    def __init__(self, graph, weights):
        super(WeightedNonOrientedGraph, self).__init__(graph)
        self.weights = dict(weights)

    def weight(self, start, end):
        return self.weights.get((start, end))


class SpanningTree(WeightedPath):

    def __init__(self, graph: WeightedNonOrientedGraph):
        from collections import deque
        self.queue = deque()
        self.graph = graph
        self.table = {}
        for vertex in graph.vertices:
            self.table[vertex] = make_value(False, inf, 0)
        self.start = self.graph.vertices[0]
        self.table[self.start] = make_value(False, 0, 0)

    def prim(self):
        self.queue.appendleft(self.start)
        weight = 0
        tree = []
        while self.queue:
            min_weight = inf
            min_vertex = None
            vertex = self.queue.pop()
            self.known_of(vertex)
            weight += self.distance(vertex)
            for v in self.graph.neighbours[vertex]:
                if not self.is_known(v):
                    if self.graph.weight(vertex, v) < self.distance(v):
                        self.table[v] = make_value(
                            False,
                            self.graph.weight(vertex, v),
                            vertex
                        )
            for v in self.graph.vertices:
                if not self.is_known(v):
                    if self.distance(v) < min_weight:
                        min_weight = self.distance(v)
                        min_vertex = v
            if min_vertex:
                self.queue.appendleft(min_vertex)
        for v in self.table:
            if self.table[v].p:
                tree.append((self.table[v].p, v))
        weight = sum([self.table[x].d for x in self.table])
        return weight, tree


if __name__ == '__main__':
    g = {
        'v1': ['v3', 'v2', 'v4'],
        'v2': ['v1', 'v4', 'v5'],
        'v3': ['v1', 'v4', 'v6'],
        'v4': ['v1', 'v2', 'v3', 'v5', 'v6', 'v7'],
        'v5': ['v2', 'v4', 'v7'],
        'v6': ['v3', 'v4', 'v7'],
        'v7': ['v4', 'v5', 'v6']
    }
    weights = {
        ('v1', 'v2'): 2,
        ('v2', 'v1'): 2,
        ('v1', 'v3'): 4,
        ('v3', 'v1'): 4,
        ('v1', 'v4'): 1,
        ('v4', 'v1'): 1,
        ('v2', 'v4'): 3,
        ('v4', 'v2'): 3,
        ('v2', 'v5'): 10,
        ('v5', 'v2'): 10,
        ('v3', 'v4'): 2,
        ('v4', 'v3'): 2,
        ('v3', 'v6'): 5,
        ('v6', 'v3'): 5,
        ('v4', 'v5'): 7,
        ('v5', 'v4'): 7,
        ('v4', 'v6'): 8,
        ('v6', 'v4'): 8,
        ('v4', 'v7'): 4,
        ('v7', 'v4'): 4,
        ('v5', 'v7'): 6,
        ('v7', 'v5'): 6,
        ('v6', 'v7'): 1,
        ('v7', 'v6'): 1,
    }
    graph = WeightedNonOrientedGraph(g, weights)
    tree = SpanningTree(graph)
    print(tree.prim())
