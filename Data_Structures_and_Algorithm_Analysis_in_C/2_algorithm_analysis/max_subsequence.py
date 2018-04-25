# coding: utf-8


def loops(l):
    """
    :type l: [int,].

    :rtype: int
    """
    max_sum = None
    for i in range(len(l)):
        for j in range(i, len(l)):
            this_sum = 0
            for k in range(i, j + 1):
                this_sum += l[k]
            if max_sum is None or this_sum > max_sum:
                max_sum = this_sum
    return max_sum


def better_loops(l):
    max_sum = 0
    for i in range(len(l)):
        this_sum = 0
        for j in range(i, len(l)):
            this_sum += l[j]
        if max_sum is None or this_sum > max_sum:
            max_sum = this_sum
    return max_sum


def divide_and_conquer(l, left, right):
    # print left, right
    if left == right:
        if l[left] > 0:
            return l[left]
        else:
            return 0

    center = (left + right) / 2
    max_left_sum = divide_and_conquer(l, left, center)
    max_right_sum = divide_and_conquer(l, center + 1, right)

    max_left_border_sum = left_border_sum = 0
    for i in range(center, left - 1, -1):
        left_border_sum += l[i]
        if left_border_sum > max_left_sum:
            max_left_sum = left_border_sum

    max_right_border_sum = right_border_sum = 0
    for i in range(center, right + 1):
        right_border_sum += l[i]
        if right_border_sum > max_right_sum:
            max_right_sum = right_border_sum

    return max([max_left_sum, max_right_sum,
               max_left_border_sum + max_right_border_sum])


def best(l):
    max_sum = this_sum = 0
    for i in range(0, len(l)):
        this_sum += l[i]
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum


if __name__ == "__main__":
    from utils import profile
    test_arg = [1, 2, 3, 4, -1, 5, -2, 8] * 100
    print profile(loops, test_arg)
    print profile(better_loops, test_arg)
    print profile(divide_and_conquer, test_arg, 0, len(test_arg) - 1)
    print profile(best, test_arg)
