while True:

    a = input("Enter the number of symbols in the string. It cannot be less than 36: ")    

    if not a.isdigit():
        print("The value is not a number or is not integer")
        continue

    a = int(a)

    if a < 36:
        print("incorrect value. The number cannot be less than 36")
        continue
    
    break

with open("text.txt", 'r', encoding= "utf8") as f:
    line = f.readlines()
    with open("text_new.txt", 'w', encoding= "utf8") as f:             
        res = ""
        count = 0         
        for i in line:
            for l in i.split():                 
                end_count = count + len(l)
                if count != 0:
                    end_count +=1
                if end_count > a:                                                 
                    res += "\n"                    
                    count = 0
                if count !=0:
                    res += " "
                    count += 1
                res += l
                count += len(l) 
        res1 = res.split("\n")                
        for j in res1:
            prob = j.count(" ")            
            if len(j) < a and prob !=0:              
                cel = (a-len(j))//prob
                ost = (a-len(j))%prob
                if cel > 0:
                    j = j.replace(" ",(" ")+(" ")*cel)                    
                if ost > 0:	
                    j = j.replace((" ")+(" ")*cel,(" ")+(" ")*cel+(" "),ost)                    
            j = j +"\n"                           
            f.writelines(j)        
print("The result is in a new file 'text_new.txt'")
          
          
        




          

       
        
    
        
