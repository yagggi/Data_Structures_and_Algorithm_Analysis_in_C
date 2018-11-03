

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
        self._indegree_dic = {}
        self._zero_indegree_list = []
        self.__init_indegree()
    
    def __init_indegree(self):
        for vertex in self.vertices():
            self._indegree_dic[vertex] = len(self.graph[vertex])

    def vertices(self):
        """
        :return: list of vertices 
        """
        return list(self.graph.keys())

    def edges(self):
        """
        :return: list of edges
        """
        res = []
        for k in self.graph:
            for d in self.graph[k]:
                if {k, d} not in res:
                    res.append({k, d})
        return res


class OrientedGraph(NonOrientedGraph):

    def __init__(self, graph=None):
        """
        :param graph: example:
        {
            'a': ('b', 'c'),
            'b': ('a'),
            'c': ('a', 'd'),
            'd': ('c'),
            'e': (,),
        }
        """
        self.graph = graph if graph else dict()
        self._indegree_dic = {}
        self._zero_indegree_list = []
        self.__init_indegree()

    def edges(self):
        res = []
        for k in self.graph:
            for d in self.graph[k]:
                if (k, d) not in res:
                    res.append((k, d))
        return res

    def __init_indegree(self):
        for pre_vertex, vertex in self.edges():
            if self._indegree_dic.get(pre_vertex) is None:
                self._indegree_dic[pre_vertex] = 0
            if self._indegree_dic.get(vertex):
                self._indegree_dic[vertex] += 1
            else:
                self._indegree_dic[vertex] = 1

    def __find_zero_indegree_vertices(self):
        res = []
        for vertex, indegree in self._indegree_dic.items():
            if indegree == 0:
                res.append(vertex)
        return res

    def topsort(self):
        """
        Topology Sort
        :return: list(set())
        """
        res = []
        cnt = 0
        total = len(self.vertices())
        zero_indegree_verteces = self.__find_zero_indegree_vertices()
        while zero_indegree_verteces:
            V = zero_indegree_verteces.pop()
            for vertex in self.graph[V]:
                self._indegree_dic[vertex] -= 1
                if self._indegree_dic[vertex] == 0:
                    zero_indegree_verteces.append(vertex)
            self.graph.pop(V)
            self._indegree_dic.pop(V)
            res.append(V)
            cnt += 1
        if cnt != total:
            return 'Graph has circle.'
        return res


if __name__ == '__main__':
    g1 = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['d'],
        'd': ['e'],
        'e': [],
    }
    g2 = {
        'a': ['b', 'c'],
        'b': ['d'],
        'c': ['a', 'd'],
        'd': ['a'],
        'e': [],
    }
    g1_class = OrientedGraph(g1)
    print(f'g1:{g1}\ng1 topsort: {g1_class.topsort()}')
    g2_class = OrientedGraph(g2)
    print(f'g2:{g2}\ng2 topsort: {g2_class.topsort()}')
