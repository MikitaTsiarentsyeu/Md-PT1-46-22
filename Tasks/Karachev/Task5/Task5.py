
def check_str(l):          
    k = 0
    t = 0
    for i in l:               
        if i.islower():
            k+=1
        elif i.isupper():
            t+=1        
    return print(f"{t} upper case, {k} lower case")

check_str("The quick BrBBBow Fox") 

       

def is_prime(x):
    d = 2
    while x%d !=0:
      d+=1
    return  d == x

print(is_prime(11))


def get_ranges(l):    
    a = f"{l[0]}"
    flag = False        
    for i in range(len(l)-1):             
        if l[i+1]-l[i] == 1:
            flag = True            
        else:
            if flag:
               a += f"-{l[i]}, {l[i+1]}"
            else:
                a += f", {l[i+1]}"
            flag = False
    if flag:
        a += f"-{l[-1]}"

    return a
        
print(get_ranges([2, 5, 6, 7, 15, 18, 197]))