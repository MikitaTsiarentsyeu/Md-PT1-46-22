while True:

    User = input("Enter how many characters you want to see in a line. But there is a nuance, not less than 35: ")    

    if not User.isdigit():
        print("Please enter an integer!")
        continue

    User = int(User)

    if User < 35:
        print("You entered an invalid number, please try again!But remember, at least 35")
        continue

    break

with open("text.txt", 'r', encoding= "koi8-r") as f:
    line = f.readlines()
    with open("Your_text.txt", 'w', encoding= "koi8-r") as f:             
        res = ""
        count = 0         
        for i in line:
            for b in i.split():                 
                end_count = count + len(b)
                if count != 0:
                    end_count +=1
                if end_count > User:                                                 
                    res += "\n"                    
                    count = 0
                if count !=0:
                    res += " "
                    count += 1
                res += b
                count += len(b) 
        res1 = res.split("\n")                
        for j in res1:
            prob = j.count(" ")            
            if len(j) < User and prob !=0:              
                cel = (User-len(j))//prob
                ost = (User-len(j))%prob
                if cel > 0:
                    j = j.replace(" ",(" ")+(" ")*cel)                    
                if ost > 0:	
                    j = j.replace((" ")+(" ")*cel,(" ")+(" ")*cel+(" "),ost)                    
            j = j +"\n"                           
            f.writelines(j)        
print("All your shenanigans in the file:'Your_text.txt'")


