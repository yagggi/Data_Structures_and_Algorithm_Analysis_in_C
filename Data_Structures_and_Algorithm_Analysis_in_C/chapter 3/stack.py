# coding: utf-8
from linked_list import SinglyLinkedList


class ListStack(SinglyLinkedList):

    @staticmethod
    def push(ele, stack):
        temp_cell = SinglyLinkedList(value=ele)
        temp_cell.next = stack.next
        stack.next = temp_cell

    @staticmethod
    def pop(stack):
        poped_cell = stack.next
        stack.next = poped_cell.next
        return poped_cell.value

    @staticmethod
    def top(stack):
        return stack.next.value


class ArrayStack(object):

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


if __name__ == "__main__":
    print '---ListStack---'
    s = ListStack()
    ListStack.push(1, s)
    ListStack.push(2, s)
    SinglyLinkedList.print_list(s)
    ListStack.pop(s)
    SinglyLinkedList.print_list(s)
    print ListStack.top(s)
    print '---ArrayStack---'
    s2 = ArrayStack()
    s2.push(1)
    s2.push(2)
    print s2.stack
    s2.pop()
    print s2.stack
    print s2.top()
