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

    def is_empty(self):
        return self.stack == []


class ReversePolish(object):

    def __init__(self, postfix):
        self.args = list(postfix)
        self.stack = ArrayStack()
        self.operators = ['+', '-', '*', '/']

    def is_operator(self, x):
        return x in self.operators

    def cal(self):
        for x in self.args:
            if self.is_operator(x):
                a = self.stack.pop()
                b = self.stack.pop()
                res = eval('%s%s%s' % (b, x, a))
                self.stack.push(res)
            else:
                try:
                    x = int(x)
                except ValueError:
                    raise
                self.stack.push(x)
        return self.stack.top()


class InfixToPostfix(object):

    def __init__(self, infix):
        from collections import defaultdict
        self.infix = list(infix)
        self.allow_operators = ['+', '*', '(', ')']
        self.postfix = []
        self.priority_dic = defaultdict(lambda: 4)
        self.priority_dic.update(
            {
                '+': 1,
                '*': 2,
                '(': 3,
            }
        )

    def get_priority(self, x):
        return self.priority_dic[x]

    def is_number(self, x):
        return x not in self.allow_operators

    def to_postfix(self, helper=None, index=0):
        if not helper:
            helper = ArrayStack()
        try:
            x = self.infix[index]
        except Exception:
            while not helper.is_empty():
                self.postfix.append(helper.pop())
                return

        if self.is_number(x):
            self.postfix.append(x)
        elif x == ')':
            poped = helper.pop()
            while poped != '(':
                self.postfix.append(poped)
                poped = helper.pop()
        else:
            while (not helper.is_empty() and
                   self.get_priority(helper.top()) >= self.get_priority(x) and
                   helper.top() != '('):
                self.postfix.append(helper.pop())
            helper.push(x)
        self.to_postfix(helper=helper, index=index + 1)

    def trans(self):
        self.to_postfix()
        return ''.join(self.postfix)


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

    print '---ReversePolish---'
    postfix = '6523+8*+3+*'
    r = ReversePolish(postfix)
    print 'postfix: %s' % postfix
    print 'res: %s' % r.cal()

    print '---InfixToPostfix---'
    args = 'a+b*c+(d*e+f)*g'
    infix = InfixToPostfix('a+b*c+(d*e+f)*g')
    print 'infix: %s' % args
    print 'postfix: %s' % infix.trans()
