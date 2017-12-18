# coding: utf-8


def rapid_pow(x, n):
    """
    :type x: int.

    :type n: int
    :rtype: int
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif not n % 2:
        return rapid_pow(x * x, n / 2)
    else:
        return rapid_pow(x * x, n / 2) * x


if __name__ == "__main__":
    from utils import profile
    import random

    test_arg = random.randint(20, 30)

    def normal_pow(x, n):
        for _ in range(n):
            x = x * x
        return x
    print profile(rapid_pow, 2, test_arg)
    print profile(normal_pow, 2, test_arg)
