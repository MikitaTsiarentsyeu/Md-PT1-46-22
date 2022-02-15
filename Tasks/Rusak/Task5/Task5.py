# №1 Check letters in a string
def check_str(any_str):
    up_count = 0
    low_count = 0
    for i in any_str:
        if i.isupper() == True:
            up_count += 1
        elif i.islower() == True:
            low_count += 1
    return f'{up_count} upper case, {low_count} lower case'

# №2 Is it a prime number?
def is_prime(num):
    if num==2 or num==3: return True
    if num%2==0 or num<2: return False
    for i in range(3, int(num**0.5)+1, 2):
        if num%i==0:
            return False
    return True

# №3 Get ranges
def get_ranges(any_list):
    out_str = ''
    x = any_list[0]
    y = 0
    for i in range(1, len(any_list)-1):
        if any_list[i] != any_list[i-1]+1 and any_list[i] == any_list[i+1]-1:
            x = any_list[i]
        elif any_list[i] == any_list[i-1]+1 and any_list[i] != any_list[i+1]-1:
            y = any_list[i]
            out_str += f'{x}-{y}, '
        elif any_list[i] != any_list[i-1]+1 and any_list[i] != any_list[i+1]-1:
            out_str += f'{any_list[i]}, '
    out_str += f'{any_list[len(any_list)-1]}'
    return out_str
