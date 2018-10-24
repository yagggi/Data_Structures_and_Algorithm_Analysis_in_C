

class MergeSort:

    def __init__(self, elements=None):
        if not elements:
            raise Exception('Elements must not be null')
        self.elements = elements

    def sort(self, elements=None):
        if elements is None:
            elements = self.elements
        length = len(elements)
        if length == 1:
            return list(elements)
        center = length // 2
        return self.merge(self.sort(elements[:center]), self.sort(elements[center:]))

    def merge(self, left, right):
        lind = rind = 0
        llen, rlen = len(left), len(right)
        res = []
        while left and right and lind < llen and rind < rlen:
            if left[lind] > right[rind]:
                res.append(right[rind])
                rind += 1
            else:
                res.append(left[lind])
                lind += 1
        return res + (left[lind:] or right[rind:])


if __name__ == "__main__":
    s = MergeSort([int(x) for x in input().split()])
    print(s.sort())
