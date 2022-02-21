# 1. Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34
def sum_element_in_list(list):
    total = 0
    for element in list:
        if (type(element) == type([])):
            total = total + sum_element_in_list(element)
        else:
            total = total + element
    return total
print('Сумма элементов -',sum_element_in_list([1, 2, [2, 4, [[7, 8], 4, 6]]]))

# 2. Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34
def first_fibon_n(number): 
    f1 = 0
    f2 = 1
    if (number < 1):
        return f1 
    print(f1, end=" ")
    for items in range(1, number):
        print(f2, end=" ")
        next = f1 + f2
        f1 = f2
        f2 = next
first_fibon_n(5)
first_fibon_n(10)

def fib(number):
    if number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    else:
        output = fib(number-1)
        return output + [output[-1] + output[-2]]
print(fib(5))
print(fib(10))