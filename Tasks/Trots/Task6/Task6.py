from functools import reduce

list1 = [1, 2, [2, 4, [2, 8], [[7, 8], 4, 6]]]
list2 = [7, [[[[2]]], [[[]], [4]], [4, 5, [6, 7]]], 8]


def suml_1(lst: list, s=0) -> int:
    for el in lst:
        if isinstance(el, list):
            s += suml_1(el)
        else:
            s += el
    return s


print(f"Sum of elements - : {suml_1(list1)}")


def suml_2(lst: list, res=None) -> int:
    if res is None:
        res = []
    for el in lst:
        suml_2(el, res) if isinstance(el, list) else res.append(el)
    return sum(res)


print(f"Sum of elements - : {suml_2(list1)}")


def suml_3(lst: list):
    return reduce(lambda a, b: a.extend(suml_3(b)) or a if isinstance(b, list) else a.append(b) or a, lst, [])


print(f"Sum of elements - : {sum(suml_3(list1))}")


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
