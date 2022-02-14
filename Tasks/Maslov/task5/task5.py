import random

def check_str(a):
    bol = 0
    mal = 0
    for i in a:
        if i.isupper():
            bol += 1
        elif i.islower():
            mal += 1
    return bol, mal
a = ('The quick Brow Fox')
print(check_str(a))   
def is_prime(k):
    
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True
print(is_prime(int(input())))
def get_ranges():
    b=[]
    for i in range(10):
        r = random.randint(1, 50)
        if r not in b:
            b.append(r)
    return sorted(b)


print(get_ranges())
  


