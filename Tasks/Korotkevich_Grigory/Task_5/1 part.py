s = str(input("Enter any, most importantly, non-empty string:"))

def check_str(s):
    a=sum(map(str.isupper, s))
    b=sum(map(str.islower, s))

    return print(a,"upper case,",b,"lower case")

check_str(s)
