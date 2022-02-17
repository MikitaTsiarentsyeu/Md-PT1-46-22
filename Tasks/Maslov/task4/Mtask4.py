
while True:
    a = input('Введите максимальное количество символов в строке ,минимальное 35 :  ')

    if a.isdigit():
        a = int(a)
        if a < 35:
            print('минимальное 35')
            continue
    break

with open('test.py.txt', 'r', encoding='utf-8') as f:
   file = []

with open('text.txt','r',encoding='utf8') as text:
    for i in text:
        i = i.split()
        for j in i:
            file.append(j)
    print(file)
with open('correct.txt','w',encoding='utf8') as finish: 
    placeholder =''
    for j in file:
        while len(placeholder) + len(j+j) != a:
            placeholder += ' ' + j
            if len(placeholder)== a:
                placeholder +='\n'
            else:
                finish.writelines(placeholder+'\n')