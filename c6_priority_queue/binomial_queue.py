

class BinomialNode:
    def __init__(self, val, left_child=None, next_sibling=None):
        self.val = val
        self.left_child = left_child
        self.next_sibling = next_sibling


class BinomialQueue:
    def __init__(self, queue=None):
        self.__current_size = 0
        self.queue = queue if queue else {}

    @property
    def size(self):
        return self.__current_size

    @size.setter
    def size(self, val):
        self.__current_size = val

    @staticmethod
    def combine(t1: BinomialNode, t2: BinomialNode) -> BinomialNode:
        if t1.val > t2.val:
            return BinomialQueue.combine(t2, t1)
        t2.next_sibling = t1.left_child
        t1.left_child = t2
        return t1

    @staticmethod
    def merge(q1: 'BinomialQueue', q2: 'BinomialQueue') -> 'BinomialQueue':
        q1.size += q2.size
        carry = None
        i, j = 0, 1
        while j <= q1.size:
            j *= 2
            t1 = q1[i]
            t2 = q2[i]
            if not t1 and not t2 and not carry:
                continue
            elif t1 and not t2 and not carry:
                continue
            elif t2 and not t1 and not carry:
                q1.queue[i] = t2
                q2.queue[i] = None
            elif carry and not t1 and not t2:
                q1.queue[i] = carry
            elif t1 and t2 and not carry:
                carry = BinomialQueue.combine(t1, t2)
                q1.queue[i] = q2.queue[i] = None
            elif t1 and carry and not t2:
                carry = BinomialQueue.combine(t1, carry)
                q1.queue[i] = q2.queue[i] = None
            elif t2 and carry and not t1:
                carry = BinomialQueue.combine(t2, carry)
                q1.queue[i] = q2.queue[i] = None
            else:
                q1.queue[i] = carry
                carry = BinomialQueue.combine(t1, t2)
                q2.queue[i] = None
        return q1

    @staticmethod
    def insert(q: 'BinomialQueue', t: BinomialNode) -> 'BinomialQueue':
        q2 = BinomialQueue(queue={0: t})
        q2.size = 1
        return BinomialQueue.merge(q, q2)

    @staticmethod
    def delete_min(q: 'BinomialQueue') -> int:
        min_val = float('inf')
        min_node = min_i = None
        for i in q.queue:
            if q.queue[i].val < min_val:
                min_node = q.queue[i]
                min_i = i
                min_val = min_node.val
        deleted_val = min_node.val
        deleted_tree = q.queue[min_i].left_child
        deleted_queue = BinomialQueue()
        deleted_queue.size = (min_i << 2) - 1
        for j in range(min_i - 1, -1, -1):
            deleted_queue.queue[j] = deleted_tree
            deleted_tree = deleted_tree.next_sibling
            deleted_queue[j].next_sibling = None
        q.queue[min_i] = None
        q.size -= deleted_queue.size + 1
        BinomialQueue.merge(q, deleted_queue)
        return deleted_val
