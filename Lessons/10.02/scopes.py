from cgi import test


for i in range(10):
    x = str(i) + "test"

print(i, x)

def scopes_test():
    x = 44
    print(x)
    x = 55

scopes_test()
scopes_test()

print(x)

[x for x in "test"]

print(x)


test_val = 101

def test_scope(x):
    # print(x)
    # print(test_val)
    global test_val
    test_val = 202
    print(test_val)

def test_scope_2(x):
    # print(x)
    # print(test_val)
    global test_val
    test_val = 303
    print(test_val)

def test_scope_3(x):
    # print(x)
    # print(test_val)
    # test_val = 404
    print(test_val)

test_scope(1)
test_scope_2(2)
test_scope_3(3)
print(test_val)

def outer_func():
    x = "outer value"
    print(x)
    def inner_func():
        nonlocal x
        print(x)
        x = "inner value"
        print(x)
    inner_func()
    print(x)

outer_func()
print(x)