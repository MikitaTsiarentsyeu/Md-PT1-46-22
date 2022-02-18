
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


with open("text.txt", "r+") as donor:
    with open("correct.txt", "w+") as receiver:
        line = donor.read(number)
        while len(line):
            receiver.write(line+'\n')
            line = donor.read(number)
            

print("done")
