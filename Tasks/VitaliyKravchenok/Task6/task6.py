# Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34


def summ_elem(x):
    summ = 0
    for n in x:
        if isinstance(n, list):
            summ += summ_elem(n)
        else:
            summ += n
    return summ 

x = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(summ_elem(x))


# Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34


def fib_num(n: int):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    if n >= 2:
        fib = fib_num(n-1)
        fib.append(fib[-1] + fib[-2])
        return fib

n = int(input())
print(fib_num(n))