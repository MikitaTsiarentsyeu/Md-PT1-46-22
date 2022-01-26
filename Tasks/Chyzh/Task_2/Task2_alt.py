from datetime import datetime           # import class
ch = int(input("Choose mode: 1 - for automatical output of current time; 2 - to enter current time: "))    #choose the proper mode
if ch == 1:
    curTime = str(datetime.now().time())    # get current time as a string
    CT = list(curTime)[0:8]                 # turn string to list splitting milliseconds
    print("".join(CT))                      # output of current time as a string
elif ch == 2:
    usersCurTime = input("Enter current time in hh:mm format:")     #input of current time
    UCT = list(usersCurTime)
    print(UCT)
    hours = int(UCT[0] + UCT[1])
    minutes = int(UCT[3] + UCT[4])
    x = hours
    y = minutes
    # hours 1 case (<30), 2 case (half), 3 case (> 30 & <45) - case123list
    # hours 4 case (>=45 - till), 5 case (00 minutes) - case45list
    # minutes tillmin (>=45)
    timedict = {}
    case123list = ["первого", "второго", "третьего", "четвертого", "пятого", "шестого", "седьмого", "восьмого",
                "девятого", "десятого", "одиннадцатого", "двенадцатого"]
    case45list = ["час", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять",
            "одиннадцать", "двенадцать"]
    tillmin = ["пятнадцати", "четырнадцати", "тринадцати", "двенадцати", "одиннадцати", "десяти", "девяти", "восьми", 
            "семи", "шести", "пяти", "четырех", "трех", "двух", "одной"]
    minutes = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", 
            "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", 
            "девятнадцать", "двадцать", "двадцать одна", "двадцать две", "двадцать три", "двадцать четыре", "двадцать пять", 
            "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять"]
    minutes1 = ["тридцать одна", "тридцать две", "тридцать три", "тридцать четыре", "тридцать пять", "тридцать шесть", "тридцать семь", 
                "тридцать восемь", "тридцать девять", "сорок", "сорок одна", "сорок две", "сорок три", "сорок четыре"]

    if y >= 60 or x >= 24:
        print("Неверно введено время!")
    elif y == 0:
        if x == 1 or x == 13:
            print("час")
        elif x == 0 or (x >= 5 and x <= 12):
            print(case45list[x-1], "часов")
        elif x >=2 and x <=4:
            print(case45list[x-1], "часа")
        elif x >= 14 and x <=16:
            print(case45list[x-13], "часа")
        elif x >= 17 and x <= 23:
            print(case45list[x-13], "часов")
    elif y == 30:
        if x <= 12:
            print("Половина", case123list[x])
        elif x >=13 and x <= 23:
            print("Половина", case123list[x-12])
    elif y >=45:
        if x == 1 or x == 13:
            if y == 59:
                print("без", tillmin[y-60], "минуты","час")
            else:
                print("без", tillmin[y-60], "минут","час")
        elif x >=0 and x <=12:
            if y == 59:
                print("без", tillmin[y-60], "минуты", case45list[x])
            else:
                print("без", tillmin[y-60], "минут", case45list[x])
        elif x >12 and x <=23:
            if y == 59:
                print("без", tillmin[y-60], "минуты", case45list[x-12])
            else:
                print("без", tillmin[y-60], "минут", case45list[x-12])
    elif y > 0 and y < 30:
        if y == 1 or y == 21:
            if x >=0 and x <=12:
                print(minutes[y-1], "минута", case123list[x])
            elif x >12 and x <=23:
                print(minutes[y-1], "минута", case123list[x-12])
        elif (y >=2 and y <= 4) or (y >= 22 and y <= 24):
            if x >=0 and x <=12:
                print(minutes[y-1], "минуты", case123list[x])
            elif x >12 and x <=23:
                print(minutes[y-1], "минуты", case123list[x-12])
        elif (y >= 5 and y <=10) or (y >= 11 and y <=16) or (y >= 17 and y <=29):
            if x >=0 and x <=12:
                print(minutes[y-1], "минут", case123list[x])
            elif x >12 and x <=23:
                print(minutes[y-1], "минут", case123list[x-12])          
    elif y > 30 and y < 45:
        if y == 31 or y == 41:
            if x >=0 and x <=12:
                print(minutes1[y-31], "минута", case123list[x])
            elif x >12 and x <=23:
                print(minutes1[y-31], "минута", case123list[x-12])
        elif (y >=32 and y <= 34) or (y >= 42 and y <= 44):
            if x >=0 and x <=12:
                print(minutes1[y-31], "минуты", case123list[x])
            elif x >12 and x <=23:
                print(minutes1[y-31], "минуты", case123list[x-12])
        elif y >= 35 and y <=40:
            if x >=0 and x <=12:
                print(minutes1[y-31], "минут", case123list[x])
            elif x >12 and x <=23:
                print(minutes1[y-31], "минут", case123list[x-12])
else:
    print ("Choose correct mode!")