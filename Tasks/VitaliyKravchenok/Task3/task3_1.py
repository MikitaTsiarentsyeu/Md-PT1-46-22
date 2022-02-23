text = input('Please, enter your string: ')
num = int(input('Enter the number of elements: '))

elements = {}

for char in text:
    if char not in elements:
        elements[char] = 1
    else:
        elements[char]+=1

l = [[k,v] for k,v in elements.items()]

for i in range(1,len(l)):
    for j in range(i,0,-1):
        if l[j][1]>l[j-1][1]:
            l[j], l[j-1] = l[j-1], l[j]
        else:
            break

if num > len(l):
    num = len(l)
    print(f'The number of elements that you\'d like to see exceeds the number of them in the string. {len(l)} elements are displayed')

for letter in range(num):
    print(f'{l[letter][0]} is used {l[letter][1]} times')



