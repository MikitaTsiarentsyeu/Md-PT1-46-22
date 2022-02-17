from functools import reduce

def cycle(l, f, i = 0):
    if i == len(l):
        return
    f(l[i])
    cycle(l, f, i+1)

l = [1,2,3,4,5,6,7,8,9]
cycle(l, print)

def print_sq(num):
    print(num*num)

cycle(l, print_sq)

lambda_print_sq = lambda num: print(num*num)
lambda_print_sq(100)
cycle(l, lambda_print_sq)

# def sum(x, y):
#     return x+y

sum = lambda x, y=0: x+y
print(sum(2,4))
print(sum(200))

cycle(l, lambda num: print(num*num))

test_str = "Abc Aac aaa ttt kit kot"
print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l, key=lambda x: x[1]))

d = {"one": 1, "two": 2, "three": 3}
# print(sorted(d, key=d.get))
print(sorted(d.items(), key=lambda v: v[1]))

l = [1,2,3,4,5,6,7,8,9]
# print(map(print, l))
mp_obj = map(print, l)
# mp_iter = iter(mp_obj)
# next(mp_iter)
# next(mp_iter)
# next(mp_iter)
for i in mp_obj: pass

print(list(map(lambda num: chr(num*10), l)))

print([(lambda num: chr(num*10))(x) for x in l])

(lambda lst: print([chr(x*10) for x in lst]))(l)

print(list(filter(lambda x: x>4, l)))

print(list(map(lambda num: chr(num*10), filter(lambda x: x>4, l))))

print(reduce(lambda x, y: x+y, l))

print(reduce(lambda x, y: x if x >= y else y, l))

print(reduce(lambda x, y: f"{x}-{y}", l))


l = ['1', '11', '12', '22', '2', '13', '30', '33']

print(sorted(filter(lambda x: int(x) % 2 == 0, l), key=int))

