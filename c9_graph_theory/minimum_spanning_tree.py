from topology_sort import NonOrientedGraph
from shortest_path_problem import WeightedPath, inf, make_value
from collections import namedtuple

Edge = namedtuple('edge', 'weight,start,end')


def make_edge(weight, start, end):
    return Edge(weight, start, end)


class WeightedNonOrientedGraph(NonOrientedGraph):

    def __init__(self, graph, weights):
        super(WeightedNonOrientedGraph, self).__init__(graph)
        self.weights = dict(weights)

    def weight(self, start, end):
        return self.weights.get((start, end))


class EdgeHeap:

    def __init__(self, graph: WeightedNonOrientedGraph):
        self.heap = [None] * (len(graph.non_duplicated_edges) + 1)
        self.cap = len(graph.non_duplicated_edges) + 1
        self.size = 0
        for start, end in graph.non_duplicated_edges:
            self.insert(graph.weight(start, end), start, end)

    def insert(self, weight, start, end):
        if self.size >= self.cap:
            raise Exception('This heap is FULL!')
        if self.size == 0:
            self.heap[1] = make_edge(weight, start, end)
            self.size += 1
            return
        ind = self.size + 1
        while self.heap[ind // 2] is not None and self.heap[ind // 2].weight > weight:
            self.heap[ind] = self.heap[ind // 2]
            ind = ind // 2
        self.heap[ind] = make_edge(weight, start, end)
        self.size += 1

    def delete_min(self):
        if self.size <= 0:
            raise Exception('This heap is EMPTY!')
        min_ele = self.heap[1]
        self.heap[1] = None
        last_ele = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        ind = 1
        while ind * 2 < self.size:
            left_ind = ind * 2
            if left_ind != self.size and\
                    self.heap[left_ind + 1] is not None and\
                    self.heap[left_ind + 1].weight < self.heap[left_ind].weight:
                left_ind += 1
            if last_ele.weight > self.heap[left_ind].weight:
                self.heap[ind] = self.heap[left_ind]
                ind = left_ind
            else:
                break
        self.heap[ind] = last_ele
        return min_ele


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

    def __init_heap(self):
        self.heap = EdgeHeap(self.graph)

    def __init_unjoint_set(self):
        self.sets = {}
        for vertex in self.graph.vertices:
            self.sets[vertex] = [vertex]

    def find_unjoint_set(self, vertex):
        if vertex in self.sets:
            return vertex
        for v, eles in self.sets.items():
            if vertex in eles:
                return v

    def union_set(self, s1, s2):
        self.sets[s1].extend(self.sets.pop(s2))

    def kruskal(self):
        self.__init_heap()
        self.__init_unjoint_set()
        weights = 0
        tree = []
        while self.heap.size:
            edge = self.heap.delete_min()
            set1 = self.find_unjoint_set(edge.start)
            set2 = self.find_unjoint_set(edge.end)
            if set1 != set2:
                self.union_set(set1, set2)
                tree.append((edge.start, edge.end))
                weights += edge.weight
        return weights, tree


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

    graph = WeightedNonOrientedGraph(g, weights)
    tree = SpanningTree(graph)
    print(tree.kruskal())
