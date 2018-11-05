

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

    def verbose(self, stack=None):
        def add_to_stack(node, res):
            if node.left:
                res.append(node.left)
            if node.right:
                res.append(node.right)
            return res

        if stack is None:
            print(self.value)
            stack = add_to_stack(self, [])
            self.verbose(stack)
        else:
            print(' '.join([str(x.value) for x in stack]))
            new_stack = []
            for node in stack:
                new_stack = add_to_stack(node, new_stack)
            if new_stack:
                self.verbose(new_stack)

    def delete(self, ele, pre=None, side=None):
        if ele > self.value:
            self.right.delete(ele, pre=self, side='right')
            return self
        elif ele < self.value:
            self.left.delete(ele, pre=self, side='left')
            return self
        elif self.right and self.left:
            tmp = self.right.find_min()
            self.value = tmp.value
            self.right.delete(self.value, pre=self, side='right')
            return self
        elif self.right is None:
            if not pre:
                return self.left
            setattr(pre, side, self.left)
            return pre
        elif self.left is None:
            if not pre:
                return self.right
            setattr(pre, side, self.right)
            return pre


