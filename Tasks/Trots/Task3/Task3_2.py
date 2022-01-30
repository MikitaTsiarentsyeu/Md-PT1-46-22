#!/usr/bin/env python3

check_text = input("Enter the text: ")

n = str(input("Enter the required number of words to display: ")).strip()
while not n.isdigit():
    n = str(input("Please enter a numeric value: ")).strip()

list_words = ((''.join(e for e in check_text if (e.isalpha() or e == " "))).lower()).split(" ")
n = int(n)
count = {}

for i in list_words:
    if i == "":
        continue
    elif i in count:
        count[i] += 1
    else:
        count[i] = 1

list_count = (list(count.items()))
list_count.sort(key=lambda y: (-y[1], y[0]))

print(f"The text: {check_text}")

if 0 < n <= len(list_count):
    print(f"Words: {n}")
    for j in range(n):
        print(f"'{list_count[j][0]}' meets in the text {list_count[j][1]} times")
else:
    print(f"Bro, we have only {len(list_count)} different words in the text, here they are:")
    for x in range(len(list_count)):
        print(f"'{list_count[x][0]}' meets in the text {list_count[x][1]} times")
