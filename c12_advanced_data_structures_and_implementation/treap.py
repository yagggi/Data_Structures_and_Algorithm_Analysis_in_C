import sys
sys.path.append('..')
from c10_algorithm_design_techniques.randomized_algorithms import random_gen


class TreapNode:
    def __init__(self, val, priority=float('inf'), left=None, right=None):
        self.val = val
        self.priority = priority
        self.left = left
        self.right = right


class Treap:
    def __init__(self):
        self.root = TreapNode(None)

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

    def insert(self, val: int, node=None):
        if node is None:
            node = TreapNode(val, random_gen())
        elif node.val is None:
            node.val = val
            node.priority = random_gen()
        elif val < node.val:
            node.left = self.insert(val, node.left)
            if node.left.priority < node.priority:
                node = self.left_single_rotate(node)
        elif val > node.val:
            node.right = self.insert(val, node.right)
            if node.right.priority < node.priority:
                node = self.right_single_rotate(node)
        return node

    def remove(self, val: int, node):
        while node:
            if val < node.val:
                node.left = self.remove(val, node.left)
            elif val > node.val:
                node.right = self.remove(val, node.right)
            else:
                if node.left.priority < node.right.priority:
                    node = self.left_single_rotate(node)
                else:
                    node = self.right_single_rotate(node)

                if node is not None:
                    node = self.remove(val, node)
                else:
                    node.left = None
        return node
