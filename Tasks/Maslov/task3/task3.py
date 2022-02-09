from collections import Counter

a = Counter(input('Введите слова : '))
b = int(input('Введите сколько хотите резултатов видеть : '))
c = Counter(a).most_common(b)
if len(c) < b:
    print(f'Ограниченное количество')
for d in c:
    print(f'{d[0]} повторяется {d[1]} раз(раза)')


from collections import Counter

a = input()
b = []
for i in a.split():
    c = ''
    c += i.lower()
    b.append(c)
print(Counter(b))
