#!/usr/bin/env python3

from datetime import datetime

d = {0: ("Двенадцать часов", "минут", "Первого"),
     1: ("Один час", "Одна минута", "Второго", "Одной минуты"),
     2: ("Два часа", "Две минуты", "Третьего", "Двух минут", "Двадцать"),
     3: ("Три часа", "Три минуты", "Четвертого", "Трех минут", "Тридцать"),
     4: ("Четыре часа", "Четыре минуты", "Пятого", "Четырех минут", "Сорок"),
     5: ("Пять часов", "Пять минут", "Шестого", "Пяти минут"),
     6: ("Шесть часов", "Шесть минут", "Седьмого", "Шести минут"),
     7: ("Семь часов", "Семь минут", "Восьмого", "Семи минут"),
     8: ("Восемь часов", "Восемь минут", "Девятого", "Восьми минут"),
     9: ("Девять часов", "Девять минут", "Десятого", "Девяти минут"),
     10: ("Десять часов", "Десять минут", "Одинадцатого", "Десяти минут"),
     11: ("Одинадцать часов", "Одинадцать минут", "Двенадцатого", "Одинадцати минут"),
     12: ("Двенадцать часов", "Двенадцать минут", "Первого", "Двенадцати минут"),
     13: ("час", "Тринадцать минут", "", "Тринадцати минут"),
     14: ("", "Четырнадцать минут", "", "Четырнадцати минут"),
     15: ("", "Пятнадцать минут", "", "Пятнадцати минут"),
     16: ("", "Шестнадцать минут"),
     17: ("", "Семнадцать минут"),
     18: ("", "Восемнадцать минут"),
     19: ("", "Девятнадцать минут")}


def time_conversion(dist, time_date):
    if time_date.hour <= 12:
        h = dist.get(time_date.hour)
    else:
        h = dist.get(time_date.hour - 12)
    if time_date.minute == 0:
        time_str = f"{h[0]} ровно"
        print(time_str)
    elif time_date.minute == 30:
        time_str = f"Половина {h[2].lower()}"
        print(time_str)
    elif 1 <= time_date.minute < 45:
        m = dist.get(time_date.minute // 10)
        m_1 = dist.get(time_date.minute % 10)
        if time_date.minute < 20:
            m = dist.get(time_date.minute)
            time_str = f"{m[1]} {h[2].lower()}"
            print(time_str)
        else:
            time_str = f"{m[4]} {m_1[1].lower()} {h[2].lower()}"
            print(time_str)
    else:
        m = dist.get(60 - time_date.minute)
        m_1 = dist.get(time_date.hour + 1) if time_date.hour <= 12 else dist.get(time_date.hour - 12 + 1)
        if (time_date.hour + 1) == 1 or (time_date.hour - 12 + 1) == 1:
            s = m_1[0].replace('Один ', '')
        elif 0 < (time_date.hour + 1) < 5 or 0 < (time_date.hour - 12 + 1) < 5:
            s = m_1[0].replace(' часа', '')
        else:
            s = m_1[0].replace(' часов', '')
        time_str = f"Без {m[3].lower()} {s.lower()}"
        print(time_str)


print("Program: Time to string conversion")

x = input(
    """
Press "Y" or "y" first then "Enter" if you want to enter the time yourself
if you want use current time just press "Enter": """)

if x == "Y" or x == "y":
    y = input("Enter the time in format HH:MM:")
    if ':' in y:
        time = y.split(":")
        hour, minute = time[0].strip(), time[1].strip()
        if len(time) == 2 and hour.isdigit() and minute.isdigit():
            hour = 0 if int(time[0].strip()) == 24 else int(time[0].strip())
            minute = 0 if int(time[1].strip()) == 60 else int(time[1].strip())
            hour = (hour + 1) if int(time[1].strip()) == 60 else hour
            if (0 <= hour < 24) and (0 <= minute < 60):
                time_now = f"{hour}:{minute}"
                time_obj = datetime.strptime(time_now, '%H:%M')
                time_now1 = time_obj.strftime('%H:%M').split(':')
                print(f"{time_now1[0]}:{time_now1[1]}")
                time_conversion(d, time_obj)
            else:
                print("Input ERROR. Restart program and repeat")
        else:
            print("Input ERROR. Restart program and repeat")
    else:
        print("Input ERROR. Restart program and repeat")
else:
    time_obj = datetime.now()
    time_now1 = time_obj.strftime('%H:%M').split(':')
    print(f"{time_now1[0]}:{time_now1[1]}")
    time_conversion(d, time_obj)
