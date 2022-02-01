from collections import Counter
text = input("Enter any text, we will find the most repeated words:")
number = int(input("Enter how many words I need to check for repetition: "))

words = sorted(text.split(), key=str.lower)
a = {i:words.count(i) for i in set(words)}
li = list(a.items())
li.sort(key = lambda i: i[1])
if 0 < number <= len(li):
    print(f"Elements: {number}")
L = len(li)
li_2 = li[L-number:L]
for i in li_2:
    print(i[0], "встречается", i[1], "раза")
