import time


# def decorator(func):
#     def inner(a, b):
#         print("输入参数 a={0},b={1}".format(a, b))
#         f1 = func(a, b)
#         print("当前时间是= {0}".format(time.ctime()))
#         # print(f1)
#         return f1
#
#     return inner
#
#
# @decorator
# def myadd(a, b):
#     return a + b
#
#
# a = 5
# b = 1
# print("{0} + {1} = {2}".format(a, b, myadd(a, b)))


def pre_str(pre=""):
    def decorator(func):
        def inner(a, b):
            print("装饰器参数pre={0}".format(pre))
            print("输入参数 a={0},b={1}".format(a, b))
            f1 = func(a, b)
            print("当前时间是={0}".format(time.ctime()))
            return f1

        return inner

    return decorator


@pre_str('add')
def add(a, b):
    return a + b


a = 5
b = 1
print("{0}+{1}={2}".format(a, b, add(a, b)))


###
class Test:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("The current function:%s" % self.func.__name__)
        return self.func()


@Test
def test1():
    print("Hello world")


test1()
