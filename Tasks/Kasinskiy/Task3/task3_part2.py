user_text = input("Enter your text: ")
el = int(input("Enter the number of elements: "))
for i in user_text:
    if i.isalpha() == False:
        user_text = user_text.replace(i, ' ')
user_text = user_text.lower()
user_text = user_text.split()
user_list=list({i:user_text.count(i) for i in user_text}.items())
print(user_list)
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

        elif user_list[i][1] == max_val:
            if user_list[i][0] < user_list[j][0]:
                max_val = user_list[i][1]
                j = i

    print(f"'{user_list[j][0]}' occurs {user_list[j][1]} times in your text")
    user_list.pop(j)
    n += 1



