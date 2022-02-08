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
#print(list)

line = ''
result = open('result.txt', 'w')
for word in list:
    if len(line) + 1 + len(word) < h:
        if len(line) != 0:
            line += ' ' + word
        else:
            line += word
    else:
        # print(line)
        result.writelines(line + '\n')
        line = ''
result.close()
