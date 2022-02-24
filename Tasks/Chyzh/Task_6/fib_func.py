
def fibonacci(n: int):
    if n == 0 or n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1]
    list = fibonacci(n-1)
    list.append(list[-1] + list[-2])
    return list
    
n = int(input("Enter the value of how many fibonacci numbers you want to calculate: "))        
print(fibonacci(n))