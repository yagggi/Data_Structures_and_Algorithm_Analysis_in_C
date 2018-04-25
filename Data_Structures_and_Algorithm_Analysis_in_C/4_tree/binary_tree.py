# coding: utf-8


class ArrayStack:

    def __init__(self):
        self.stack = []
        self.top_index = -1

    def push(self, ele):
        self.stack.append(ele)
        self.top_index += 1

    def pop(self):
        self.top_index -= 1
        return self.stack.pop()

    def top(self):
        return self.stack[self.top_index]

    def is_empty(self):
        return self.stack == []


class BinaryTree:

    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

    @staticmethod
    def build(*args):
        stack = ArrayStack()
        for ele in args:
            if ele in ['*', '+', '-', '/']:
                right = stack.pop()
                left = stack.pop()
                new_node = BinaryTree(left=left, right=right, value=ele)
                stack.push(new_node)
            else:
                stack.push(BinaryTree(value=ele))
        return stack.pop()

    def print_expression(self, node=None):
        if not node:
            node = self
        if node.left.value not in ['*', '+', '-', '/']:
            left = node.left.value
        else:
            left = self.print_expression(node.left)
        if node.right.value not in ['*', '+', '-', '/']:
            right = node.right.value
        else:
            right = self.print_expression(node.right)
        return '({} {} {})'.format(left, node.value, right)


if __name__ == '__main__':
    exp = 'a b + c d e + * *'
    node = BinaryTree.build(*exp.split(' '))
    print(node.print_expression())
