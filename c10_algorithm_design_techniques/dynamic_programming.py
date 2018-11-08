from c9_graph_theory.shortest_path_problem import WeightedGraph
inf = float('inf')


def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def better_fib(n):
    if n <= 1:
        return 1
    last = pre_last = 1
    for i in range(2, n + 1):
        answer = last + pre_last
        pre_last, last = last, answer
    return answer


def eval(n):
    if n == 0:
        return 1.0
    else:
        sum = 0
        for i in range(0, n):
            sum += eval(i)
        return 2.0 * sum / n + n


def better_eval(n):
    c = [0] * (n + 1)
    c[0] = 1.0
    for i in range(1, n + 1):
        sum = 0
        for j in range(0, i):
            sum += c[j]
        c[i] = 2.0 * sum / i + i
    answer = c[n]
    del c
    return answer


def even_better_eval(n):
    c = [0] * (n + 1)
    answer = c[0] = 1.0
    for i in range(1, n + 1):
        pre = c[i - 1]
        answer = 2.0 * pre / i + i
        c[i] = pre + answer
    del c
    return answer


class OptimalBuild:

    def __init__(self, freq_dic):
        self.freq_dic = freq_dic
        self.words = sorted(list(freq_dic.items()), key=lambda x: x[0])
        self.table = {}

    def __cal_cost(self, words, left, right, cost):
        total = 0
        if left > right:
            return 0
        for ind in range(left, right + 1):
            if ind > len(words) - 1:
                break
            total += words[ind][1] * cost

    def optimal_cost(self):
        """
        :return:
        """
        words = self.words
        length = len(words)
        for width in range(1, length + 1):
            for left in range(0, length - width):
                min_perc = inf
                mid = None
                right = left + width + 1
                sub_word = words[left: right]
                total_p = sum([x[1] for x in sub_word])
                for center_ind in range(left, right):
                    left_perc = self.__cal_perc(left, center_ind)
                    right_perc = self.__cal_perc(center_ind + 1, right)
                    perc = left_perc + right_perc + total_p
                    if perc < min_perc:
                        min_perc = perc
                        mid = self.words[center_ind][0]
                self.table[(left, right)] = dict(
                    perc=round(min_perc, 2),
                    center=mid,
                    sub_word=sub_word
                )
        return self.table

    def __cal_perc(self, left, right):
        if left >= right:
            return 0
        if right - left == 1:
            return self.words[left][1]
        return self.table[(left, right)]['perc']


class DynamicPath:
    def __init__(self, graph: WeightedGraph):
        self.graph = graph
        self.vertices = list(graph.vertices)
        self.number = len(self.vertices)
        self.table = [[None] * self.number] * self.number
        self.shortest_table = [[None] * self.number] * self.number

    def shortest_pairs(self, start, end):
        for i in range(self.number):
            for j in range(self.number):
                self.shortest_table[i][j] = self.graph.distance(i, j)
        for k in range(self.number):
            for i in range(self.number):
                for j in range(self.number):
                    l = self.shortest_table[i][k] + self.shrotest_table[k][j]
                    if l < self.shortest_table[i][j]:
                        self.shortest_table[i][j] = l
                        self.table[i][k] = k
        return self.shortest_table[start][end]


if __name__ == '__main__':
    freq_dic = {
        'a': 0.22,
        'am': 0.18,
        'and': 0.20,
        'egg': 0.05,
        'if': 0.25,
        'the': 0.02,
        'two': 0.08
    }
    p = OptimalBuild(freq_dic)
    res = p.optimal_cost()[(0, len(freq_dic))]
    print(res['perc'], res['center'])
