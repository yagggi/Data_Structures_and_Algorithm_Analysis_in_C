RED = 1
BLACK = 0


class RedBlackNode:
    def __init__(self, val, color=BLACK, left=None, right=None):
        self.val = val
        self.color = color
        self.left = left
        self.right = right

    def min_child(self):
        node = self
        while node.left:
            node = node.left
        return node

    def max_child(self):
        node = self
        while node.right:
            node = node.right
        return node

    def replace_by(self, node):
        self.val = node.val
        self.color = node.color
        self.left = node.left
        self.right = node.right

    def has_2_black_children(self):
        if self.left and self.left.color == RED:
            return False
        if self.right and self.right.color == RED:
            return False
        return True


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

    def left_double_rotate(self, node):
        node.left = self.right_single_rotate(node.left)
        return self.left_single_rotate(node)

    def right_double_rotate(self, node):
        node.right = self.left_single_rotate(node.right)
        return self.right_single_rotate(node)

    def sibling_rotate(self, val, par):
        if val < par.val:
            sibling = par.right
            if sibling.right.color == RED:
                new_par = self.right_single_rotate(par)
                new_par.color = RED
                par = new_par.left
                par.color = BLACK
                node = par.left
                node.color = RED
            else:
                new_par = self.right_double_rotate(par)
                par = new_par.left
                par.color = BLACK
                node = par.left
                node.color = RED
        else:
            sibling = par.left
            if sibling.left.colort == RED:
                new_par = self.left_single_rotate(par)
                new_par.color = RED
                par = new_par.right
                par.color = BLACK
                node = par.right
                node.color = RED
            else:
                new_par = self.left_double_rotate(par)
                par = new_par.right
                par.color = BLACK
                node = par.right
                node.color = RED
        return node, par

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
        if node.left:
            node.left.color = BLACK
        if node.right:
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

    def delete(self, val: int):
        node = self.root
        sibling = par = node
        while node and (node.val != val):
            if (node.left and node.left.color == RED) or\
                    (node.right and node.right.color == RED):
                if val > node.val:
                    par = node
                    node = par.right
                    sibling = par.left
                    method = self.left_single_rotate
                    next_sibling = 'left'
                else:
                    par = node
                    node = par.left
                    sibling = par.right
                    method = self.right_single_rotate
                    next_sibling = 'right'
                if node.color == RED:
                    continue
                par = method(par)
                sibling = getattr(par, next_sibling)

            if sibling.has_2_black_children():
                node.color = RED
                sibling.color = RED
                par.color = BLACK
            else:
                node, par = self.sibling_rotate(val, par)

            par = node
            if val > node.val:
                node = node.right
                sibling = node.left
            else:
                node = node.left
                sibling = node.right

        if node.right:
            min_right = node.right.min_child()
            node.replace_by(min_right)
        elif node.left:
            max_left = node.left.max_child()
            node.replace_by(max_left)
        elif val > par.val:
            par.right = None
        elif val < par.val:
            par.left = None
