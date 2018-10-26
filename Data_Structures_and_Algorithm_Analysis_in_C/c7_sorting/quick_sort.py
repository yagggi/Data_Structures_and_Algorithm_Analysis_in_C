

class QuickSort:

    def __init__(self, elements=None):
        if not elements:
            raise Exception('Elements must not be null.')
        self.elements = elements
        self.left = 0
        self.right = len(elements) - 1

    def sort(self, elements=None, left=None, right=None):
        if elements is None:
            elements = self.elements
        if left is None:
            left = self.left
        if right is None:
            right = self.right
        pass

    def med3(self, elements, left, right):
        """Median-of-three partitioning"""
        def swap(e, ind1, ind2):
            e[ind1], e[ind2] = e[ind2], e[ind1]
        center = (left + right) // 2
        if elements[left] > elements[center]:
            swap(elements, left, center)
        if elements[left] > elements[right]:
            swap(elements, left, right)
        if elements[center] > elements[right]:
            swap(elements, center, right)
        swap(elements, center, right - 1)
        return elements[right - 1]
