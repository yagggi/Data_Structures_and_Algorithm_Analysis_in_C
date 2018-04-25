# coding: utf-8


class Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.queue = []

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, ele):
        assert not self.is_full(), 'queue is full.'
        self.size += 1
        self.queue.insert(0, ele)

    def dequeue(self):
        assert not self.is_empty(), 'queue is empty.'
        return self.queue.pop()


if __name__ == "__main__":
    q = Queue(3)
    try:
        q.dequeue()
    except AssertionError as e:
        print(str(e))

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.queue)
    try:
        q.enqueue(4)
    except AssertionError as e:
        print(str(e))
