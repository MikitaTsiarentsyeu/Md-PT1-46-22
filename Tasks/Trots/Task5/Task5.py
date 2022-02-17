#!/usr/bin/env python3

def is_prime(x):
    if (x == 2) or (x == 3):
        return True
    if (x % 2 == 0) or (x < 2):
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

print(is_prime(13))


def check_str(text: str):
    u_case = 0
    l_case = 0
    for i in text:
        if i.islower():
            l_case += 1
        elif i.isupper():
            u_case += 1
    return f"{u_case} upper case ,{l_case} lower case"

print(check_str('The quick Brow Fox'))


def get_ranges(some_list):
    i = 0
    s = f""
    while i < len(some_list):
        if i == 0:
            s += f"{some_list[i]}"
        else:
            s += f", {some_list[i]}"
        j = i
        count = 1
        while (j < len(some_list) - 1) and (some_list[j] == some_list[j + 1] - 1):
            count = count + 1
            j = j + 1
        if count >= 2:
            s += f"-{some_list[i + count - 1]}"
            i = i + count
        else:
            i = i + 1
    return s


list_1 = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 15]
list_2 = [4, 7, 10]
list_3 = [2, 3, 8, 9]
list_4 = [0, 1, 2, 3, 4, 7, 8, 10]

print(get_ranges(list_4))
