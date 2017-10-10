# coding: utf-8


def loops(l):
    """
    :type l: [int,]
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


# better loops
def better_loops(l):
    max_sum = 0
    for i in range(len(l)):
        this_sum = 0
        for j in range(i, len(l)):
            this_sum += l[j]
        if max_sum is None or this_sum > max_sum:
            max_sum = this_sum
    return max_sum


if __name__ == "__main__":
    import timeit
    from functools import partial
    test_arg = [1, 2, 3, 4, -1, 5, -2, 8]
    print timeit.Timer(partial(loops, test_arg)).timeit(3)
    print timeit.Timer(partial(better_loops, test_arg)).timeit(3)
