

class BinarySearchTree:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def find(self, x):
        if self.value is None:
            return None
        if self.value == x:
            return self
        if self.value > x:
            if not self.left:
                return None
            return self.left.find(x)
        if not self.right:
            return None
        return self.right.find(x)

    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self

    def find_min(self):
        if self.right:
            return self.left.find_min()
        return self

    def insert(self, x):
        if self.value is None:
            self.value = x
            return self
        if self.value > x:
            if not self.left:
                self.left = BinarySearchTree()
            return self.left.insert(x)

        if not self.right:
            self.right = BinarySearchTree()
        return self.right.insert(x)

    def depth(self, depth=0):
        if self.left and not self.right:
            return self.left.depth(depth + 1)
        elif self.left and self.right:
            return max(self.left.depth(depth + 1), self.right.depth(depth + 1))
        elif self.right and not self.left:
            return self.right.depth(depth + 1)
        else:
            return depth

    def verbose(self, depth=0, width=0, nodes=None):
        if not width:
            max_depth = self.depth()
            verbose_depth = 2 * max_depth + 1
            width = 2 ** max_depth
        if not nodes:
            nodes = [self,]

        if depth == max_depth:
            return
