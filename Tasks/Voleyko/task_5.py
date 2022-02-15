#Task5_1
#1Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
#check_str('The quick Brow Fox') -> '3 upper case, 12 lower case'
def check_str(string):
    lower = []
    upper = []
    for i in range(len(string)):
        if string[i].islower():
            lower.append(i)
        elif string[i].isupper(): 
            upper.append(i)
    return len(upper),len(lower)
print(check_str('The quick Brow Fox')[0],'upper case,', check_str('The quick Brow Fox')[1],'lower case')

#Task5_2
#Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
#is_prime(787) -> True
#is_prime(777) -> False
def is_prime (number):
    for x in range(2, number):
        if (number%x ==0):
            return False
    return True
print(is_prime(787))
print(is_prime(777))
#Task5_3
#Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
#отсортированных по возрастанию, и которая этот список “сворачивает”.
#get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#get_ranges([4,7,10])  -> "4, 7, 10"
#get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
def get_ranges(list):
    new_list = []
    prev = min(list)
    for i in sorted(list):
        if i == prev + 1:
            new_list[-1].append(i)
        else:
            new_list.append([i])
        prev = i
    return ','.join(['{}-{}'.format(i[0], i[-1]) if len(i) > 1 else str(i[0]) for i in new_list])
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10])) 
print(get_ranges([4,7,10])) 
print(get_ranges([2,3,8,9])) 