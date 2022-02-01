
# Написать программу для поиска наиболее часто встречающихся слов в тексте.
# Пользователь вводит текст, и количество элементов, которые он хотел бы увидеть в ответе.
# При совпадении частоты использования, слова должны выводиться в алфавитном порядке.
# The Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund Python related development with our grants program and by funding special projects.

x = str(input("Please enter text:"))

x = x.lower()

x = x.replace(',','')
x = x.replace('.','')
x = x.replace(')','')
x = x.replace('(','')

x = x.split()


for k, v in enumerate(x):
    #print(k,v)

    d = {v : x.count(v) for v in x}

#for k, v in d.items():
    #print(k,v)

sorted_values = sorted(d.values())[::-1]
sorted_d = {}

for i in sorted_values:
    for k in sorted(d.keys()):
        if d[k] == i:
           sorted_d[k] =d[k] 


y = int(input("Please enter the number of items: ")) 

for i in sorted_d:
    print(f"'{i}' встречается {d[i]} раз(а)")






