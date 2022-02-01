from collections import Counter 
text = input('Please, enter your string: ')
num = int(input('Enter the number of elements to show: '))

elem_numbers = Counter(text).most_common(num)

if len(elem_numbers) < num:
    print(f'The number of elements that you\'d like to see exceeds the number of them in the string. {len(elem_numbers)} elements are displayed')

for elem in  elem_numbers:
    print(f'{elem[0]} is used {elem[1]} times')


