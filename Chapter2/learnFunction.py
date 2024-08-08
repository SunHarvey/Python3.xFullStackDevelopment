# def func(x, *args):
#     print("x={0},args={1}".format(x, args))
#     result = x
#     for i in args:
#         result = result + i
#     return result
#
#
# print("result=", func(1, 2, 3))

##
# for i in range(0, -5, -1):
#     print(i)
#
# x = "abcde"
# for i in range(len(x)):
#     print(x[i])
##

def test(fun, a, b):
    print(fun(a, b))


def func(x, y):
    return 2 * x + y


test(func, 1, 2)
