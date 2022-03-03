import time

t = 0

def time_dec(func):
    def wrapper(n):
        start = time.time()
        res = func(n)
        global t
        t = time.time() - start
        return res
    return wrapper

@time_dec
def loader(n):
    r = 0
    for i in range(n):
        r += i
    return r

x = loader(100000)
print(x, t)