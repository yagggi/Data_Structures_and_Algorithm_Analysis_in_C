# coding: utf-8


def profile(func, *args, **kwargs):
    import timeit
    from functools import partial
    return timeit.Timer(partial(func, *args, **kwargs)).timeit(1)
