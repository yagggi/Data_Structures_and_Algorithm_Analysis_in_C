

class InsertionSort:
    def __init__(self, elements=None):
        self.elements = elements

    def sort(self):
        for ind, ele in enumerate(self.elements):
            sub_ind = ind
            while sub_ind > 0 and self.elements[sub_ind - 1] > self.elements[sub_ind]:
                self.elements[sub_ind - 1], self.elements[sub_ind] = self.elements[sub_ind], self.elements[sub_ind - 1]
                sub_ind -= 1
        return self.elements


if __name__ == "__main__":
    s = InsertionSort([int(x) for x in input().split()])
    print(s.sort())
