def func(x):
    return x * x


result = map(func, [1, 2, 3])
print(list(result))

result = map(lambda x: x + 3, [1, 3, 5, 6])
print(list(result))
