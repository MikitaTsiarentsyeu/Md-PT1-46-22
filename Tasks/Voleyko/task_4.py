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

def align_string(line):
    x = line.split()
    needed_space = number - len(line)
    words_count = len(x[0:-1])
    n_of_space_between_words = needed_space//words_count
    a = (' '*n_of_space_between_words + ' ').join(x)
    if len(a) ==number:
        return a
    else:
        different = number - len(a)
        count = 0
        for i in range(len(a)-1):
            if len(a)<number and count != different :
                x[i]+=' '
                count+=1
            else: #len(a)==number and count ==needed_space:
                break
                
    return ' '.join(x)
    
with open("text.txt", "r+") as donor:
    with open("correct.txt", "w+") as receiver:
        string = donor.read(number)
        while len(string):
            elements = list(string)
            if elements[-1]is [' ']:
                receiver.write(string+'\n')
                string = donor.read(number)  
            elif elements[-1] is not[' ']:
                new_string = string.split()
                len_last_word = len(list(new_string[-1]))
                line = align_string(''.join(elements[:-(len_last_word+1)]))
                
                receiver.write(line+'\n'+''.join(new_string[-1]))
                string = donor.read(number-len_last_word)
                

print("done")

