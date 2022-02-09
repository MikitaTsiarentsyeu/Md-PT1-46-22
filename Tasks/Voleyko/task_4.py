while True:
    number = input('Please, enter the number of items(Remember: min = 35!):\n')
    if not (number.isdigit()):
        print("incorrect input, the number values should be digits")
        continue
    number = int(number)
    if number >= 35:
        print('Ok, let\'s see!')
        break
    elif number < 35:
        print('Sorry, incorrect input!\nMin value = 35!')   
    else:
        print('incorrect input, please enter numbers!')  
    exit

file = []

with open('text.txt','r',encoding='utf8') as text:
    for i in text:
        i = i.split()
        for j in i:
            file.append(j)
    print(file)
with open('correct.txt','w',encoding='utf8') as finish: 
    placeholder =''
    for j in file:
        while len(placeholder) + len(j+j) != number:
            placeholder += ' '+ j
            if len(placeholder)==number:
                placeholder +='\n'
            else:
                finish.writelines(placeholder+'\n')