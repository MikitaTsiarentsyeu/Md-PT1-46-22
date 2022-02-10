l = [i*(-1) for i in [1,2,3,4,5,6,7,8,9]]

print(l)

# l = [("Fizz"*(i%3==0))+("Buzz"*(i%5==0)) or i for i in range(1,101)]

first_div, second_div = 3, 5
start, stop = 1, 101

def check_rem(i, x):
    return i%x==0

def mult_token(token, mult):
    return token*mult

def main():
    [print(mult_token("Fizz", (check_rem(i, first_div))) + mult_token("Buzz", (check_rem(i, second_div))) or i) for i in range(start,stop)]

main()