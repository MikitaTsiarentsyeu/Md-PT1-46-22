def test_sum(a, b):
    print(id(a), id(b))
    res = a + b
    return res
    print("after return")

def test_print(val):
    print(str(val).upper())

print(test_sum(2,3))
test_print("hello")

print(type(test_print))

x, y = 8888888, 99999999
print(id(x), id(y))
test_sum(x, y)