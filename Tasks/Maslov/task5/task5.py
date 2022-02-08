def check_str(a):
    bol = 0
    mal = 0
    for i in a:
        if i.isupper():
            bol += 1
        elif i.islower():
            mal += 1
    return bol, mal
   
def is_prime(): pass
def get_ranges():pass
a = ('The quick Brow Fox')
print(check_str(a))