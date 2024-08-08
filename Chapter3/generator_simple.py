# def mygen():
#     print("gen() 1")
#     yield 1
#
#     print("gen() 2")
#     yield 2
#
#     print("gen() 3")
#     yield 3
#
#
# gen = mygen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def odd(max):
#     n = 1
#     count = 0
#     while True:
#         yield n
#         n += 2
#         count += 1
#         if count == max:
#             raise StopIteration
#
#
# odd_num = odd(3)
# for num in odd_num:
#     print(num)

class Odd:
    def __init__(self, max):
        self.count = 0
        self.max = max
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 2
        self.count = self.count + 1
        if self.count > self.max:
            raise StopIteration
        return self.start


odd_num = Odd(4)
for num in odd_num:
    print(num)
