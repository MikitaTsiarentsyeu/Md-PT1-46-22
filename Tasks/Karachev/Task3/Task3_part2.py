from collections import Counter

s = str(input("Write your random text: "))
x = int(input("Write number of words: "))

symb = ["!", "(", ")", "/", ".", ",", "`", "-", "_", "?", "<",">", "@", "#", "$", "%", "[", "]","{", "}", "*", "^", ":", ";"]

for i in symb:
    if i in s:
        s = s.replace(i,'')

s = s.lower()
s = s.split()
s = sorted(s)
s = Counter(s)

r = dict(s.most_common(x))

for i in r:
    print(f"Word '{i}' occurs {r[i]} times")
