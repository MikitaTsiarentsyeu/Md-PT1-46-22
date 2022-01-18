l = []
print(id(l))
l = [1,2,3,4,5,6,7,8,9,"0", []]
print(id(l))
print(l, type(l), len(l))

# l = list("my test str")
# print(l)

print([1,2,3]+[1,2,3])
print([1,2,3]*10)

print(l[1])
print(l[2:8:2])
print(l[::-1])

l[0] = 1.0
print(l)

l.append("new elem")
print(l)

l.extend("test")
#l.extend([1,2,3,4])
print(l)
print(id(l))

l.insert(0, "new first element")
print(l)

l.remove(3)
print(l)

print('t' in l)
print(1.0 in l)

l.remove('t')
print(l)

print(l.pop(), l)
print(l.pop(0), l)

del l[0]
print(l)

del l[0:8]
print(l)

#del l
l.clear()
print(l, id(l))

l1 = l2 = []
print(l1, l2)
l2.append(1)
print(l1, l2)
print(id(l1), id(l2))