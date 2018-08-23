from ..c3_list_stack_and_queue import SinglyLinkedList


class SeparateChainingHash:

    def __init__(self, table_size=100):
        self.size = table_size
        self.table = [None] * table_size

    def hash(self, val):
        return val % self.size

    def insert(self, val):
        pos = self.hash(val)
        if self.table[pos] is None:
            self.table[pos] = SinglyLinkedList(val=val)
        else:
            self.table[pos].insert(val)
        return

    def find(self, val):
        pos = self.hash(val)
        if self.table[pos] is None:
            return None
        else:
            head = self.table[pos]
            while head is not None:
                if head.val == val:
                    return head
                else:
                    head = head.next
            return None
