def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True
print(is_prime(777))

def check_str(s: str):
    up_count = 0
    low_count = 0
    for i in s:
        if i.isupper():
            up_count += 1
        if i.islower():
            low_count += 1
    print(up_count, low_count)
check_str("Допуски среднего диаметра    внутреВыыыннВыей резьбы, предназначенной для соединения с наружной конической")


def get_ranges(A: list):
    B = []
    start = A[0]
    j = 0
    for i in range(1, len(A)):
        if A[i] - A[i-1] != 1:
            stop = A[i-1]
            B.append(f'{start}-{stop}') if ((i) - j) != 1 else B.append(f'{start}')
            start = A[i]
            j = i
    stop = A[-1]
    B.append(f'{start}-{stop}') if j < (len(A) - 1) else B.append(f'{stop}')
    print(', '.join(B))
get_ranges([0,1,2,3,5,6,7,9,11,25,26])

