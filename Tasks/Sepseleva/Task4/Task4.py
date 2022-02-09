#getting data from the user + validation
while True:
    chunk = input('Enter the number of symbols in a line that is more than 35: ')

    if not (chunk.isdigit()):
        print('Your input should contain only numbers. Try again')
        continue

    chunk = int(chunk) 

    if chunk < 35:
        print('Your value should be more than 35. Try again')
        continue

    break  

position = 0  #the position of the pointer in the file

#counting the number of symbols in a string
def count_length(l):
    length =len(' '.join(l)) 
    return length

#reading the contents 
with open('text.txt', 'r', encoding='utf-8') as text:
    with open('new_text.txt', 'a', encoding='utf-8') as copy:
        while True:
            part = text.read(chunk+1)
            if part:
                if len(part) < chunk:
                    line = part.split()
                elif part[-1] != ' ':
                    line = part.split()
                    del line[-1]
                else:
                    part = part[:-1]
                    line = part.split() 

                #setting position of the pointer in the file    
                position = position +  len(' '.join(line).encode())+1
                if '\n' in part[:-1]:
                    position+=1
                if part[0] == ' ':
                    position+=1
                text.seek(position)
                

                #adding spaces between the words
                if len(line) > 1:
                    while count_length(line)<chunk:
                        for i in range(len(line)-1):
                            if count_length(line)<chunk:
                                line[i]+=' '
                            else:
                                break
                        
                #appending the text to a new file
                new_line = ' '.join(line)
                copy.write(new_line + '\n')
            
            else: 
                break  
print('New file with the formatted text has been created.')              