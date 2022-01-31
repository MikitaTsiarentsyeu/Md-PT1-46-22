
from collections import Counter
s = input("Enter text: ")
N = int(input("Enter the number of words you want to check repeated: "))
if isinstance(N, int) == False:
    N = int(input("You can't use strings as numerical values: "))

s1 = s.lower()
words = s1.split(' ')
r = {i:words.count(i) for i in set(words)}
l = list(r.items())
l.sort(key = lambda i: i[1])
print(l)
L = len(l)
lmod = l[L-N:L]
for i in lmod:  
    print(i[0], "встречается", i[1], "раза")