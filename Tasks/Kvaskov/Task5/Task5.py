import random
import decimal




k = decimal.Decimal()
x = str()
a = []




def check_str(string):
    number_ch_title = []
    number_ch_lower = []
    other_ch = []
    string = str(input("Input some string in lower and upper case\n"))
    for i in range(len(string)):
        if ord(string[i]) in range(65,91):
            number_ch_title.append(string[i])
        elif ord(string[i]) in range(97, 123):
            number_ch_lower.append(string[i])
        else:
            other_ch.append(string[i])
    print(f" {len(number_ch_title)} upper case\n {len(number_ch_lower)} lower case" )

def is_prime(number):
    a = random.randint(1, 100)
    b = decimal.Decimal(a) 
    number = decimal.Decimal(input("Input number bigger than null, not including 1 (one)\n"))
    if b % number == 0:
        b += 3
        if (b**(number - 1) - 1) % number == 0: # Fermat's little theorem
            print(f"number = {number} True ")    
        else:
            print(f"number = {number} False ")     
    elif (b**(number - 1) - 1) % number == 0:
        print(f"number = {number} True ")
    else:    
        print(f"number = {number} False ")

def get_ranges(User_List):
    User_List = list(map(int, input("enter a list of numbers separated by spaces\n").split()))
    List1 = sorted(User_List)
    n = 0
    List_1 = []
    List_2 = []
    List_3 = []
    for i in range(1, len(List1)):
        if List1[i] - List1[n] == 1:
            List_1 = List1[n], List1[i]
            List_2.extend(List_1)
            n += 1
        else:
            if n == 0:
                List_3.append(List1[0])
            List_3.append(List1[n + 1])
            n += 1
    for j in List_2:
        if j in List_3:
            List_3.remove(j)
    set(List_2)
    list(List_2)            
    
    print(f"numbers from task {List_2} \nother number {List_3} ")

    
   
    

        




#check_str(x)
#is_prime(k)
get_ranges(a)
                


