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
        from collections import deque
        self.queue = deque()
        self.graph = graph
        self.table = {}
        for vertex in graph.vertices:
            self.table[vertex] = make_value(False, inf, 0)
        self.table[start] = make_value(False, 0, 0)
        self.start = start
        self.end = end

    def known_of(self, vertex):
        self.table[vertex] = make_value(
            True,
            self.table[vertex].d,
            self.table[vertex].p
        )

    def is_known(self, vertex):
        return self.table[vertex].known

    def distance(self, vertex):
        return self.table[vertex].d

    def bfs(self):
        for counter in range(len(self.graph.vertices)):
            for vertex in self.graph.vertices:
                if (not self.table[vertex].known) and (self.table[vertex].d == counter):
                    self.known_of(vertex)
                    for v in self.graph.neighbours[vertex]:
                        self.table[v] = make_value(
                            False,
                            counter + 1,
                            vertex
                        )
        return self.table[self.end].d

    def better_bfs(self):
        self.queue.appendleft(self.start)
        while self.queue:
            vertex = self.queue.pop()
            counter = self.table[vertex].d
            for v in self.graph.neighbours[vertex]:
                if self.table[v].d == inf:
                    self.table[v] = make_value(
                        False,
                        counter + 1,
                        vertex
                    )
                    self.queue.appendleft(v)
        return self.table[self.end].d


class WeightedGraph(Graph):
    def __init__(self, graph, weights):
        super(WeightedGraph, self).__init__(graph)
        self.weights = dict(weights)

    def weight(self, start, end):
        return self.weights.get((start, end))


class WeightedPath(UnWeightedPath):

    def dijkstra(self):
        """
        Weighted shortest path solution: Dijkstra algorithm
        :return:
        """
        self.queue.appendleft(self.start)
        while self.queue:
            vertex = self.queue.pop()
            self.known_of(vertex)
            for v in self.graph.neighbours[vertex]:
                if not self.is_known(v):
                    if self.distance(v) > self.distance(vertex) + self.graph.weight(vertex, v):
                        self.table[v] = make_value(
                            False,
                            self.distance(vertex) + self.graph.weight(vertex, v),
                            vertex
                        )
                        if v not in self.queue:
                            self.queue.appendleft(v)
        return self.distance(self.end)

    def path(self):
        if self.distance(self.end) == inf:
            print('Run dijkstra method first.')
            return
        s = vertex = self.end
        while vertex != self.start:
            last_vertex = self.table[vertex].p
            cost = self.graph.weight(last_vertex, vertex)
            s = f'{last_vertex}--({cost})-->{s}'
            vertex = last_vertex
        return s


if __name__ == '__main__':
    g = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': ['e'],
        'e': [],
    }

    print(f'UNWEIGHTED GRAPH: {g}\nSTART: "a", END: "e"')
    graph = Graph(g)
    table = UnWeightedPath(graph, 'a', 'e')
    print(f'BFS RESULT: {table.bfs()}')
    table2 = UnWeightedPath(graph, 'a', 'e')
    print(f'BETTER BFS RESULT: {table2.better_bfs()}')
    weights = {
        ('a', 'b'): 10,
        ('a', 'c'): 5,
        ('b', 'd'): 13,
        ('c', 'd'): 1,
        ('d', 'e'): 2,
    }
    weighted_graph = WeightedGraph(g, weights)
    table3 = WeightedPath(weighted_graph, 'a', 'e')
    print(f'ADD WEIGHTS TO GRAPH ABOVE\nWEIGHTS: {weights}')
    print(f'DIJKSTRA RESULT: {table3.dijkstra()}\nPATH: {table3.path()}')
