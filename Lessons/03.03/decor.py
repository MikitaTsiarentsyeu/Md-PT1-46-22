from unittest import result


def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

def comment_process(func):
    def wrapper(x, y):
        print("the process is started")
        res = func(x, y)
        print(f"the result is {res}")
        print("the process is finished")
        return res
    return wrapper

@comment_process
def sum(a, b):
    return a+b

x = sum(3,4)
print(x)

@do_twice
def print_number_four():
    print(4)

# print_number_four()

# x = do_twice(print_number_four)
# x()
# print_number_four = x

# print_number_four = do_twice(print_number_four)