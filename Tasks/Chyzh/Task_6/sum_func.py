
list = [11, 2, 8, [7,9,100], [13,1,0,[2,3,[45,7,1]]]]

def sum(list):
    sum1 = 0
    for i in list:
        if (type(i) == type([])):
            sum1 = sum1 + sum(i)
        else:
            sum1 = sum1 + i
    return sum1

print("The sum of all elements in list including nested lists elements is: ", sum(list))

