

class MinHeap:

    def __init__(self, cap=10):
        self.heap = {k: None for k in range(1, cap + 1)}
        self.cap = cap
        self.size = 0

    def insert(self, val):
        if self.size >= self.cap:
            raise Exception('This heap is FULL!')
        ind = self.size + 1
        while self.heap[ind // 2] > val and ind > 1:
            self.heap[ind], self.heap[ind // 2] = self.heap[ind // 2], self.heap[ind]
            ind = ind // 2
        self.heap[ind] = val
        self.size += 1

    def delete_min(self):
        if self.size <= 0:
            raise Exception('This heap is EMPTY!')
        min_ele = self.heap[1]
        last_ele = self.heap.pop(self.size)
        self.size -= 1
        ind = 1
        while ind * 2 < self.size:
            left_ind = ind * 2
            if left_ind + 1 < self.size and self.heap[left_ind + 1] < self.heap[left_ind]:
                next_ind = left_ind + 1
            else:
                next_ind = left_ind
            if last_ele > self.heap[next_ind]:
                self.heap[left_ind], self.heap[ind] = self.heap[ind], self.heap[left_ind]
                ind = next_ind
            else:
                break
        self.heap[ind] = last_ele
        return min_ele



