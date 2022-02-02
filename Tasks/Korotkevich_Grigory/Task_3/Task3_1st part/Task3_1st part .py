from collections import Counter
elements = input("Write any line and I will find the most repeated character: ")
number = int(input("Enter a number and you will see the same number of items: "))
count = {}
for i in elements:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
list_d = (list(count.items()))
list_d.sort(key=lambda y: y[1], reverse=True)

if 0 < number <= len(list_d):
    print(f"Elements: {number}")
    for j in range(number):
        print(f"'{list_d[j][0]}' repeats  {list_d[j][1]} times")
