import math
import random


def plus(a, b):
    return a+b


def square(a):
    return a**2


def hypot(a, b):
    return math.sqrt(a**2+b**2)


def harmonic(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic(n-1)


def harmonics(li):
    for element in li:
        print(harmonic(element))


def mean(li):
    sum = 0
    for element in li:
        sum += element
    return float(sum) / len(li)


def exchange(li, i1, i2):
    temp = li[i1]
    li[i1] = li[i2]
    li[i2] = temp


def shuffle(li):
    for i in range(0, len(li)):
        new_index = i
        while i == new_index:
            new_index = random.randint(0, len(li))
        exchange(li, i, new_index)


a = float(6)
b = 4
print(isinstance(a/b, int))