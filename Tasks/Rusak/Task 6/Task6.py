# 1. Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.

def sum_list(any_list):
    summ = 0
    for i in any_list:
        if isinstance(i, list):
            summ += sum_list(i)
        else:
            summ += i
    return summ

l = [1, 2, [2, 4, [[7, [[], []], 12, 10, [9,[11, 12], 10], 8], 4, 6]]]

print(sum_list(l))


# 2. Написать функцию для вычисления n первых чисел Фибоначчи.

def Fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    fib_list = Fibonacci(n-1)
    fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

print(Fibonacci(5))