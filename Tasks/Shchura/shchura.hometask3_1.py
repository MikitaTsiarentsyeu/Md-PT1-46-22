#program to calculate top elements in string
str = input("Please, enter your string:")
number = input("Please, enter how many top elements to identify:")
while not number.isnumeric():
    number = input("Incorrect value, enter number:")
number = int(number)
dict = {}
for i in str:
    if i not in dict.keys():
        dict[i] = 1
    else: 
        dict[i] += 1
new_dict = {}
for i in dict:
    if dict[i] in new_dict.keys():
        new_dict[dict[i]].append(i)
    else:
        new_dict[dict[i]] = [i]
new_dict_keys = sorted(new_dict, reverse=True)
if number in range(len(new_dict_keys)):
    for i in new_dict_keys[:number]:
        print(f"{new_dict[i]} встречается {i} раза")
else:
    print("The number of top elements is out of the actual range. Available top elements are:")
    for i in new_dict_keys:
        print(f"{new_dict[i]} встречается {i} раза")