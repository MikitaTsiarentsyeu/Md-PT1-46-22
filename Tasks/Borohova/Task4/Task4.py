while True:
    h = (input("Введите кол-во символов:"))

    if h.isdigit():
        h = int(h)
        if h <= 35:
            print("Введите число больше 35")
            continue
    else:
        print("Неверный формат ввода, введите число")
        continue

    break
# print(h)

list = []

with open("text.txt", 'r') as f:
    for l in f:
        f1 = l.split()
        for i in f1:
            list.append(i)
# print(list)

line = ''
result = open('result.txt', 'w')

for word in list:
    if len(line) + 1 + len(word) <= h:
        if len(line) != 0:
            line += ' ' + word
        else:
            line += word
    else:
        res = ''
        a = h - len(line)
        if a == 0:
            res = line
        else:
            l1 = [x for x in line.split()]
            w = len(l1)
            if w == 1:
                res = l1[0]
            a += (w - 1)
            spaces = a // (w - 1)
            spaces1 = a % (w - 1)
            res = ''
            for x in l1:
                res += x + spaces * ' '
                if spaces1 > 0:
                    res += ' '
                    spaces1 -= 1
        line = res
        result.writelines(line + '\n')
        line = word
if len(line) > 0:
    result.writelines(line)
result.close()
