n = int(input("Enter any number and I'll tell you if it's prime or not!:"))

def s_prime(n):
    from math import sqrt 
    simple = True

    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            simple = False
            break
        i += 1

    return print(simple if ("True")else("False"))
s_prime(n)
