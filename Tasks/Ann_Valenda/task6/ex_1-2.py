from functools import reduce
from iteration_utilities import deepflatten


# 1. Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34
def list_after(lst):
    if not lst:
        return lst
    if isinstance(lst[0], list):
        return list_after(lst[0]) + list_after(lst[1:])
    return lst[:1] + list_after(lst[1:])


print(reduce(lambda x, y: x+y, list_after([1, 2, [2, 4, [[7, 8], 4, 6]]])))
# print(list_after([1, 2, [2, 4, [[7, 8], 4, 6]]]))

# ___________var 2___________  (I saw this method before this home task :)


def deep(lst):
    return list(deepflatten(lst))


print(reduce(lambda x, y: x+y, deep([1, 2, [2, 4, [[7, [2, 3, [2, 4]], 8], 4, 6]]])))
# _____________________________________________________________________

# 2. Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова:
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34


def fib(n: int):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    if n >= 2:
        fib_row = fib(n-1)
        fib_row.append(fib_row[-1] + fib_row[-2])
        return fib_row


print(fib(30))
print(fib(20))
print(fib(1))
print(fib(0))
# _______________var2_____________________ if output is n first numbers, how in example
cache = {}


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    if cache.get(n) is not None:
        return cache.get(n)
    else:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]


for i in range(10):
    print(fibonacci(i), end=' ')
