from unicodedata import decimal


User_List = [1, 2, [2, 4, [[7, 8], 4, 6]]]
def sum_of_list(User_List):
    if type(User_List) is int:
        return User_List
    else:
        result = 0
        for i in User_List:
            result += sum_of_list(i)               
        return result
print(sum_of_list(User_List))

def fib(number_of_first_fibonacci_numbers: decimal):
    if number_of_first_fibonacci_numbers in [0,1,2]:
        return [0,1,1]
    List_fib = fib(number_of_first_fibonacci_numbers - 1)
    List_fib.append(List_fib[-1] + List_fib[-2])
    if len(List_fib) > number_of_first_fibonacci_numbers:
        List_fib.pop(-1)
    return List_fib
print(fib(5))


