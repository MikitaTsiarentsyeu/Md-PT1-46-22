# my_func()

def my_func_1():
    print("hello from my_func 1")
    my_func_2()

def my_func_2():
    print("hello from my_func 2")

my_func_1()

# sign = '*'
# if sign == '*':
#     def func(x, y):
#         return x*y
# elif sign == '+':
#     def func(x, y):
#         return x+y  VERY BAD APPROACH

def func(x, y, sign):
    if sign == '*':
        return x*y
    elif sign == '+':
        return x+y

print(func(2, 3, '-'))

def func(x, y):
    print(f"x: {x}, y: {y}")

    return x, y

a, b = func(3, 2)
print(a, b)

def check_int(x):
    x += 2
    return x

a = 2
print(check_int(a))
print(a)

def check_list(x):
    x[0] += 2
    return x

a = [2]
print(check_list(a))
print(a)

a = [3,2,5]
print(sorted(a))
print(a)
print(a.sort())
print(a)


print(sorted([4,2,7,21,6,7,5,5,3,4,3,6,8,6]))