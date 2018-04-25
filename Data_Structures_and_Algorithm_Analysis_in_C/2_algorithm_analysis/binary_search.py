# coding: utf-8


def binary_search(l, x):
    """
    :type l: list(int), sorted ASC.

    :type x: int, the number to search
    :rtype: int, index of x or -1
    """
    left = 0
    right = len(l) - 1
    while left < right:
        center = (left + right) / 2
        if l[center] == x:
            return center
        elif l[center] > x:
            right = center - 1
        elif l[center] < x:
            left = center + 1
    return -1


if __name__ == "__main__":
    import random
    from ..utils import profile
    test_list = range(1000000)
    x = random.randint(0, 1000000)
    print(profile(binary_search, test_list, x))
