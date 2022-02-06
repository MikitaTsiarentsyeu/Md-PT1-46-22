with open('text.py.txt', 'r+', encoding='utf-8') as f:
    s = f.readlines()
    print(s)
    
a = int(input('Введите максимальное количество символов в строке ,минимальное 35 :  '))
b = ""
c = 0
for i in s:
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
