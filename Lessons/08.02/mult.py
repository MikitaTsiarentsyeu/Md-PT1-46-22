def canonical_mult(a, b):
    if b < 0:
        # a, b = b, a
        a = -a
        b = -b
    res = 0
    for i in range(b):
        res += a

    return res

print(canonical_mult(3, 2))