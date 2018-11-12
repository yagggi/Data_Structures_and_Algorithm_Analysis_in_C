

class Graph:
    def __init__(self, graph=None):
        """
        :param graph: example:
        {
            'a': ['b', 'c'],
            'b': ['a'],
            'c': ['a', 'd'],
            'd': ['c'],
            'e': [],
        }
        """
        self.graph = graph if graph else dict()

    @property
    def vertices(self):
        """
        :return: list of vertices
        """
        return list(self.graph.keys())

    @property
    def edges(self):
        res = []
        for k in self.graph:
            for d in self.graph[k]:
                if (k, d) not in res:
                    res.append((k, d))
        return res

    @property
    def neighbours(self):
        res = {vertex: set() for vertex in self.vertices}
        for start, end in self.edges:
            res[start].add(end)
        return res
