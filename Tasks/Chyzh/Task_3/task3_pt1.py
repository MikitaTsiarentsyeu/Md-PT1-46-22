s = input("Enter text: ")
while len(s) <= 3:
    s = input("Enter string consist of different letters more than 3 symbols length: ")
N = int(input("Enter the number of symbol you want to check repeated: "))
if (isinstance(N, int) == False) or N > len(s):
    N = int(input("You can't use strings as numerical values and number of indexed symbols can't be more than number of symbols in string: "))
    
for i in s:
    if i == " ":
        s.remove(i)
r = {i:s.count(i) for i in set(s)}

l = list(r.items())
l.sort(key=lambda i: i[1])
print(l)
L = len(l)
lmod = l[L-N:L]
for i in lmod:  
    print(i[0], "встречается", i[1], "раза")







