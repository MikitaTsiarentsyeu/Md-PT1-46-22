line = str(input('Введите слово:\t'))
line = line.replace(' ', '')

dict_line = {}
for i in line:
    if i in dict_line:
        dict_line[i] += 1
    else:
        dict_line[i] = 1

list_dict = list(dict_line.items())
list_dict.sort(key = lambda x: [-x[1], x[0]])

num = input('Введите необходимое количество отсортированных элементов:\t')
while not num.isdigit() or int(num) > len(list_dict):
    num = input(f'Неправильный ввод! Введите цифровое значение не более {len(list_dict)}:\t') 
       
num = int(num)
count = ''

for x in range(0, num):
    if 1 < list_dict[x][1] < 5  or 21 < list_dict[x][1] < 25:
        count = 'раза'
    else:
        count = 'раз'
    print(f'"{list_dict[x][0]}" встречается {list_dict[x][1]} {count}')
