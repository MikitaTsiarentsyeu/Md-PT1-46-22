#!/usr/bin/env python3

check_string = input("Enter the string: ")
n = str(input("Enter the required number of items to display: ")).strip()
while not n.isdigit():
    n = str(input("Please enter a numeric value: ")).strip()

n = int(n)
count = {}

for i in check_string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

list_count = (list(count.items()))
list_count.sort(key=lambda y: -y[1])

print(f"The string: {check_string}")

if 0 < n <= len(list_count):
    print(f"Elements: {n}")
    for j in range(n):
        print(f"'{list_count[j][0]}' meets in the string {list_count[j][1]} times")
else:
    print(f"Bro, we have only {len(list_count)} different elements, here they are:")
    for x in range(len(list_count)):
        print(f"'{list_count[x][0]}' meets in the string {list_count[x][1]} times")
