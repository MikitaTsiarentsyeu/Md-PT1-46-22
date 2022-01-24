from datetime import datetime as d
import re
user_choice = input("To check the exact time, please enter 'c', to indicate time manually, please enter 'm':")

while  user_choice not in ['c', 'm']:
    user_choice = input("Unknown istruction. To check the exact time, please enter 'c', to indicate time manually, please enter 'm':")

if user_choice == 'c':
    time = d.today()
    time = str(time.strftime("%H:%M"))
else:
    time = input("Please enter time (hh:mm) manually:")
    while re.fullmatch(r'[2][0-3]:[0-5][0-9]', time) is None and re.fullmatch(r'[0-1][0-9]:[0-5][0-9]', time) is None:
        time = input("Not valid time. Please enter time in correct format (hh:mm):")
           
hour, minutes = time.split(":")

if minutes == "00":
    hours_dict = {"00": "ноль", "01": "один", "02": "два", "03": "три", "04":  "четыре", "05": "пять", "06": "шесть", "07": "семь", "08": "восемь", 
    "09": "девять", "10": "десять", "11": "одиннадцать", "12": "двенадцать", "13": "один", "14": "два", "15": "три", "16":  "четыре", "17": "пять", 
    "18": "шесть", "19": "семь", "20": "восемь", "21": "девять", "22": "десять", "23": "одиннадцать"}
    name = list(hours_dict.keys())
    if hour in name[1] or hour in name[13]:
        print(f"{hours_dict[hour]}", "час ровно")
    elif hour in name[2:5] or hour in name[14:17]:
        print(f"{hours_dict[hour]}", "часа ровно")
    else:
        print(f"{hours_dict[hour]}", "часов ровно")

if minutes != "00" and minutes < "30":
    minutes_dict = {"01": "одна", "02": "две", "03": "три", "04": "четыре", "05": "пять", "06": "шесть", "07": "семь", "08": "восемь", "09": "девять", "10": "десять", 
    "11": "одиннадцать", "12": "двенадцать", "13": "тринадцать", "14": "четырнадцать", "15": "пятнадцать", "16": "шестнадцать", "17": "семнадцать", "18": "восемнадцать", 
    "19": "девятнадцать", "20": "двадцать", "21": "двадцать одна", "22": "двадцать две", "23": "двадцать три", "24": "двадцать четыре", "25": "двадцать пять", "26": "двадцать шесть", 
    "27": "двадцать семь", "28": "двадцать восемь", "29":  "двадцать девять"}
    hours_dict = {"00": "первого", "01": "второго", "02": "третьего", "03": "четвертого", "04": "пятого", "05": "шестого", "06": "седьмого", "07": "восьмого", "08": "девятого", 
    "09": "десятого", "10": "одиннадцатого", "11": "двенадцатого", "12": "первого", "13": "второго", "14": "третьего", "15": "четвертого", "16": "пятого", "17": "шестого", 
    "18": "седьмого", "19": "восьмого", "20": "девятого", "21": "десятого", "22": "одиннадцатого", "23": "двенадцатого"}
    name = list(minutes_dict.keys())
    if minutes in name[0] or minutes in name[20]:
        print(f"{minutes_dict[minutes]} минута {hours_dict[hour]} часа")
    elif minutes in name[1:5] or minutes in name [21:24]:
        print(f"{minutes_dict[minutes]} минуты {hours_dict[hour]} часа")
    else:
        print(f"{minutes_dict[minutes]} минут {hours_dict[hour]} часа")

if minutes == "30":
    hours_dict ={"00": "первого", "01": "второго", "02": "третьего", "03": "четвертого", "04": "пятого", "05": "шестого", "06": "седьмого", "07": "восьмого", "08":"девятого", 
    "09":"десятого", "10": "одиннадцатого", "11": "двенадцатого", "12": "первого", "13": "второго", "14": "третьего", "15": "четвертого", "16": "пятого", "17": "шестого", 
    "18": "седьмого", "19": "восьмого", "20":"девятого", "21":"десятого", "22": "одиннадцатого", "23": "двенадцатого"}
    print(f"половина {hours_dict[hour]} часа")

if minutes > "30" and minutes < "45":
    minutes_dict = {"31": "тридцать одна", "32": "тридцать две", "33": "тридцать три", "34": "тридцать четыре", "35": "тридцать пять", "36": "тридцать шесть", "37": "тридцать семь", 
    "38": "тридцать восемь", "39": "тридцать девять", "40": "сорок", "41": "сорок одна", "42": "сорок две", "43": "сорок три", "44": "сорок четыре"}
    hours_dict = {"00": "первого", "01": "второго", "02": "третьего", "03": "четвертого", "04": "пятого", "05": "шестого", "06": "седьмого", "07": "восьмого", "08": "девятого", 
    "09": "десятого", "10": "одиннадцатого", "11": "двенадцатого", "12": "первого", "13": "второго", "14": "третьего", "15": "четвертого", "16": "пятого", "17": "шестого", 
    "18": "седьмого", "19": "восьмого", "20": "девятого", "21": "десятого", "22": "одиннадцатого", "23": "двенадцатого"}
    name = list(minutes_dict.keys())
    if minutes == name[0] or minutes == name[10]:
        print(f"{minutes_dict[minutes]} минута {hours_dict[hour]} часа")
    elif minutes in name[1:4] or minutes in name[11:13] or minutes in name[13]:
        print(f"{minutes_dict[minutes]} минуты {hours_dict[hour]} часа")
    else:
        print(f"{minutes_dict[minutes]} минут {hours_dict[hour]} часа")
 
if minutes >= "45":
    minutes_dict = {"45": "пятнадцати", "46": "четырнадцати", "47": "тринадцати", "48": "двенадцати", "49": "одиннадцати", "50": "десяти", "51": "девяти", "52": "восьми", 
    "53": "семи", "54": "шести", "55": "пяти", "56": "четырех", "57": "трех", "58": "двух", "59": "одной"}
    hours_dict = {"00": "один", "01": "два", "02": "три", "03": "четыре", "04": "пять", "05": "шесть", "06": "семь", "07": "восемь", "08": "девять", "09": "десять", 
    "10": "одиннадцать", "11": "двенадцать", "12": "один", "13": "два", "14": "три", "15": "четыре", "16": "пять", "17": "шесть", "18": "семь", "19": "восемь", "20": "девять", 
    "21": "десять", "22": "одиннадцать", "23": "двенадцать"}
    name = list(hours_dict.keys())
    if minutes == list(minutes_dict.keys())[14]:
        message_part_1 = (f"без {minutes_dict[minutes]} минуты")
    else:
        message_part_1 = (f"без {minutes_dict[minutes]} минут")
    if hour == name[0] or hour == name[12]:
        message_part_2 = (f"{hours_dict[hour]} час")
    elif hour in name[1:4] or hour in name[13:16]:
        message_part_2 = (f"{hours_dict[hour]} часа")
    else:
        message_part_2 = (f"{hours_dict[hour]} часов")
    print(f"{message_part_1} {message_part_2}")
  