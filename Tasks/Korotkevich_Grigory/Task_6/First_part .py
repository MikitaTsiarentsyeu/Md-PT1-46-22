l = [1, 2, [2, 4, [[7, 8], 4, 6]]]

def sum_of_elements(l):
    summ = 0
    for i in l:
        if isinstance(i, list):
            summ += sum_of_elements(i)
        else:
            summ += i
    return summ 

print(sum_of_elements(l))
