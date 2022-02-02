text = str(input('Введите текст:\t'))
text = text.lower()

for char in text:
    if not char.isalpha() and char != '-':
        text = text.replace(char, ' ')

list_text = text.split()

for i in list_text:
    if i=='':
        list_text[i].remove('')

text_dict = {} 
for i in list_text:
    if i in text_dict:
        text_dict[i] = text_dict[i] + 1
    else:
        text_dict[i] = 1

tup_list = list(text_dict.items())
tup_list.sort(key = lambda x: (-x[1], x[0]))

num = input('Введите необходимое количество отсортированных элементов:\t')
while not num.isdigit() or int(num) > len(tup_list):
    num = input(f'Неправильный ввод! Введите цифровое значение не более {len(tup_list)}:\t') 
       
num = int(num)
count = ''

for x in range(0, num):
    if 1 < tup_list[x][1] < 5  or 21 < tup_list[x][1] < 25 or 31 < tup_list[x][1] < 35:
        count = 'раза'
    else:
        count = 'раз'
    print(f'"{tup_list[x][0]}" встречается {tup_list[x][1]} {count}')
