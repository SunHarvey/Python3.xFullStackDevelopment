from functools import reduce


def add(x, y):
    return x + y


data = [1, 2, 3, 4]

r = reduce(add, data)
print(r)

fun = lambda x, y: x + y
r2 = reduce(fun, data)
print(r2)
