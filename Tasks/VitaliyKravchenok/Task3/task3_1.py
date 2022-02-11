#Task 3_1 but without sorted() (you said we'd better use this approach now to practise more.)
#Check, please, if you have time
text = input('Please, enter your string: ')
num = int(input('Enter the number of elements to show: '))

#Counting the characters in the given string

elems = {}

for char in text:
    if char not in elems:
        elems[char] = 1
    else:
        elems[char]+=1

#Sorting the elements in the list

l = [[k,v] for k,v in elems.items()]

for i in range(1,len(l)):
    for j in range(i,0,-1):
        if l[j][1]>l[j-1][1]:
            l[j], l[j-1] = l[j-1], l[j]
        else:
            break


#Displaying the info to the user
if num > len(l):
    num = len(l)
    print(f'The number of elements that you\'d like to see exceeds the number of them in the string. {len(l)} elements are displayed')

for letter in range(num):
    print(f'{l[letter][0]} is used {l[letter][1]} times')



