from graph import Graph
from collections import namedtuple

inf = float('inf')
Value = namedtuple('value', 'known,d,p')


def make_value(known, d, p):
    return Value(known, d, p)


class UnWeightedPath:
    """
    For unweighted path length.
    """
    def __init__(self, graph: Graph, start: str, end: str):
        self.graph = graph
        self.table = {}
        for vertex in graph.vertices:
            self.table[vertex] = make_value(False, inf, 0)
        self.table[start] = make_value(False, 0, 0)
        self.start = start
        self.end = end

    def bfs(self):
        for counter in range(len(self.graph.vertices)):
            for vertex in self.graph.vertices:
                if (not self.table[vertex].known) and (self.table[vertex].d == counter):
                    self.table[vertex] = make_value(
                        True,
                        self.table[vertex].d,
                        self.table[vertex].p
                    )
                    for v in self.graph.neighbours[vertex]:
                        self.table[v] = make_value(
                            False,
                            counter + 1,
                            vertex
                        )
        return self.table[self.end].d


if __name__ == '__main__':
    g1 = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': ['e'],
        'e': [],
    }

    g1_class = Graph(g1)
    table = UnWeightedPath(g1_class, 'a', 'e')
    print(table.bfs())