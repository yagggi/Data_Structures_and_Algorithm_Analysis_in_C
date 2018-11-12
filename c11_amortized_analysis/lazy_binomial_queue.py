import sys
sys.path.append("..")
from c06_priority_queue.binomial_queue import BinomialQueue


class LazyBinomialQueue(BinomialQueue):

    @staticmethod
    def lazy_merge(q1: 'LazyBinomialQueue', q2: 'LazyBinomialQueue') -> 'LazyBinomialQueue':
        q1.size += q2.size
        q1.queue += q2.queue
        q2.queue = None
        return q1

    @staticmethod
    def lazy_delete_min(q: 'LazyBinomialQueue') -> int:
        from collections import defaultdict
        import math

        table = defaultdict(list)
        for i in range(int(math.log(q.size, 2)) + 1):
            table[i] = []
        min_val = float('inf')
        min_node = min_i = None
        for i, ele in enumerate(q.queue):
            if q.queue[i].val < min_val:
                min_node = ele
                min_i = i
                min_val = min_node.val
        deleted_val = min_node.val
        deleted_tree = q.queue[min_i].left_child
        for j in range(min_i - 1, -1, -1):
            table[j].append(deleted_tree)
            deleted_tree = deleted_tree.next_sibling

        for ind, node in enumerate(q.queue):
            if node:
                table[ind].append(node)
        for k in table:
            while len(table[k]) > 1:
                n1 = table[k].pop()
                n2 = table[k].pop()
                table[k + 1].append(LazyBinomialQueue.combine(n1, n2))
        new_queue = []
        for k in table:
            if table[k]:
                new_queue.extend(table[k])
            else:
                new_queue.append(None)
        q.size -= 1
        q.queue = new_queue
        return deleted_val
