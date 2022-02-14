# second function <--"is_prime"--> that indicates if number is prime


num = int(input("Enter any numeric value to check if it's prime: "))
def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return print("Not prime!")
            break
    return print("Grats! It's prime!")
is_prime(num)