from ..c4_tree import BinaryTree


class LeftistHeap(BinaryTree):

    def __init__(self, npl=0,  **kwargs):
        self.npl = npl
        super.__init__(**kwargs)

    @staticmethod
    def merge(h1: 'LeftistHeap', h2: 'LeftistHeap') -> 'LeftistHeap':
        if h1 is None:
            return h2
        elif h2 is None:
            return h1
        elif h1.value < h2.value:
            return LeftistHeap.real_merge(h1, h2)
        else:
            return LeftistHeap.real_merge(h2, h1)

    @staticmethod
    def real_merge(h1: 'LeftistHeap', h2: 'LeftistHeap') -> 'LeftistHeap':
        if h1.left is None:
            h1.left = h2
        else:
            h1.right = LeftistHeap.merge(h1.right, h2)
            if h1.left.npl < h1.right.npl:
                h1.left, h1.right = h1.right, h1.left
            h1.npl = h1.right.npl + 1
        return h1
