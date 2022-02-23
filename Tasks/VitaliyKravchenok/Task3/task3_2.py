text = input('Please, enter your text: ')
num = int(input('Enter the number of words to show: '))
text_low = text.lower()
punct_marks = "!()-[]\{\};?@#$%:'\"\,./^&;*_"

for i in text_low:
    if i in punct_marks:
        text_low = text_low.replace(i, '')

l = [i for i in text_low.split() if not i.isdigit()]

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
            
dict_words = {}

for word in l:
    if word not in dict_words:
        dict_words[word] = 1
    else:
        dict_words[word]+=1

words = [[k,v] for k,v in dict_words.items()]


for i in range(1,len(words)):
    for j in range(i,0,-1):
        if words[j][1]>words[j-1][1]:
            words[j], words[j-1] = words[j-1], words[j]
        else:
            break

if num > len(words):
    num = len(words)
    print(f'The number of words that you\'d like to see exceeds the number of them in the text. {len(words)} elements are displayed')
for elem in range(num):
    print(f'{words[elem][0]} is used {words[elem][1]} times')