from .red_black_tree import RedBlackTree


class AANode:
    def __init__(self, val, level=0, left=None, right=None):
        self.val = val
        self.level = level
        self.left = left
        self.right = right


class AATree(RedBlackTree):
    def __init__(self):
        self.root = AANode(None)

    def skew(self, node):
        if node.left.level == node.level:
            node = self.left_single_rotate(node)
        return node

    def split(self, node):
        if node.level == node.right.right.level:
            node = self.right_single_rotate(node)
            node.level += 1
        return node

    def insert(self, val: int, node=None):
        if node is None:
            node = AANode(val, level=1)
            return node
        elif node.val is None:
            node = self.root
            node.val = val
            node.level = 1
            return node
        elif val < node.val:
            node.left = self.insert(val, node.left)
        elif val > node.val:
            node.right = self.insert(val, node.right)
        node = self.skew(node)
        node = self.split(node)
        return node
