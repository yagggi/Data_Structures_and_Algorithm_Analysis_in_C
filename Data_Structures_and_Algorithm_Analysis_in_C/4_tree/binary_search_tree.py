# coding: utf-8


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
            return self.left.find(x)
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
            return self.left.insert(x)
        return self.right.insert(x)
