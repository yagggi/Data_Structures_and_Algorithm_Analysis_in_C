# coding: utf-8


class SingleLinkedList(object):

    def __init__(self, next_node=None, **kwargs):
        self.next = next_node
        for k, v in kwargs:
            setattr(self, k, v)

    def is_last(self):
        return self.next is None

    @staticmethod
    def find(ele, head):
        position = head.next
        while position is not None and position.value != ele:
            position = position.next
        return position

    @staticmethod
    def find_prev(ele, head):
        position = head
        while position.next is not None and position.next.value != ele:
            position = position.next
        return position

    @staticmethod
    def delete(ele, head):
        import gc

        prev_node = SingleLinkedList.find_prev(ele, head)
        temp_node = SingleLinkedList()
        temp_node = prev_node.next
        prev_node.next = temp_node.next
        del temp_node
        gc.collect()
        return

    @staticmethod
    def insert(ele, head, position):
        temp_node = SingleLinkedList()
        temp_node.next = position.next
        temp_node.value = ele
        position.next = temp_node
        return


class DoublyLinkedList(object):

    def __init__(self, next_node=None, prev_node=None, **kwargs):
        self.next = next_node
        self.prev = prev_node
        for k, v in kwargs:
            setattr(self, k, v)

    def is_last(self):
        return self.next is None

    @staticmethod
    def find(ele, head):
        position = head.next
        while position is not None and position.value != ele:
            position = position.next
        return position

    @staticmethod
    def delete(ele, head):
        import gc

        node = DoublyLinkedList.find(ele, head)
        prev_node = node.prev
        prev_node.next = node.next
        del node
        gc.collect()
        return

    @staticmethod
    def insert(ele, head, position):
        temp_node = DoublyLinkedList()
        temp_node.next = position
        temp_node.prev = position.prev
        temp_node.value = ele
        position.prev.next = temp_node
        return
