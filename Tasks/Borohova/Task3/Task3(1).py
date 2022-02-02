a = input("Введите строку:")
a1 = int(input("Введите кол-во элементов:"))

d = {}
sorted_dict = {}

for i in a:
    v = d.get(i, 0)
    d[i] = v + 1

d1 = sorted(d, key=d.get)

for y in d1:
    sorted_dict[y] = d[y]

while a1 > 0:
    item = sorted_dict.popitem()
    print("{} встречается {} раз".format(item[0], item[1]))
    a1 -= 1

    if len(sorted_dict) < 1:
        break
