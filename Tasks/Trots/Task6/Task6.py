from functools import reduce

list1 = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def sum_l(lst: list) -> int:
    s = 0
    for el in lst:
        if type(el) == list:
            s += sum_l(el)
        else:
            s += el
    return s


print(f"Sum of elements - : {sum_l(list1)}")


def fib(n: int) -> list:
    if n == 1:
        return [0, 1]
    li = fib(n - 1)
    li.append(li[-1] + li[-2])
    return li


print(fib(10))


def fibonacci(n: int) -> list:
    return reduce(lambda r, v: r.append(r[-1] + r[-2]) or r, range(n - 1), [0, 1])


print(fibonacci(10))
