

class MaxHeapForSort:

    def __init__(self, elements=None):
        if not elements:
            raise Exception('Elements must not be empty!')
        self.cap = len(elements)
        self.heap = {k: None for k in range(1, self.cap + 1)}
        self.size = 0
        self.elements = elements

    def insert(self, val):
        if self.sieze >= self.cap:
            raise Exception('This heap is FULL!')
        ind = self.size + 1
        while self.heap[ind // 2] < val and ind > 1:
            self.heap[ind], self.heap[ind // 2] = self.heap[ind // 2], self.heap[ind]
            ind //= 2
        self.heap[ind] = val
        self.size += 1

    def delete_max(self):
        if self.size <= 0:
            raise Exception('This heap is EMPTY!')
        max_ele = self.heap[1]
        last_ele = self.heap.pop(self.size)
        self.heap[self.size] = max_ele
        self.size -= 1
        ind = 1
        while ind * 2 < self.size:
            left_ind = ind * 2
            if left_ind + 1 < self.size and self.heap[left_ind + 1] > self.heap[left_ind]:
                next_ind = left_ind + 1
            else:
                next_ind = left_ind
            if last_ele < self.heap[next_ind]:
                self.heap[left_ind], self.heap[ind] = self.heap[ind], self.heap[left_ind]
                ind = next_ind
            else:
                break
        self.heap[ind] = last_ele
        return max_ele

    def sort(self):
        for x in self.elements:
            self.insert(x)
        while True:
            try:
                self.delete_max()
            except Exception:
                break
        return list(self.heap.values())