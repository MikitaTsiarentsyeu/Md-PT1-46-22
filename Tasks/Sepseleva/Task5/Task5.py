def check_str(s):
    lower = 0
    upper = 0
    for i in s:
        if i.isalpha():
            if i.isupper():
                upper+=1
            else:
                lower+=1
    return print(f'{upper} upper case, {lower} lower case')
   

def is_prime(n):
    if n in [2,3]:
        return True
    if n % 2 == 0 or n<=1:
        return False
    for i in range (3,int((n**0.5)+1),2):
        if n % i == 0:
            return False
    return True


def get_ranges(l):
    start = 0
    end = 0
    s = ''

    while start < len(l):
        if start == len(l)-1:
            s+=f'{l[-1]}'
            break
        elif end == len(l)-1:
            s += f'{l[start]}-{l[end]}'
            break
        else:
            for i in range(start,len(l)-1):
                if l [i+1] == l[i]+1:
                    end = i+1
                else:
                    if start == end:
                        s += f'{l[i]}, '
                    else:
                        s += f'{l[start]}-{l[end]}, '
                    start = i + 1 
                    end = i + 1    
                    break
    return s                


