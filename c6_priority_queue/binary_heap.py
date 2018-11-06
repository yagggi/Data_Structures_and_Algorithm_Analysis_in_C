

class MinHeap:

    def __init__(self, cap=10):
        self.heap = [None] * (cap + 1)
        self.cap = cap
        self.size = 0

    def insert(self, val):
        if self.size >= self.cap:
            raise Exception('This heap is FULL!')
        if self.size == 0:
            self.heap[1] = val
            self.size += 1
            return
        ind = self.size + 1
        while self.heap[ind // 2] is not None and self.heap[ind // 2] > val:
            self.heap[ind] = self.heap[ind // 2]
            ind = ind // 2
        self.heap[ind] = val
        self.size += 1

    def delete_min(self):
        if self.size <= 0:
            raise Exception('This heap is EMPTY!')
        min_ele = self.heap[1].val
        self.heap[1] = None
        last_ele = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1
        ind = 1
        while ind * 2 < self.size:
            left_ind = ind * 2
            if left_ind != self.size and\
                    self.heap[left_ind + 1] is not None and\
                    self.heap[left_ind + 1] < self.heap[left_ind]:
                left_ind += 1
            if last_ele > self.heap[left_ind]:
                self.heap[ind] = self.heap[left_ind]
                ind = left_ind
            else:
                break
        self.heap[ind] = last_ele
        return min_ele
