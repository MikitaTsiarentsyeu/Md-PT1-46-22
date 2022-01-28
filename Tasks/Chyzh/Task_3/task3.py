


input("Enter string consist of different letters more than 3 symbols length: ", s)
while len(s) <= 3:
    s = input("Enter string consist of different letters more than 3 symbols length: ")
l = list(s)
print(l)

for i in l:
    if i == " ":
        l.remove(i)
print([l[i] for i in range(len(l)) if not i == l.index(l[i])])