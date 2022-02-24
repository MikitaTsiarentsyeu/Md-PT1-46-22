def first_fibonacci_numbers(number):
    if number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    else:
        output = first_fibonacci_numbers(number-1)
        return output + [output[-1] + output[-2]]
print(first_fibonacci_numbers(5))
print(first_fibonacci_numbers(10)) 
