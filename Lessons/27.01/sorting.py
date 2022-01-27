import random
l=[4,2,8,5,-100,1,5,4,8,-45]
# l.sort()
# l = l[::-1]
# print(l)

# print(sorted([1,2,3,4,0]))

for j in range(len(l)-1):
    print(l)
    # for i in range(len(l)):
    for i in range(len(l)-j-1):
        if (l[i]>l[i+1]):
            l[i+1], l[i] = l[i], l[i+1]

print(l)

#random.shuffle(l)

print(l)
for i in range(len(l)):
    min, current = i, i+1
    while current < len(l):
        if l[current] < l[min]:
            min = current
        current += 1
    l[i], l[min] = l[min], l[i]
    print(l)
print(l)
    