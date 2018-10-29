

class QuickSort:

    def __init__(self, elements=None):
        if not elements:
            raise Exception('Elements must not be null.')
        self.elements = elements
        self.left = 0
        self.right = len(elements) - 1

    def insertion_sort(self, elements, left, right):
        for ind in range(left, right):
            sub_ind = ind
            while sub_ind > left and elements[sub_ind - 1] > elements[sub_ind]:
                elements[sub_ind - 1], elements[sub_ind] = elements[sub_ind], elements[sub_ind - 1]
                sub_ind -= 1
        return

    def sort(self, elements=None, left=None, right=None):
        if elements is None:
            elements = list(self.elements)
        if left is None:
            left = self.left
        if right is None:
            right = self.right

        cutoff = 3
        if left + cutoff <= right:
            pivot = self.med3(elements, left, right)
            i = left
            j = right - 1
            while True:
                i += 1
                j -= 1
                while elements[i] < pivot:
                    i += 1
                while elements[j] > pivot:
                    j -= 1
                if i < j:
                    self.swap(elements, i, j)
                else:
                    break
            self.swap(elements, i, right - 1)
            self.sort(elements, left, i - 1)
            self.sort(elements, i + 1, right)
        else:
            self.insertion_sort(elements, left, right + 1)
        return elements

    def swap(self, e, ind1, ind2):
        e[ind1], e[ind2] = e[ind2], e[ind1]

    def med3(self, elements, left, right):
        """Median-of-three partitioning"""
        center = (left + right) // 2
        if elements[left] > elements[center]:
            self.swap(elements, left, center)
        if elements[left] > elements[right]:
            self.swap(elements, left, right)
        if elements[center] > elements[right]:
            self.swap(elements, center, right)
        self.swap(elements, center, right - 1)
        return elements[right - 1]

    def select(self, kth, elements=None, left=None, right=None):
        if kth <= 0 or kth > self.right:
            raise Exception('kth must be a positive number and not big than elements count.')
        if elements is None:
            elements = list(self.elements)
        if left is None:
            left = self.left
        if right is None:
            right = self.right
        cutoff = 3
        if left + cutoff <= right:
            pivot = self.med3(elements, left, right)
            i = left
            j = right - 1
            while True:
                i += 1
                j -= 1
                while elements[i] < pivot:
                    i += 1
                while elements[j] > pivot:
                    j -= 1
                if i < j:
                    self.swap(elements, i, j)
                else:
                    break
            self.swap(elements, i, right - 1)
            if kth <= i:
                self.select(kth, elements, left, i - 1)
            elif kth > i + 1:
                self.select(kth, elements, i + 1, right)
        else:
            self.insertion_sort(elements, left, right + 1)
        return elements[kth - 1]


if __name__ == "__main__":
    s = QuickSort([int(x) for x in input('Enter elements seperated by single space:\n').split()])
    kth = int(input('Enter the k-th smallest:\n'))
    print(s.sort(), f'\n{kth}-th smallest:{s.select(kth)}')
