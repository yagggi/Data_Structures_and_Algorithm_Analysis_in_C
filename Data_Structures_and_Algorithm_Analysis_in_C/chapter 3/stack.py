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


if __name__ == "__main__":
    s = ListStack()
    ListStack.push(1, s)
    ListStack.push(2, s)
    SinglyLinkedList.print_list(s)
    ListStack.pop(s)
    SinglyLinkedList.print_list(s)
    print ListStack.top(s)
