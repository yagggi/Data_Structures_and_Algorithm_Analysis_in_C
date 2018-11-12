RED = 1
BLACK = 0


class RedBlackNode:
    def __init__(self, val, color=BLACK, left=None, right=None):
        self.val = val
        self.color = color
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.root = RedBlackNode(float('-inf'))
        self.root.left = self.root.right = RedBlackNode(None)

    def left_single_rotate(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        return left

    def right_single_rotate(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        return right

    def rotate(self, val: int, parent: RedBlackNode):
        if val < parent.val:
            if val < parent.left.val:
                parent.left = self.left_single_rotate(parent.left)
            else:
                parent.left = self.right_single_rotate(parent.right)
            return parent.left
        else:
            if val < parent.right:
                parent.right = self.left_single_rotate(parent.right)
            else:
                parent.right = self.right_single_rotate(parent.right)
            return parent.right

    def reorient(self, val: int, node: RedBlackNode, par: RedBlackNode,
                 g_par: RedBlackNode, gg_par: RedBlackNode):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK
        if par.color == RED:
            g_par.color = RED
            if (val < g_par.val) != (val < par.val):
                self.rotate(val, g_par)
            node = self.rotate(val, gg_par)
            node.color = BLACK
        self.root.right.color = BLACK

    def insert(self, val: int):
        node = par = g_par = gg_par = self.root
        while node.val != val:
            gg_par = g_par
            g_par = par
            par = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
            if node.left.color == RED and node.right.color == RED:
                self.reorient(val, node, par, g_par, gg_par)

        if node and node.val is not None:
            return None
        node = RedBlackNode(val, color=RED)
        node.left = node.right = None
        if val < par.val:
            par.left = node
        else:
            par.right = node
        self.reorient(val, node, par, g_par, gg_par)
        return self
