# def print_10_times(text): not a recursion
#     counter = 0
#     while True:
#         if counter == 10:
#             break
#         print(text)
#         counter += 1

def print_10_times(text, counter = 0):
    if counter == 10:
        return counter
    print(text)
    counter += 1
    print(print_10_times(text, counter))
    # return counter

print_10_times("this is a recursion")

1
1*2
1*2*3
1*2*3*4
1*2*3*4*5

def factorial(n):
    if n == 0:
        return 1
    print(n)
    current = factorial(n-1)
    print(f"n - {n}, current - {current}")
    return n*current

print(factorial(5))