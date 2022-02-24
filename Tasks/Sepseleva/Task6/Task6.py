def get_sum(l):
    sm = 0
    for i in l:
        if not isinstance(i, list):
            sm += i
        else:
            sm += get_sum(i)
    return sm

print(get_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fibonacci(n):
    if n == 2:
        return [0,1]
    fib_l = fibonacci(n-1)
    fib_l.append(fib_l[-1] + fib_l[-2])
    return fib_l    

print(fibonacci(15))

