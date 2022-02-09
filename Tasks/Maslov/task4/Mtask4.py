
with open('mtext.txt', 'r', encoding='utf-8') as f:
    f = f.readlines()
    print(f)

while True:
    a = input('Введите максимальное количество символов в строке ,минимальное 35 :  ')

    if a.isdigit():
        a = int(a)
        if a < 35:
            print('минимальное 35')
            continue
    break
   
a = int(input('Введите максимальное количество символов в строке ,минимальное 35 :  '))

b = ""
c = 0
for i in f:
    for j in i.split():
        d = c + len(j)
        if c != 0:
            d += 1
        if d > a:
            b += '\n'
            c = 0
        if c != 0:
            b += ' '
            c += 1
        b += j
        c += len(j)
    print(b)