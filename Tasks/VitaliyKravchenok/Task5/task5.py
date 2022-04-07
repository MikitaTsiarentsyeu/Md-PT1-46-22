# Реализовать функцию check_str которая получает на вход непустую строку
# и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brow Fox') -> '3 upper case, 12 lower case'

def check_str(a: str):
    lower_counter = 0
    upper_counter = 0
    for i in a:
        if i.isalpha():
            if i.isupper():
                upper_counter += 1
            else:
                lower_counter += 1

    print(f"{upper_counter} upper case, {lower_counter} lower case")


# 2. Реализовать функцию is_prime которая получает на вход любое число больше
# нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

def is_prime(a):
    if a in [1, 2, 3]:
        return True
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


# 3. Реализовать функцию get_ranges которая получает на вход непустой
# список неповторяющихся целых чисел,
# отсортированных по возрастанию, и которая этот список “сворачивает”.
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


def get_ranges(a):
    x = a[0]
    counter = 0
    for i in range(len(a) - 1):
        if a[i] == a[i + 1] - 1:
            counter += 1
            y = a[i + 1]
            if len(a) - 2 == i:
                print(f"{x} - {a[-1]}")
        else:
            if counter != 0:
                print(f"{x} - {y}")
                counter = 0
                x = a[i + 1]
            else:
                print(a[i])
                x = a[i + 1]
            if len(a) - 2 == i:
                print(a[-1])


get_ranges([0, 1, 2, 3, 5, 7, 8, 9, 12, 13, 15])



