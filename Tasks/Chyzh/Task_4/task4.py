


while True:
    S = int(input("Enter the number characters, equal or more than 35, to divide text in lines: ")) 
    if S < 35:
        print("Omg, you've been asked equal or more than 35!")
        continue
    if not isinstance(S, int):
        print("Integer please!")
        continue
    break

with open("text.txt", 'r', encoding= "utf-8") as f:
    line = f.readlines()
    with open("formatted_text.txt", 'w', encoding= "utf-8") as f:             
        res = ""
        count = 0         
        for i in line:
            for k in i.split():              
                fin_count = count + len(k)      
                if count != 0:
                    fin_count +=1
                    res += " "
                    count += 1
                res += k
                count += len(k) 
                if fin_count > S:                                                 
                    res += "\n"                    
                    count = 0
        res1 = res.split("\n")                
        for j in res1:
            space = j.count(" ")            #prob = space
            if len(j) < S and space !=0:              
                cel = (S-len(j))//space
                ost = (S-len(j))%space
                if cel > 0:
                    j = j.replace(" ",(" ")+(" ")*cel)                    
                if ost > 0:	
                    j = j.replace((" ")+(" ")*cel,(" ")+(" ")*cel+(" "),ost)                    
            j = j +"\n"                           
            f.writelines(j)  
                 
print("Check formatted_text.txt")