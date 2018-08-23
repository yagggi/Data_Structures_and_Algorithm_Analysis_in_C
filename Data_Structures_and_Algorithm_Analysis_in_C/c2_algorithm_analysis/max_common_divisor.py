

def gcd(m, n):
    """
    :type m: int.

    :type n: int
    :rtype: int
    """
    while n > 0:
        rem = m % n
        m = n
        n = rem
    return m


if __name__ == "__main__":
    from ..utils import profile
    import random

    test_arg1, test_arg2 = random.randint(10000, 1000000), random.randint(1, 10000)
    print(profile(gcd, test_arg1, test_arg2))
