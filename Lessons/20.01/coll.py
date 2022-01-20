t = (1,2,3,4,5,6,7,8,9,0,"test",[])
print(type(t), t)

x = (1,)
print(type(x))

print(t[0], ((1,2,3)+(4,5,6))*3)

print(t[2:7:2])

# t[0] = 1.0 #ERROR!

print(len(t))
print(t.index("test"))

del t



d = {}
print(d, type(d))

d = {"one":1, "two":2, 3:"three"}
print(d)
print(d["one"], d[3])

# {[]:"test"} #ERROR
d = {1:"one", 1:"two"}
print(d[1])

d[1] = "one"
d[1] = 1.0

d["test"] = "test"
print(d)

print(d.keys())
print(d.values())
print(list(d.items())[0])

d[1] == d.get(1, "not found")

#print(d.pop(1), d)
print(d.popitem(), d)


s = {1,3,5}
print(s, type(s))

s = {1,1,1,1,1,1,1,1,1,1,1,1,1,1}
print(s)

s = set()
print(type(s))

l = [1,2,3,3,4,4,5,5,6,7]
l = list(set(l))
print(l)

l1=[1,2,3]
l2=[3,2,1]
print(l1==l2, set(l1)==set(l2))

#{1,2,3,["test"]} ERROR

print({"one", 837777823741809134})

s = {1,2,3,4,5,6}
s.add(1)
s.add(7)
print(s)

s.update([4,5,6,7,8])
print(s)

s.remove(7)
print(s)

#s.remove(7) ERROR
s.discard(7)
print(s)

print(s.pop(), s)
print(s.pop(), s)
print(s.pop(), s)

s.clear()

print({1,2,3}.union({3,4,5}))
print({1,2,3,4}.intersection({3,4,5}))

print({1,2,3}.issubset({0,1,2,3,4}))

l = [[1,2,3],(4,5,6),{7,8,9}]
l = [[1,2,3],[4,5,6],[7,8,9]]

print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

t = (l, "test")
t[0][0][0] = 1.0
print(t, l)

d = {(1,2,3):"one, two, three"}
print(d)
#d[t] = "some list" ERROR
#d = {t: "test"} ERROR