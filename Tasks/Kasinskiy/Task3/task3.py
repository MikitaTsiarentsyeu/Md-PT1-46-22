
user_string = input("Enter your string: ")
while user_string == '':
    user_string = input("Enter your string: ")

el = int(input("Enter the number of elements: "))

user_list = list({i:user_string.count(i) for i in user_string}.items())

if el > len(user_list):

    el = len(user_list)

n = 1

while n <= el:

    j = 0

    max_val = user_list[0][1]

    for i in range(1, len(user_list)):

        if user_list[i][1] > max_val:

            max_val = user_list[i][1]

            j = i

    print(f"'{user_list[j][0]}' occurs {user_list[j][1]} times in your string")

    user_list.pop(j)

    n += 1






