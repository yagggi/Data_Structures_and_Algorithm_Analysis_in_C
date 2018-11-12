import sys
import copy
sys.path.append("..")
from c04_tree.splay_tree import SplayTree


class TopDownSplayNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


class TopDownSplayTree(SplayTree):
    def __init__(self, left=None, right=None):
        self.left_max = left
        self.right_min = right

    @staticmethod
    def splay(val: int, node: TopDownSplayNode):
        right_min = TopDownSplayNode(None)
        left_max = TopDownSplayNode(None)
        header = TopDownSplayNode(None)
        header.left = left_max
        header.right = right_min
        while val != node.value:
            if val < node.value:
                if node.left and val < node.left.value:
                    node = TopDownSplayTree.left_single_rotate(node)
                if node.left is None:
                    break
                right_min.left = copy.deepcopy(node)
                right_min = right_min.left
                right_min.left = None
                node = node.left
            else:
                if node.right and val > node.right:
                    node = TopDownSplayTree.right_single_rotate(node)
                if node.right is None:
                    break
                left_max.right = copy.deepcopy(node)
                left_max = left_max.right
                left_max.right = None
                node = node.right
        left_max.right = node.left
        right_min.left = node.right
        node.left = header.left
        node.right = header.right
        return node

    @staticmethod
    def insert(val: int, node: TopDownSplayNode):
        new_node = TopDownSplayNode(val)
        if node is None:
            node = new_node
        else:
            node = TopDownSplayTree.splay(val, node)
            if val < node.val:
                new_node.left = node.left
                new_node.right = node
                node.left = None
                node = new_node
            elif val > node.val:
                new_node.right = node.right
                new_node.left = node
                node.right = None
                node = new_node
            else:
                pass
        return node

    @staticmethod
    def delete(val: int, node: TopDownSplayNode):
        if node:
            node = TopDownSplayTree.splay(val, node)
            if node.value == val:
                if node.left is None:
                    new_node = node.right
                else:
                    new_node = node.left
                    new_node = TopDownSplayTree.splay(val, new_node)
                    new_node.right = node.right
                node = new_node
        return node
