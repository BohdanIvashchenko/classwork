def task1(x, n):
    a = 1
    for i in range(1, n + 1):
        a *= x / i
        yield a


def task2(n):
    a = 1
    for i in range(1, n + 1):
        a += 1 / i
        yield a


def task3(n):
    a1 = 5
    a2 = 19
    yield a1
    yield a2
    for i in range(n):
        a1, a2 = a2, 5 * a1 - 2 * a2
        yield a2

def task4(n):
    a = 1
    b = 1
    for i in range(1, n+1):
        a /= b
        b *= 3

def task5(x, e):
    a = 1
    y = 1
    i = 1

    while abs(a) >= e:
        a *= x/i
        y += a
        i += 1
        yield y