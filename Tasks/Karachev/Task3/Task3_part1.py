from collections import Counter

s = str(input("Write your random string: "))
x = int(input("Write number of elements: "))

s = Counter(s)

r = dict(s.most_common(x))

for i in r:
    print(f"Element '{i}' occurs {r[i]} times") 
        