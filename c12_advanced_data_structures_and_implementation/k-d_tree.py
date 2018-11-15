

class KdNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class KdTree:
    def __inst__(self):
        self.root = KdNode([None, None])

    def recursive_insert(self, data, node, level):
        if node is None:
            node = KdNode(list(data))
        elif data[level] < node.data[level]:
            node.left = self.recursive_insert(data, node.left, ~level + 2)
        else:
            node.right = self.recursive_insert(data, node.right, ~level + 2)
        return node

    def insert(self, data):
        return self.recursive_insert(data, self.root, 0)

    def recursive_print_range(self, low, high, node, level):
        if node is not None:
            if low[0] <= node.data[0] <= high[0] and low[1] <= node.data[0] <= high[1]:
                print(node.data)
            if low[level] <= node.data[level]:
                self.recursive_print_range(low, high, node.left, ~level + 2)
            if high[level] >= node.data[level]:
                self.recursive_print_range(low, high, node.right, ~level + 2)

    def print_range(self, low, high):
        self.recursive_print_range(low, high, self.root, 0)
