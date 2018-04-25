# coding: utf-8


class SinglyLinkedList:

    def __init__(self, next_node=None, **kwargs):
        self.next = next_node
        for k, v in kwargs.items():
            setattr(self, k, v)

    def is_last(self):
        return self.next is None

    @staticmethod
    def find(ele, head, attr_name):
        position = head.next
        while position is not None and getattr(position, attr_name) != ele:
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

        prev_node = SinglyLinkedList.find_prev(ele, head)
        temp_node = prev_node.next
        prev_node.next = temp_node.next
        del temp_node
        gc.collect()
        return

    @staticmethod
    def insert(ele, position):
        temp_node = SinglyLinkedList()
        temp_node.next = position.next
        temp_node.value = ele
        position.next = temp_node
        return

    @staticmethod
    def print_list(head):
        node = head.next
        ans = []
        while node is not None:
            d = {}
            for k, v in node.__dict__.items():
                if k == 'next':
                    continue
                d[k] = v
            ans.append(d)
            node = node.next
        print(ans)
        return ans


class DoublyLinkedList:

    def __init__(self, next_node=None, prev_node=None, **kwargs):
        self.next = next_node
        self.prev = prev_node
        for k, v in kwargs.items():
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


class Polynomial(object):

    def __init__(self, polynomial):
        if not polynomial:
            polynomial = []
        sorted_args = sorted(polynomial, key=lambda x: -x[1])
        self.polynomial = SinglyLinkedList(coefficient=None, exponent=None)
        current_node = self.polynomial
        for coefficient, exponent in sorted_args:
            node = SinglyLinkedList(coefficient=coefficient,
                                    exponent=exponent)
            current_node.next = node
            current_node = node

    @staticmethod
    def add_polynomial(poly1, poly2):
        node1 = poly1.polynomial.next
        node2 = poly2.polynomial.next
        ans = SinglyLinkedList(coefficient=None, exponent=None)
        head = ans
        while node1 is not None and node2 is not None:
            if node1.exponent > node2.exponent:
                ans.next = SinglyLinkedList(coefficient=node1.coefficient,
                                            exponent=node1.exponent)
                node1 = node1.next
            elif node2.exponent > node1.exponent:
                ans.next = SinglyLinkedList(coefficient=node2.coefficient,
                                            exponent=node2.exponent)
                node2 = node2.next
            else:
                ans.next = SinglyLinkedList(coefficient=node1.coefficient + node2.coefficient,
                                            exponent=node1.exponent)
                node1, node2 = node1.next, node2.next
            ans = ans.next
        if node1 is None and node2 is None:
            return head
        elif node1 is None:
            ans.next = node2
            return head
        else:
            ans.next = node1
            return head

    @staticmethod
    def mult_polynomial(poly1, poly2):
        node1 = poly1.polynomial.next
        node2 = poly2.polynomial.next
        ans = SinglyLinkedList(coefficient=None, exponent=None)
        head = ans
        while node2 is not None:
            start = node1
            while start is not None:
                ans.next = SinglyLinkedList(coefficient=start.coefficient * node2.coefficient,
                                            exponent=start.exponent + node2.exponent)
                ans = ans.next
                start = start.next
            node2 = node2.next

        ans = SinglyLinkedList(coefficient=None, exponent=None)
        node = head.next
        head = ans
        while node is not None:
            position = SinglyLinkedList.find(node.exponent, head, 'exponent')
            if position is None:
                ans.next = SinglyLinkedList(coefficient=node.coefficient,
                                            exponent=node.exponent)
                ans = ans.next
            else:
                position.coefficient += node.coefficient
            node = node.next
        return head


class RadixSort(object):

    def __init__(self, nums):
        self.bucket = SinglyLinkedList()
        self.length = len(nums)
        bucket = self.bucket
        for i in range(10):
            bucket.next = SinglyLinkedList(values=[], num=i)
            bucket = bucket.next
        for num in nums:
            position = SinglyLinkedList.find(num % 10, self.bucket, 'num')
            position.values.append(num)

    @staticmethod
    def get_num(num, digit):
        return (num / (10 ** digit)) % 10

    @staticmethod
    def put_num_into_bucket(bucket, num, digit):
        while getattr(bucket, 'num') != digit:
            bucket = bucket.next
            continue
        bucket.values.append(num)

    @staticmethod
    def pop_num_out_bucket(bucket, num):
        temp_bucket = []
        for i in bucket.values[::-1]:
            if i != num:
                temp_bucket.append(bucket.values.pop())
                continue
            else:
                res = bucket.values.pop()
                bucket.values += temp_bucket[::-1]
                return res

    def sort(self):
        digit = 1
        while len(self.bucket.next.values) != self.length:
            bucket = self.bucket.next
            while bucket:
                for num in bucket.values[::-1]:
                    expected_digit = RadixSort.get_num(num, digit)
                    if expected_digit != bucket.num:
                        RadixSort.pop_num_out_bucket(bucket, num)
                        RadixSort.put_num_into_bucket(self.bucket.next, num, expected_digit)
                bucket = bucket.next
            digit += 1
        return self.bucket.next.values


if __name__ == "__main__":
    a = Polynomial(polynomial=[[10, 1000], [5, 14], [1, 0]])
    b = Polynomial(polynomial=[[3, 1990], [-2, 1492], [11, 0], [5, 0]])
    head = Polynomial.add_polynomial(a, b)
    SinglyLinkedList.print_list(head)
    head = Polynomial.mult_polynomial(a, b)
    SinglyLinkedList.print_list(head)

    r = RadixSort(nums=[0, 1, 512, 343, 64, 125, 216, 27, 8, 729])
    print(r.sort())
