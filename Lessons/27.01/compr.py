l = [x for x in range(10)]
print(l)

l = [x for x in range(10) if x%2 == 0]
print(l)

l = [x for x in range(100) if x%2 == 0 if x%5 == 0]
print(l)

l = [x**2 for x in range(100) if x%2 == 0 if x%5 == 0]
print(l)

l = []
for x in range(10):
    if x%2 == 0:
        if x%5 == 0:
            l.append(x**2)

d = {0:"zero", 1:"one"}
l = [v for k, v in d.items()] #list(d.values())
print(l)

l1 = [1,2,3,4,5,6,7]
l2 = [0,1,2,3]
l = [x**y for x in l1 for y in l2]
print(l)

l=[]
for x in l1:
    for y in l2:
        l.append(x**y)

l = [[1,2,3],[4,5,6],[7,8,9]]
l = [y for x in l for y in x]
print(l)

d = {x:str(x) for x in l}
print(d)

d = {x:x**2 for x in l}
print(d)