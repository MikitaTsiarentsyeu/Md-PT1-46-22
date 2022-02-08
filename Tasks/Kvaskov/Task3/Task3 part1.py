MyDict1 = {}
MyDict2 = {}
sep = " "
j = 0
n = 0

UserString1 = str(input("Input same string, the number of elements of the string is at least 10   ").strip().replace(" ",""))
NumberOfElements = int(input("Enter the number of output for repeating elements, output starts at max reps "))

UserString1 = sep.join(UserString1)
UserStringEdit = UserString1.split(" ")
UserStringEdit.sort()
UserStringEdit1 = UserStringEdit

for x1 in UserStringEdit:
    if UserStringEdit1[0] == UserStringEdit[1]:
        member = UserStringEdit1.pop(0)
        UserStringEdit1.append(member)
        j += 1
        MyDict1[UserStringEdit1[0]] = j + 1 
    else:
        j = 0
        MyDict2[UserStringEdit1[0]] = 1
        member = UserStringEdit1.pop(0)
        UserStringEdit1.append(member)           
MyDict3 = {**MyDict2, **MyDict1}

List_MyDict3 = list(MyDict3.items())
List_MyDict3.sort(key = lambda i: i[1])
List_MyDict3.reverse()
for n in range(NumberOfElements):
    print(f" element = {List_MyDict3[n][0]} repeats {List_MyDict3[n][1]} time ")
    n += 1


      