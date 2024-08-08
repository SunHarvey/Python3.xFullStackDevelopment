from Chapter3.iterator_example import Fibs


def fibs(max):
    a, b = 1, 1
    count = 0
    while True:
        if count == max:
            raise StopIteration
        yield a
        a, b = b, a + b
        count += 1


if __name__ == '__main__':
    fib = Fibs(500)
    for item in fib:
        print(item)
