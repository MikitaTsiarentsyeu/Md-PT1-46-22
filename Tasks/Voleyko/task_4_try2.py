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
    with open("correct2.txt", "w+") as receiver:
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
                    number_of_space = number - last_check
                    count = 0
                    check = number_of_space//len(str_words[:-1])
                    if check<1:
                        for i in range(len(new_str)-1):
                            if count < number_of_space :
                                str_words[i]+=' '
                                count+=1
                            else: 
                                break
                        receiver.write(' '.join(str_words[:-1])+'\n'+''.join(str_words[-1]))
                        reading_str = donor.read(number- len(list(str_words[-1])))
                    else:
                        receiver.write((' '*check+' ').join(str_words[:-1])+'\n'+''.join(str_words[-1]))
                        reading_str = donor.read(number- len(list(str_words[-1])))
                            

print("done")

