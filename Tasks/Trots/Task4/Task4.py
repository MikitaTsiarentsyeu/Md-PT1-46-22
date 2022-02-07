#!/usr/bin/env python3
while True:
    n = (input("Please enter the maximum number of characters per line(must be over 35): ")).strip()
    if n.isdigit():
        if int(n) > 35:
            n = int(n)
            break
        else:
            print("Input Error!!Value must be over 35! Try again!")
    else:
        print("Input Error!!Please, enter a numeric value!")
        
text = ""

with open("text2.txt", 'r', encoding="utf-8") as file:    
    for line in file:
        text += line

text_1 = '' 
c = 0  

for i in text.split():
    c += len(i)
    if c >= n:
        text_1 += '\n'
        c = len(i)
    elif text_1 != '':
        text_1 += ' '
        c += 1
    text_1 += i

text_Strings = text_1.splitlines()

for i in range(len(text_Strings)):
    spaces = len(text_Strings[i].split()) - 1
    symbols = list(text_Strings[i])
    while len(symbols) < n and spaces != 0:
        for j in range(len(symbols) + spaces):
            if symbols[j-1] == " ":
                continue
            if symbols[j] == " ":
                symbols.insert(j, " ")
            if (len(symbols) == n):
                break
    text_Strings[i] = "".join(symbols)

new_text = "\n".join(text_Strings)

with open("textformat.txt", 'w', encoding="utf-8") as file:
    file.write(new_text)
if file.closed:
    print("Bro, your formated text is ready! File name is textformat.txt")