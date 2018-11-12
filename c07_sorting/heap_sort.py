

class MaxHeapForSort:

    def __init__(self, elements=None):
        if not elements:
            raise Exception('Elements must not be empty!')
        self.cap = len(elements)
        self.heap = [None] * (self.cap + 1)
        self.size = 0
        self.elements = elements

    def insert(self, val):
        if self.size >= self.cap:
            raise Exception('This heap is FULL!')
        if self.size == 0:
            self.heap[1] = val
            self.size += 1
            return
        ind = self.size + 1
        while self.heap[ind // 2] is not None and self.heap[ind // 2] < val:
            self.heap[ind] = self.heap[ind // 2]
            ind = ind // 2
        self.heap[ind] = val
        self.size += 1

    def delete_max(self):
        if self.size <= 0:
            raise Exception('This heap is EMPTY!')
        max_ele = self.heap[1]
        last_ele = self.heap[self.size]
        self.heap[1] = None
        self.heap[self.size] = max_ele
        self.size -= 1
        ind = 1
        while ind * 2 < self.size:
            left_ind = ind * 2
            if left_ind != self.size and\
                    self.heap[left_ind + 1] is not None and\
                    self.heap[left_ind + 1] > self.heap[left_ind]:
                left_ind += 1
            if last_ele < self.heap[left_ind]:
                self.heap[ind] = self.heap[left_ind]
                ind = left_ind
            else:
                break
        self.heap[ind] = last_ele
        return max_ele

    def sort(self):
        for x in self.elements:
            self.insert(x)
        while self.size > 0:
            self.delete_max()
        return self.heap[1:]


if __name__ == "__main__":
    s = MaxHeapForSort([int(x) for x in input('Enter elements seperated by single space:\n').split()])
    print(s.sort())
