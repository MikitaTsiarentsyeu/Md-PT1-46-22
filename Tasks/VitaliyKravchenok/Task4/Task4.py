while True:

    len_string = input("Input the length of the string, its value must not be less than 35: ")    

    if not len_string.isdigit():
        print("Incorrect input! Please, input digit value!")
        continue

    len_string = int(len_string)

    if len_string < 35:
        print("Incorrect input! Please, input digit value not less than 35!")
        continue

    break

with open("text.txt", 'r', encoding= "utf8-r") as f:
    rline = f.readlines()
    with open("new_text.txt", 'w', encoding= "utf8-r") as f:             
        line = ""
        count = 0         
        for i in rline:
            for b in i.split():                 
                end_count = count + len(b)
                if count != 0:
                    end_count +=1
                if end_count > len_string:                                                 
                    line += "\n"                    
                    count = 0
                if count !=0:
                    line += " "
                    count += 1
                line += b
                count += len(b) 
        edit_line = line.split("\n")                
        for j in edit_line:
            space = j.count(" ")            
            if len(j) < len_string and space != 0:              
                integral = (len_string-len(j))//space
                rem = (len_string-len(j))%space
                if integral > 0:
                    j = j.replace(" ",(" ")+(" ")*integral)                    
                if rem > 0:	
                    j = j.replace((" ")+(" ")*integral,(" ")+(" ")*integral+(" "),rem)                    
            j = j +"\n"                           
            f.writelines(j)        
print("The text is written to a new file 'new_text.txt")