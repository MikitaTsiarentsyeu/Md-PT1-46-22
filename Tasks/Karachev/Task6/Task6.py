
l = [1, 2, [2, 4, [[7, 8, [1,2]], 4, 6, [1,1]]]]

def sum_list(l):
    summ = 0
    for number in l:
        if isinstance(number, list):
            summ += sum_list(number)
        else:
            summ += number
    return summ 

print(sum_list(l))


def fibon(number):     
    if number == 1:
        return [0, 1]    
    feb_row = fibon(number-1)
    feb_row.append(feb_row[-1]+feb_row[-2])
    return feb_row

print(fibon(10))