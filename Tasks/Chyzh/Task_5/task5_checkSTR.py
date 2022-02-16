# first function <--"check_str"--> that indicates number of upper and lower registry symbols

s = str(input("Enter the string consists of capital and lowercase letters: \n"))
def check_str(s):
    up_counter = 0
    low_counter = 0
    for i in s:
        if i.isupper():
            up_counter += 1
        elif i.islower():
            low_counter += 1
    print("capital letters: ", up_counter, "\nlowercase letters: ",low_counter)
check_str(s)