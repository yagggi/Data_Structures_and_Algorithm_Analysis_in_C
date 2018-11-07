from topology_sort import NonOrientedGraph


class DepthFirstSearchTree:

    def __init__(self, graph: NonOrientedGraph):
        self.graph = graph
        self.known = {}
        self.counter = 0
        for vertex in self.graph.vertices:
            self.known[vertex] = False
        self.low = {}
        self.num = {}
        self.parent = {}
        self.arti_point = set()

    def dfs(self, vertex=None):
        self.counter += 1
        if not vertex:
            vertex = 'c'
        self.num[vertex] = self.counter
        self.known[vertex] = True
        for v in self.graph.neighbours[vertex]:
            if not self.known[v]:
                self.parent[v] = vertex
                self.dfs(v)
        return self.num

    def find_low(self, vertex=None):
        if not vertex:
            vertex = 'c'
        self.low[vertex] = self.num[vertex]
        for v in self.graph.neighbours[vertex]:
            if self.num[v] > self.num[vertex]:
                self.find_low(v)
                if self.low[v] >= self.num[vertex]:
                    self.arti_point.add(vertex)
                self.low[vertex] = min(self.low[vertex], self.low[v])
            elif self.parent[vertex] != v:
                self.low[vertex] = min(self.low[vertex], self.num[v])
        return self.arti_point

    def dfs_and_find_low(self, vertex=None):
        if not vertex:
            vertex = 'c'
        self.counter += 1
        self.known[vertex] = True
        self.low[vertex] = self.num[vertex] = self.counter
        for v in self.graph.neighbours[vertex]:
            if not self.known[v]:
                self.parent[v] = vertex
                self.dfs_and_find_low(v)
                if self.low[v] >= self.num[vertex]:
                    self.arti_point.add(vertex)
                self.low[vertex] = min(self.low[vertex], self.low[v])
            elif self.parent.get(vertex) != v:
                self.low[vertex] = min(self.low[vertex], self.num[v])
        return self.arti_point


if __name__ == '__main__':
    g = {
        'a': ['b', 'd'],
        'b': ['a', 'c'],
        'c': ['b', 'd', 'g'],
        'g': ['c'],
        'd': ['c', 'a', 'e', 'f'],
        'e': ['d', 'f'],
        'f': ['d', 'e']
    }
    graph = NonOrientedGraph(g)
    dfst = DepthFirstSearchTree(graph)
    print(dfst.dfs())
    print(dfst.find_low())
    dfst = DepthFirstSearchTree(graph)
    print(dfst.dfs_and_find_low())
