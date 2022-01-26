import datetime

d1 = {1:("час", "первого"), 2:("два", "второго"), 3:("три", "третьего"), 4:("четыре", "четвертого"),
5:("пять", "пятого"), 6:("шесть", "шестого"), 7:("семь", "седьмого"), 8:("восемь", "восьмого"),
9:("девять", "девятого"), 10:("десять", "десятого"), 11:("одиннадцать", "одиннадцатого"), 12:("двенадцать", "двенадцатого"), 0:("ноль","")}

d2 = {1:("одна минута", "одной минуты"), 2:("две минуты", "двух минут"), 3:("три минуты", "трех минут"), 4:("четыре минуты", "четырёх минут"),
5:("пять минут", "пяти минут"), 6:("шесть минут", "шести минут"), 7:("семь минут", "семи минут"), 8:("восемь минут", "восьми минут"),
9:("девять минут", "девяти минут"), 10:("десять минут", "десяти минут"), 11:("одиннадцать минут", "одиннадцати минут"), 12:("двенадцать минут", "двенадцати минут"), 
13:("тринадцать минут", "тринадцати минут"), 14:("четырнадцать минут", "четырнадацати минут"), 15:("пятнадцать минут", "пятнадцати минут"),
16:("шестнадцать минут"), 17:("семнадцать минут"), 18:("восемнадцать минут"), 19:("девятнадцать минут"), 20:("двадцать минут"), 21:("двадцать одна минута"),
22:("двадцать две минуты"), 23:("двадцать три минуты"), 24:("двадцать четыре минуты"), 25:("двадцать пять минут"), 26:("двадцать шесть минут"), 27:("двадцать семь минут"),
28:("двадцать восемь минут"), 29:("двадцать девять минут"), 30:("половина"), 31:("тридцать одна минута"), 32:("тридцать две минуты"), 33:("тридцать три минуты"),
34:("тридцать четыре минуты"), 35:("тридцать пять минут"), 36:("тридцать шесть минут"), 37:("тридцать семь минут"), 38:("тридцать восемь минут"), 39:("тридцать девять минут"),
40:("сорок минут"), 41:("сорок одна минута"), 42:("сорок две минуты"), 43:("сорок три минуты"), 44:("сорок четыре минуты"), 0:("ровно")}

rezim = str(input("Выберите режим работы:\nВведите Да для работы с текущим временем или введите любой символ для ввода времени в формате HH:MM: "))
rezim = rezim.replace(" ", "")
rezim = rezim.lower()

if rezim == "да": 
    dat = datetime.datetime.now()   
    dat = str(dat)
    dat = str(dat[11:16])

else : dat = input("Введите время в формате HH:MM: ")

dat = dat.replace(" ", "")

print(f"Текущее время {dat}")

h = int(dat[0:2])
m = int(dat[3:5])
h = h-12 if h > 12 else h

if m == 0:

    if h == 1:
        print(f"{ d1[h][0]} {d2[m]}")
    elif 1 < h < 5:
        print(f"{ d1[h][0]} часа {d2[m]}")
    else:
        print(f"{ d1[h][0]} часов {d2[m]}")   

elif m <= 15:
    h = 0 if h+1 == 13 else h
    print(f"{d2[m][0]} {d1[h+1][1]}")

elif m <= 44:
    h = 0 if h+1 == 13 else h
    print(f"{d2[m]} {d1[h+1][1]}")

elif m > 44:
    h = 0 if h+1 == 13 else h
    m = 60 - m    
    print(f"без {d2[m][1]} {d1[h+1][0]}")









