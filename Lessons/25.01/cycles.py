# while True:
#     print("infinity!!!")


x = 0
# while x <= 10:
#     print(x)
#     x += 1

# x = -10
# while x <= 0:
#     print(x)
#     x += 1

# flag = True

# while True:
#     if not flag:
#         flag = not flag
#         x += 1
#         continue
#     print(x)
#     x += 1
#     flag = not flag
#     if x == 11:
#         break

l = [1,2,3,4,5,6,7,8,9.0,"test"]

for i in l:
    if i == 3:
        continue
    # if i == 7:
    #     break
    print(i)
else:
    print("this is else")

for i in set("some string"):
    print(i)

d = {1:"one", 2:"two", 3:"three"}
for i in d:
    print(i, d[i])

for k, v in d.items():
    print(k, v)

for i in d.values():
    print(i)

for i in l:
    # l.append(i)
    print(i)
    print(l.pop())
    print(l)
    # if len(l) == 100:
    #     break

x = 0
indexes = []
while x <= len(l) - 1:
    # l.pop()
    if x%2 == 0:
        indexes.append(x)
    print(l[x])
    x += 1

for i in indexes[::-1]:
    del l[i]

print(l)

for i in range(0,10,3):
    print(i)

l = [1,2,3,4,5]
for i in range(len(l)):
    print(l[i])

for i, e in enumerate("some string"):
    print(i, e)

l = [[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    print(i)
    for j in i:
        print(j)