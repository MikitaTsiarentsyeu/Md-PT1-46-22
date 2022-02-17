def is_prime(x):
    if isinstance(x, int) and x > 1:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True


def check_str(s: str):
    up_count = 0
    low_count = 0
    for i in s:
        if i.isupper():
            up_count += 1
        if i.islower():
            low_count += 1
    print(f'{up_count} - upper case, {low_count} - lower case')


def get_ranges(user_list: list):
    b = []
    start = user_list[0]
    j = 0
    for i in range(1, len(user_list)):
        if user_list[i] - user_list[i - 1] != 1:
            stop = user_list[i - 1]
            b.append(f'{start}-{stop}') if (i - j) != 1 else b.append(f'{start}')
            start = user_list[i]
            j = i
    stop = user_list[-1]
    b.append(f'{start}-{stop}') if j < (len(user_list) - 1) else b.append(f'{stop}')
    print(', '.join(b))



check_str("The Python Software Foundation (PSF) is a 501 non-profit corporation")
print(is_prime(707))
get_ranges([-5, 0, 1, 2, 3, 5, 6, 7, 9, 11, 25, 26])

