from .binary_search_tree import BinarySearchTree


class SplayTree(BinarySearchTree):

    @staticmethod
    def find(node, x, nodes=[]):
        if not node:
            return None
        elif node.value == x:
            node = SplayTree.rotate(node, nodes)
            return node
        elif node.value > x:
            nodes.append(node)
            return SplayTree.find(node.left, x, nodes)
        elif node.value < x:
            nodes.append(node)
            return SplayTree.find(node.right, x, nodes)

    @staticmethod
    def rotate(node, nodes):
        while nodes:
            k2 = nodes.pop()
            if k2.value > node.value:
                if not nodes:
                    SplayTree.left_single_rotate(k2)
                else:
                    k3 = nodes[-1]
                    if k3.value > k2.value:
                        SplayTree.left_single_rotate(k2)
                    else:
                        k3 = nodes.pop()
                        SplayTree.right_double_rotate(k3)
            else:
                if not nodes:
                    SplayTree.right_single_rotate(k2)
                else:
                    k3 = nodes[-1]
                    if k3.value > k2.value:
                        k3 = nodes.pop()
                        SplayTree.left_double_rotate(k3)
                    else:
                        SplayTree.right_single_rotate(k2)
        return node

    @staticmethod
    def left_single_rotate(node):
        left = node.left
        left.right = node
        return left

    @staticmethod
    def right_single_rotate(node):
        right = node.right
        right.left = node
        return right

    @staticmethod
    def left_double_rotate(node):
        node.left = SplayTree.right_single_rotate(node.left)
        return SplayTree.left_single_rotate(node)

    @staticmethod
    def right_double_rotate(node):
        node.right = SplayTree.left_single_rotate(node.right)
        return SplayTree.right_single_rotate(node)

    @staticmethod
    def find_max(node, nodes=[]):
        if not node.right:
            node = SplayTree.rotate(node, nodes)
            return node
        else:
            nodes.append(node)
            node = node.right
            return SplayTree.find_max(node, nodes)

    @staticmethod
    def delete(root, x):
        node = SplayTree.find(root, x)
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            left_max = SplayTree.find_max(root)
            left_max.right = node.right
            return left_max
