def summ_elem(x):
    a = 0
    for i in x:
        if isinstance(i, list):
            a += summ_elem(i)
        else:
            a += i
    return a
x = [1, 2, [2, 4, [[7, 8], 4, 6]]]
print(summ_elem(x))



def fibonacci(n):
    v = []
    fib1 = fib2 = 1
    v.append(fib1)
    v.append(fib2)
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        v.append(fib2)
    return v
n = int(input())
print(fibonacci(n))