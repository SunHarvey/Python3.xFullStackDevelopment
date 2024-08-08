# lst = [1, 2, 3, 4]
# it = iter(lst)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# for x in lst:
#     print(x)
#
# file = open('./reduceFunc.py')
# for line in file:
#     print(line.strip())


# def fib(max):
#     a, b = 1, 1
#     idx = 0
#     ls = []
#
#     while True:
#         if idx == max:
#             return ls
#         ls.append(a)
#         a, b = b, a + b
#         idx = idx + 1
#
#
# if __name__ == '__main__':
#     result = fib(10)
#     print(result)

class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if self.idx == self.max:
            raise StopIteration

        self.idx = self.idx + 1
        self.a, self.b = self.b, self.a + self.b
        return fib


if __name__ == '__main__':
    fibs = Fibs(10)
    print(list(fibs))
