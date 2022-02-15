counter_base = 0

# def counter(n): DEPENDENT COUNTERS
#     global counter_base
#     counter_base = n
#     def inner():
#         global counter_base
#         counter_base += 1
#         return counter_base
#     return inner

def counter(n): #INDEPENDENT COUNTERS
    def inner():
        nonlocal n
        n += 1
        return n
    return inner

c1 = counter(0)

for i in range(10):
    print(c1())

c2 = counter(100)

for i in range(10):
    print(c2())

for i in range(10):
    print(c1())