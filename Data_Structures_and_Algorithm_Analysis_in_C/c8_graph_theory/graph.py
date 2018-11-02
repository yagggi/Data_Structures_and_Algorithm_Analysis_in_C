

class NonOrientedGraph:
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

    def vertices(self):
        return list(self.graph.keys())

    def edges(self):
        res = []
        for k in self.graph:
            for d in self.graph[k]:
                if {k, d} not in res:
                    res.append({k, d})
        return res


class OrientedGraph(NonOrientedGraph):

    def edges(self):
        res = []
        for k in self.graph:
            for d in self.graph[k]:
                if (k, d) not in res:
                    res.append((k, d))
        return res
