import sys


s = 1
s1 = 0
b = 0
d = 0
d1 = 0
k = 0
lenLast = 0
markers = """!,:;.?- - """
result1 = []
counter1 = 0
LenOfFile1 = 0
User_Input = int(input("enter the number of characters, number of characters must be bigger than 35 = "))

if User_Input < 35:
   print(" Your input is not correct")
   sys.exit()
    
with open('Text1.txt', 'r', encoding='utf-8') as f:
        LenOfFile = len(f.read())
f.close()
with open('Text1.txt', 'r', encoding='utf-8') as f:
    while LenOfFile + counter1 >= LenOfFile1:  
        for n in range(User_Input - b):
            MyLine2 = f.read(1)
            result1.append(MyLine2)
        if (result1[-1] == ' ' or result1[-1] == markers or result1[-1] == ''):
           result = "".join(result1)
           ListResult = result.split()
           del result1[0:]            
           with open ('Text1Edit.txt', 'a', encoding='utf-8') as f1:
                f1.write(result + '\n',  )
        else:
            result = "".join(result1) #
            ListResult = result.split()
            lenLine = len(ListResult)
            lenLast = ListResult.pop(lenLine - 1)
            counter1 += len(lenLast) + 2
            result = " ".join(ListResult)
            for j in range((User_Input - len(result)) + (lenLine - 2)):
                ListResult.insert(s, " ")
                s += 2 + s1
                k += 1
                if k >= lenLine - 2:
                    s = 1                        
                    k = 0
                    s1 += 1          
            result = "".join(ListResult)
            with open ('Text1Edit.txt', 'a', encoding='utf-8') as f1:
                 f1.write(result + '\n')
            del result1[0:]
            result1.append(lenLast)
            d = " ".join(result1)
            d1 = " ".join(d)
            result1 = d1.split()
            b = len(d)
            s = 1
            k = 0
            s1 = 0 
        with open ('Text1Edit.txt', 'r', encoding='utf-8') as f1:
            LenOfFile1 = len(f1.read())
            if LenOfFile1 >= LenOfFile + counter1:
                break
            f1.close()
    with open ('Text1Edit.txt', 'a', encoding='utf-8') as f1:
        f1.write("\ndecoding is done, thank you")          
                    
    print(result)

       

     
          

    


