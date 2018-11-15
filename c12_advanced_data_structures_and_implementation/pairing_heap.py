

class PairingNode:
    def __init__(self, val, left_child=None, next_sibling=None, prev=None):
        self.val = val
        self.left_child = left_child
        self.next_sibling = next_sibling
        self.prev = prev


class PairingHeap:
    def __init__(self):
        self.root = PairingNode(None)

    def compare_and_link(self, node1, node2):
        if node2 is None:
            return node1
        elif node1.val <= node2.val:
            node2.prev = node1
            node1.next_sibling = node2.next_sibling
            if node1.next_sibling is not None:
                node1.next_sibling.prev = node1
            node2.next_sibling = node1.left_child
            if node2.next_sibling is not None:
                node2.next_sibling.prev = node2
            node1.left_child = node2
            return node1
        else:
            node1.prev = node2
            node1.next_sibling = node2.left_child
            if node1.next_sibling is not None:
                node1.next_sibling.prev = node1
            node2.left_child = node1
            return node2

    def insert(self, val, node: PairingNode):
        new_node = PairingNode(val)
        if node is None:
            return new_node
        else:
            return self.compare_and_link(new_node, node)

    def decrease_key(self, delta: int, node: PairingNode):
        if delta < 0:
            raise Exception('decrease_key method called with negative delta')
        node.val -= delta
        if node == self.root:
            return self.root
        if node.next_sibling is not None:
            node.next_sibling.prev = node.prev
        if node.prev.left_child == node:
            node.prev.left_child = node.next_sibling
        else:
            node.prev.next_sibling = node.next_sibling
        node.next_sibling = None
        return self.compare_and_link(node, self.root)

    def delete_min(self):
        if self.root is None or self.root.val is None:
            raise Exception('Pairing heap is empty!')
        else:
            min_val = self.root.val
            new_root = PairingNode(None)
            if self.root.left_child is not None:
                new_root = self.combine_sibling(self.root.left_child)
            return min_val, new_root

    def combine_siblings(self, node):
        if node.next_sibling is None:
            return node

        node_list = []
        while node is not None:
            node_list.append(node)
            node.prev.next_sibling = None
            node = node.next_sibling
        node_list.append(None)
        cnt = len(node_list) - 1
        i = 0
        for i in range(0, cnt - 1, 2):
            node_list[i] = self.compare_and_link(node_list[i],
                                                 node_list[i + 1])

        j = i - 2
        if j == cnt - 3:
            node_list[j - 2] = self.compare_and_link(node_list[j],
                                                     node_list[j + 2])
        while j >= 2:
            node_list[j - 2] = self.compare_and_link(node_list[j - 2],
                                                     node_list[j])
            j -= 2
        return node_list[0]