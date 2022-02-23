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
        reading_str = donor.read(number)
        #print(reading_str)
        str_elem = list(reading_str)
        while len(reading_str):
            if str_elem[-1]==' ':
                receiver.write(reading_str+'\n')
                reading_str = donor.read(number)
            elif str_elem[-1]!=' ':
                str_words = reading_str.split()
                #len_last_items=len(str_words[-1])
                new_str =' '.join(str_words[:-1])
                last_check = len(new_str)
                if last_check == number:
                    receiver.write(new_str+'\n'+ ''.join(str_words[-1]))
                    reading_str = donor.read(number - len(str_words[-1]))
                else:
                    #number_of_space = number - last_check
                    add_space = new_str.split()
                    for words in add_space:
                        if last_check!=number:
                            words+=' ' 
                        else:
                            break    
                    receiver.write(' '.join(add_space)+'\n'+''.join(str_words[-1]))
                    reading_str = donor.read(number)
                    #reading_str = donor.read(number - len(str_words[-1]))

print("done")

