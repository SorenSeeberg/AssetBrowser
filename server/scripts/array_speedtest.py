import timeit
import array
import numpy

ITERATIONS = 1000
SIZE = 2**16


def test1():
    for x in range(ITERATIONS):
        data = list()
        for y in range(SIZE):
            data.append(y)


def test2():
    for x in range(ITERATIONS):
        data = [0 for x in range(SIZE)]
        for y in range(SIZE):
            data[y] = y


def test3():
    data = [0 for x in range(SIZE)]
    for x in range(ITERATIONS):
        for y in range(SIZE):
            data[y] = y


def test4():
    data = array.array('I', (0 for x in range(SIZE)))
    for x in range(ITERATIONS):
        for y in range(SIZE):
            data[y] = y


def test5():
    data = numpy.array([0 for x in range(SIZE)], dtype=numpy.int16)
    for x in range(ITERATIONS):
        for y in range(SIZE):
            data[y] = y


if __name__ == '__main__':
    print(f'Array Linear Write Test i: {ITERATIONS} s: {SIZE}\n-----------------------')
    print('List 01      :', timeit.timeit(stmt=test1, number=1))
    print('List 02      :', timeit.timeit(stmt=test2, number=1))
    print('List 03      :', timeit.timeit(stmt=test3, number=1))
    print('Array 01     :', timeit.timeit(stmt=test4, number=1))
    print('NP Array 01  :', timeit.timeit(stmt=test5, number=1))
