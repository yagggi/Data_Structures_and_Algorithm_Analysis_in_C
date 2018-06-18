

class AVLTree:

    def __init__(self, value=None, right=None, left=None, hight=-1):
        self.value = value
        self.right = right
        self.left = left
        self.hight = hight

    @staticmethod
    def hight(node):
        if node is None:
            return -1
        else:
            return node.hight

    @staticmethod
    def up(node, hight):
        if node is None:
            return
        node.hight += 1
        AVLTree.up(node.left, hight)
        AVLTree.up(node.right, hight)
        return

    @staticmethod
    def left_single_rotate(node):
        left = node.left
        left.right = node
        left.hight -= 1
        AVLTree.up(left.left, -1)
        AVLTree.up(left.right, 1)
        return left

    @staticmethod
    def right_single_rotate(node):
        right = node.right
        right.left = node
        right.hight -= 1
        AVLTree.up(right.right, -1)
        AVLTree.up(right.left, 1)
        return right

    @staticmethod
    def left_double_rotate(node):
        node.left = AVLTree.right_single_rotate(node.left)
        return AVLTree.left_single_rotate(node)

    @staticmethod
    def right_double_rotate(node):
        node.right = AVLTree.left_single_rotate(node.right)
        return AVLTree.right_single_rotate(node)

    @staticmethod
    def insert(node, x):
        if node is None:
            node = AVLTree(hight=0, value=x)
        elif node.value > x:
            node.left = AVLTree.insert(node.left, x)
            if AVLTree.hight(node.left) - AVLTree.hight(node.right) == 2:
                if x < node.left.value:
                    node = AVLTree.left_single_rotate(node)
                else:
                    node = AVLTree.left_double_rotate(node)
        elif node.value < x:
            node.right = AVLTree.insert(node.right, x)
            if AVLTree.hight(node.right) - AVLTree.hight(node.left) == 2:
                if x > node.right.value:
                    node = AVLTree.right_single_rotate(node)
                else:
                    node = AVLTree.right_double_rotate(node)
        return node
