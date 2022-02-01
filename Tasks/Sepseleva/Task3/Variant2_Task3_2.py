#Task 3_2 without sorted()
#Check, please, if you have time
text = input('Please, enter your text: ')
num = int(input('Enter the number of words to show: '))
text1 = text.lower()
punctuation_marks = "!()-[]\{\};?@#$%:'\"\,./^&;*_"

for i in text1:
    if i in punctuation_marks:
        text1 = text1.replace(i, '')

l = [i for i in text1.split() if not i.isdigit()]

#It looks terrible but couldn't come up with a better idea without sorted() and functions in general
#sorting in alphabetical order 
flag = True
while flag:
    flag = False
    for i in range(len(l)-1):
        for j in range(min(len(l[i]), len(l[i+1]))):
            if l[i][j]>l[i+1][j]:
                l[i], l[i+1] = l[i+1], l[i]
                flag = True
                break
            elif l[i][j]<l[i+1][j]:
                break
            
#counting the number of words in the text
words_dict = {}

for word in l:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word]+=1

words = [[k,v] for k,v in words_dict.items()]


#Sorting numbers

for i in range(1,len(words)):
    for j in range(i,0,-1):
        if words[j][1]>words[j-1][1]:
            words[j], words[j-1] = words[j-1], words[j]
        else:
            break

#Displaying the data to the user

if num > len(words):
    num = len(words)
    print(f'The number of words that you\'d like to see exceeds the number of them in the text. {len(words)} elements are displayed')
for elem in range(num):
    print(f'{words[elem][0]} is used {words[elem][1]} times')