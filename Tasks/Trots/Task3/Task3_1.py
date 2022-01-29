check_string = input("Enter the string: ")
n = int(input("Enter the required number of items to display: "))

count ={}

for i in check_string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

list_count = (list(count.items()))
list_count.sort(key = lambda i: i[1], reverse = True)

print(f"The string: {check_string}")

if 0 < n <= len(list_count):
    print(f"Elements: {n}")
    for j in range(n):
        print(f"'{list_count[j][0]}' meets in the string {list_count[j][1]} times")
else:
    print(f"Bro, we have only {len(list_count)} different elements, here they are:")
    for l in range(len(list_count)):
        print(f"'{list_count[l][0]}' meets in the string {list_count[l][1]} times")

