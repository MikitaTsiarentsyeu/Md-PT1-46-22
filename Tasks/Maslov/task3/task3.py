from collections import Counter
a = Counter(input())
print(a)





from collections import Counter

a = input()
b = []
for i in a.split():
    c = ''
    c += i.lower()
    b.append(c)
print(Counter(b))