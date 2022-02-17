l = []

try:
    l[0]
except IndexError:
    print("something went wrong")

print("after error")


# for i in range(10):
#     print(i)

it = iter(range(10))
try:
    while True:
        print(next(it))
except StopIteration:
    pass



n = 4

try:
    if n <= 5:
        raise RuntimeError
    print(n)
except RuntimeError:
    print("please input value higher than 5")