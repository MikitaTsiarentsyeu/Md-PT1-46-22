# Написать программу для поиска наиболее часто встречающихся элементов в строке.
# Пользователь вводит строку, и количество элементов, которые он хотел бы увидеть в ответе.
# Строка:lkseropewdssafsdfafkpwe

x = list(input("Please enter text:"))

#x = list("lkseropewdssafsd fafk1pwe")

d = {i : x.count(i) for i in x}

sorted_values = sorted(d.values())[::-1]
sorted_d = {}

for i in sorted_values:
    for k in d.keys():
        if d[k] == i:
           sorted_d[k] =d[k] 

y = int(input("Please enter the number of items: ")) 
for i in sorted_d:
    print(f"'{i}' встречается {d[i]} раз(а)")




