from shortest_path_problem import WeightedGraph, WeightedPath, make_value, inf
import copy


class FlowGraph(WeightedGraph):
    def insert_weighted_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = [end]
            self.weights[(start, end)] = weight
        else:
            if end not in self.graph[start]:
                self.graph[start].append(end)
                self.weights[(start, end)] = weight
            else:
                self.weights[(start, end)] += weight

    def decrease_edge(self, start, end, cost):
        edge = (start, end)
        if edge not in self.edges:
            raise Exception(f'Edge {edge} not in graph!')
        if cost > self.weights[edge]:
            raise Exception(f'Cost({cost}) larger than weight{self.weights[edge]}!')
        elif cost == self.weights[edge]:
            self.graph[start] = list(filter(lambda x: x != end, self.graph[start]))
            self.weights.pop(edge)
        else:
            self.weights[edge] -= cost


class FlowPath(WeightedPath):

    def dijkstra(self):
        """
        Find the largest augmenting path
        :return: (flow: int, augmenting paths: [(start, end, cost)])
        """
        self.queue.appendleft(self.start)
        while self.queue:
            vertex = self.queue.pop()
            self.known_of(vertex)
            for v in self.graph.neighbours[vertex]:
                if not self.is_known(v):
                    if self.distance(vertex) > self.graph.weight(vertex, v) or self.distance(vertex) == 0:
                        flow = self.graph.weight(vertex, v)
                    else:
                        flow = self.distance(vertex)
                    if flow > self.distance(v) or self.distance(v) == inf:
                        self.table[v] = make_value(
                            False,
                            flow,
                            vertex
                        )
                        if v not in self.queue:
                            self.queue.appendleft(v)
        if self.distance(self.end) == inf:
            return 0, []
        return self.distance(self.end), self.edges_of_path()

    def bfs(self):
        """
        Find the smallest edge number augmenting path
        :return: (flow: int, augmenting paths: [(start, end, cost)]
        """
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
        edges = self.edges_of_path(False)
        if self.distance(self.end) == inf:
            return 0, []
        else:
            flow = min([self.graph.weight(x, y) for x, y in edges])
            edges = [(start, end, flow) for start, end in edges]
            return flow, edges

    def edges_of_path(self, cost=True):
        """
        Calculate augmenting path
        :return: [(start, end, cost), ...,]
        """
        res = []
        if self.distance(self.end) == inf:
            return []
        vertex = self.end
        while vertex != self.start:
            last_vertex = self.table[vertex].p
            if cost:
                cost = self.distance(vertex)
                res.append((last_vertex, vertex, cost))
            else:
                res.append((last_vertex, vertex))
            vertex = last_vertex
        return res


class MaxFlow:
    """
    Implement of a simple max-flow algorithm
    """
    def __init__(self, graph: FlowGraph, start, end):
        self.start = start
        self.end = end
        self.graph = graph
        self.max_flow = 0
        self.__init_flow_graph()
        self.__init_residual_graph()

    def __init_flow_graph(self):
        self.flow_graph = copy.deepcopy(self.graph)
        for edge in self.flow_graph.weights:
            self.flow_graph.weights[edge] = 0

    def __init_residual_graph(self):
        self.residual_graph = copy.deepcopy(self.graph)

    def max_augmenting_ffa(self):
        """
        Implement of Ford-Fulkerson method based on max augmenting.
        :return: int
        """
        counter = 0
        while True:
            path = FlowPath(self.residual_graph, self.start, self.end)
            flow, paths = path.dijkstra()
            if not paths:
                return self.max_flow, counter
            for start, end, cost in paths:
                self.flow_graph.insert_weighted_edge(start, end, cost)
                self.residual_graph.decrease_edge(start, end, cost)
                self.residual_graph.insert_weighted_edge(end, start, cost)
            self.max_flow += flow
            counter += 1

    def ek(self):
        """
        Implement of Edmonds–Karp algorithm
        :return: int
        """
        counter = 0
        while True:
            path = FlowPath(self.residual_graph, self.start, self.end)
            flow, paths = path.bfs()
            if not paths:
                return self.max_flow, counter
            for start, end, cost in paths:
                self.flow_graph.insert_weighted_edge(start, end, cost)
                self.residual_graph.decrease_edge(start, end, cost)
                self.residual_graph.insert_weighted_edge(end, start, cost)
            self.max_flow += flow
            counter += 1


if __name__ == '__main__':
    g = {
        's': ['a', 'b'],
        'a': ['b', 'd', 'c'],
        'c': ['t'],
        'b': ['d'],
        't': [],
        'd': ['t']
    }
    weights = {
        ('s', 'a'): 3,
        ('s', 'b'): 2,
        ('a', 'b'): 1,
        ('a', 'd'): 4,
        ('a', 'c'): 3,
        ('c', 't'): 2,
        ('b', 'd'): 2,
        ('d', 't'): 3,
    }

    g_2 = {
        's': ['a', 'b'],
        'a': ['b', 't'],
        'b': ['t'],
        't': []
    }
    weights_2 = {
        ('s', 'b'): 100000,
        ('s', 'a'): 100000,
        ('a', 'b'): 1,
        ('a', 't'): 100000,
        ('b', 't'): 100000,
    }
    print(f'graph 1: {g}\nweights: {weights}')
    flow_graph_1 = FlowGraph(g, weights)
    max_flow_1 = MaxFlow(flow_graph_1, 's', 't')
    flow_graph_2 = FlowGraph(g_2, weights_2)
    max_flow_2 = MaxFlow(flow_graph_2, 's', 't')
    print(f"graph_1's max flow and circle counter calculated by max_augmenting_ffa: {max_flow_1.max_augmenting_ffa()}")
    print(f"graph_2's max flow and circle counter calculated by max_augmenting_ffa: {max_flow_2.max_augmenting_ffa()}")

    ek1 = MaxFlow(flow_graph_1, 's', 't')
    ek2 = MaxFlow(flow_graph_2, 's', 't')
    print(f"graph_1's max flow and circulation counter calculated by EK: {ek1.ek()}")
    print(f"graph_2's max flow and circulation counter calculated by EK: {ek2.ek()}")