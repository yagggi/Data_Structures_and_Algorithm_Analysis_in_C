

def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def better_fib(n):
    if n <= 1:
        return 1
    last = pre_last = 1
    for i in range(2, n + 1):
        answer = last + pre_last
        pre_last, last = last, answer
    return answer


def eval(n):
    if n == 0:
        return 1.0
    else:
        sum = 0
        for i in range(0, n):
            sum += eval(i)
        return 2.0 * sum / n + n


def better_eval(n):
    c = [0] * (n + 1)
    c[0] = 1.0
    for i in range(1, n + 1):
        sum = 0
        for j in range(0, i):
            sum += c[j]
        c[i] = 2.0 * sum / i + i
    answer = c[n]
    del c
    return answer


def even_better_eval(n):
    c = [0] * (n + 1)
    c[0] = 1.0
    for i in range(1, n + 1):
        pre = c[i - 1]
        answer = 2.0 * pre / i + i
        c[i] = pre + answer
    del c
    return answer
