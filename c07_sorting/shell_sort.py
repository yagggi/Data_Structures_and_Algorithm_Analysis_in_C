

class ShellSort:
    def __init__(self, elements=None):
        self.elements = elements
        self.number = len(elements)

    def sort(self):
        # using Shell sequence, yet not a good one
        inc = self.number
        while inc > 1:
            inc //= 2
            for i in range(inc, self.number, 1):
                tmp = self.elements[i]
                j = i
                while j >= inc:
                    if tmp < self.elements[j - inc]:
                        self.elements[j] = self.elements[j - inc]
                    else:
                        break
                    j -= inc
                self.elements[j] = tmp
        return self.elements


if __name__ == "__main__":
    s = ShellSort([int(x) for x in input().split('Enter elements seperated by single space:\n')])
    print(s.sort())
