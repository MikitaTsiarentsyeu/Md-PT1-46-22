from collections import Counter
text = input('Please, enter your text: ')
num = int(input('Enter the number of words to show: '))
text1 = text.lower()
punctuation_marks = "!()-[]\{\};?@#$%:'\"\,./^&;*_"

#getting rid of punctuation marks

for i in text1:
    if i in punctuation_marks:
        text1 = text1.replace(i, '')

#counting the words
words = [i for i in text1.split() if not i.isdigit()] #getting rid of numbers 'cause they're not words
words =  sorted(words)
print(words)

number_words = Counter(words).most_common(num)
print(number_words)
#displaying the result

if len(number_words) < num:
     print(f'The number of words that you\'d like to see exceeds the number of them in the text. {len(number_words)} elements are displayed')
for i in number_words:
    print(f'{i[0]} is used {i[1]} times')

  