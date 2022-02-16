# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.

text = "The quick Brow Fox"

def check_str(text):
    x, y = [], []
    for i in text:
        if i.isupper():
            x.append(i)
        if i.islower():
            y.append(i)
    print (f"\n\n{len(x)} upper case, {len(y)} lower case\n\n")
    #print(x)
    #print(y)
check_str(text)



# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.

import math

user_input = int(input("Please enter a positive number '> 0' \n"))     

def is_prime(user_input):
    if user_input <= 0:
        print("\nincorrect input, number '<= 0' \n")
        exit()
    elif user_input == 1:
        print("False\n")
        exit()
    elif user_input == 2:
        print("True\n")
        exit()
    elif user_input > 2:
        i = 2
        limit = int(math.sqrt(user_input))
        while i <= limit:
            if user_input % i == 0:
                print("False\n")
                exit()
            i += 1
        print("True\n")
is_prime(user_input)



# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, отсортированных по возрастанию, и которая этот список “сворачивает”.

l1 = [0, 1, 2, 9, 3, 4, 7, 8, 10]
l2 = [4,7,10]
l3 = [2, 3, 8, 9]
l4 = [1, 2, 3, 3, 15, 10, 10, 11, 12, 13]


def get_ranges(l1):
    l1 = list(sorted(set(l1)))
    l_new = []
    for i in l1:
        if l1[i]-l1[i+1] == -1:
            l_new.append(i)
        print(f' "{min(l_new)} - {max(l_new)}')
get_ranges(l1)

