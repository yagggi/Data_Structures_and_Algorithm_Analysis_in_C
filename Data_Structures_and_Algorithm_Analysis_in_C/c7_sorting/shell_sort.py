

class ShellSort:
    def __init__(self, elements=None):
        self.elements = elements
        self.number = len(elements)

    def sort(self):
        inc = self.number
        while inc > 1:
            inc //= 2
            for i in range(inc, self.number, 1):
                tmp = self.elements[i]
                j = i
                while j >= inc:
                    if tmp < self.elements[j - inc]:
                        self.elements[j], self.elements[j - inc] = self.elements[j - inc], self.elements[j]
                    else:
                        break
                    j -= 1
                # self.elements[j] = tmp
        return self.elements


if __name__ == "__main__":
    s = ShellSort([int(x) for x in input().split()])
    print(s.sort())
