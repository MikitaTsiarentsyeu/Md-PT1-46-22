
#The Python Software Foundation (PSF) is a 501 non-profit corporation that holds the intellectual property rights behind the Python programming language. We manage the open source licensing for Python version 2.1 and later and own and protect the trademarks associated with Python. We also run the North American PyCon conference annually, support other Python conferences around the world, and fund Python related development with our grants program and by funding special projects.

from re import M


MyDict1 = {}
MyDict2 = {}
MyDict3 = {}
MyDict5 = {}
List_MyDict2 = []
List_MyDict3 = []
List_MyDict4 = []
List_MyDict5 = []
List_MyDictEdit = []
Tuple1 = tuple()
Tuple2 = tuple()
markers = '''!()-[]{};?@#$%:'"\,./^&;*_'''
j = 0
n = 0
k = 0
i = 0
z = 0
x = 0
UserString1 = str(input("Enter some text including punctuation marks\n").strip())
NumberOfElements = int(input("Enter the number of output for repeating elements, output starts at max reps\n"))
for x2 in markers:
    UserString1 = UserString1.replace(x2, '')
print(UserString1)
UserString1 = UserString1.lower()
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

for k in MyDict1:
    if k in MyDict2:
        del MyDict2[k]

MyDict2.update(MyDict1)

print(MyDict2)
      
List_MyDict1 = list(MyDict2.items())
List_MyDict1.sort(key = lambda i: i[1])
List_MyDict1.reverse()
print(List_MyDict1)
List_MyDictEdit.extend(List_MyDict1)

#List_MyDict4 = list(MyDict2.items())
#List_MyDict4.sort()
# List_MyDict5 = List_MyDict3 + List_MyDict4

for m in range(NumberOfElements):
    print(f" element = {List_MyDict1[m][0]} repeats {List_MyDict1[m][1]} time ")

#for m in range(len(List_MyDict1)):
#    if List_MyDict1[0][1] == List_MyDict1[m + 1][1] and len(List_MyDict1 - m) in List_MyDict1:
#        List_MyDict2.append(List_MyDict1[m])
#        Tuple1 = List_MyDict1.pop(m)
#        List_MyDict1.append(Tuple1)
        
        
        
    
 #       member1 = List_MyDictEdit.pop(i)
 #       List_MyDictEdit.append(member1)
    
            
        
    





#for n in range(NumberOfElements):
#    print(f" element = {List_MyDict5[n][0]} repeats {List_MyDict5[n][1]} time ")

#List_MyDict4 = []
#List_MyDict5 = []
#for n in range(len(MyDict3)):
#    if List_MyDict3[n][1] == List_MyDict3[n + 1][1]:    
#        List_MyDict4.append(List_MyDict3[n])
#        List_MyDict4.append(List_MyDict3[n + 1])
#        List_MyDict3.pop(n + 1)
#       List_MyDict4.sort()
#        print(f" element = {List_MyDict4[0][0]} repeats {k} time ")
#        del List_MyDict4[0][0]          
#    else:
#       List_MyDict5.append(List_MyDict3[n])
#print(f" element = {List_MyDict4[n][0]} repeats {List_MyDict4[n][1]} time ")

    
    

    