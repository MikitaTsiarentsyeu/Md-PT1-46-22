from sympy import false, true


def times(a, b):
    return a*b

print(times(2, 3))
print(times([2], 3))
print(times('[2]', 3))

def times_for_int(a:int, b:int) -> int:
    "this function will multiply only int values"
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times_for_int(2, 3))

def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return false
    for i in l2:
        if i not in l1:
            return false
    return true

print(eq((1,2,3), (1,2,3)))