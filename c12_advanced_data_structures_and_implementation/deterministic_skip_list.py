

class SkipNode:
    def __init__(self, val, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down


class SkipList:
    def __init__(self):
        self.bottom = SkipNode(None)
        self.bottom.down = self.bottom
        self.bottom.right = self.bottom
        self.tail = SkipNode(float('inf'))
        self.tail.right = self.tail
        self.tail.down = self.bottom
        self.head = SkipNode(float('-inf'))
        self.head.right = self.tail
        self.head.down = self.bottom

    def find(self, val: int):
        cur_pos = self.head
        while cur_pos.val != val:
            if val < cur_pos.val:
                cur_pos = cur_pos.down
            else:
                cur_pos = cur_pos.right
            if cur_pos == self.bottom:
                break
        return cur_pos

    def insert(self, val: int):
        self.bottom.val = val
        cur_pos = self.head
        while cur_pos != self.bottom:
            while val > cur_pos.val:
                cur_pos = cur_pos.right

            if cur_pos.val > cur_pos.down.right.right.val:
                new_node = SkipNode(val)
                new_node.right = cur_pos.right
                new_node.down = cur_pos.down.right.right
                cur_pos.right = new_node
                new_node.val = cur_pos.val
                cur_pos.val = cur_pos.down.right.val
            else:
                cur_pos = cur_pos.down

        if self.head.right != self.tail:
            new_node = SkipNode(float('-inf'))
            new_node.down = self.head
            new_node.right = self.tail
            new_node.val = float('-inf')
            self.head = new_node
        return
