
'''Реализовать:
1.текстовый вывод сегодняшнего времени
2.текстовый вывод времени, ведомого с консоли (чч:мм).
(дать возможность выбора режима работы программы)

Для получения свободного времени можно использовать модуль datetime.

min == 0: такое-то значение часа ровно
мин < 30: столько-то минут следующих часов
мин == 30: половина такого-то
мин > 30 и мин < 45 столько-то минут следующих часов
мин >= 45 без мин такого-то

21:16
шестнадцать минут десятого'''





import datetime as dt

minutes_count = {
1: ['одна', 'одной'], 2: ['две', 'двух'], 3: ['три', 'трех'],
4: ['четыре', 'четырёх'], 5: ['пять', 'пяти'], 6: ['шесть', 'шести'],
7: ['семь', 'семи'], 8: ['восемь', 'восьми'], 9: ['девять', 'девяти'],
10: ['десять', 'десяти'], 11: ['одинадцать', 'одинадцати'], 
12: ['двенадцать', 'двенадцати'], 13: ['тринадцать', 'тринадцати'],
14: ['четырнадцать', 'четарнадцати'], 15: ['пятнадцать', 'пятнадцати'],
16: ['шестнадцать'], 17: ['семнадцать'], 18: ['восемнадцать'], 19: ['девятнадцать'],
20: ['двадцать'], 30: ['тридцать'], 40: ['сорок'], 50: ['пятьдесят']
}

counting_hours = {
0: ['ноль'],1: ['час', 'первого'],2: ['два', 'второго'],3: ['три', 'третьего'],4: ['четыре', 'четвертого'],5: ['пять', 'пятого'],
6: ['шесть', 'шестого'],7: ['семь', 'седьмого'],8: ['восемь', 'восьмого'],9: ['девять', 'девятого'],10: ['десять', 'десятого'],
11: ['одинадцать', 'одинадцатого'],12: ['двенадцать', 'двенадцатого'],
}


player = int(input('Enter 1 if you want to know the current time!\n'
                   'Enter 2 and you will need to manually enter the time in hh:mm format!\n'))


if player == 1:
    time = dt.datetime.now().time()
    time = time.strftime('%H:%M')

elif player == 2:
    time = input()
    time = time.replace(' ', '')

time = time.split(':')
min = int(time[1])
h = int(time[0])

h1 = h
h = h - 12 if h > 11 else h

if min == 0:
    h1 = h1 - 12 if h1 > 12 else h1
    end = ''
    if h1 == 1:
        print('час ровно')
    else:
        if h1 == 0 or 5 <= h1 <= 12:
            end = 'ов'
        elif 1 < h1 < 5:
            end = 'а'
        print(f'{counting_hours[h1][0]} час{end} ровно')

elif min < 30 or 30 < min < 45:
    if min == 1:
        print(f'{minutes_count[min][0]} минута {counting_hours[h+1][1]}')
    elif 1 < min < 5:
        print(f'{minutes_count[min][0]} минуты {counting_hours[h+1][1]}')
    elif 4 < min < 20:
        print(f'{minutes_count[min][0]} минут {counting_hours[h+1][1]}')
    elif  min == 20 or min == 40:
        print(f'{minutes_count[min][0]} минут {counting_hours[h+1][1]}')
    elif min == 21 or min == 31 or min == 41:
        print(f'{minutes_count[min-min%10][0]} {minutes_count[min%10][0]} минута {counting_hours[h+1][1]}')
    elif 21 < min < 25 or 31< min <35 or 41 < min < 45:
        print(f'{minutes_count[min - min%10][0]} {minutes_count[min%10][0]} минуты {counting_hours[h+1][1]}')
    elif 24 < min < 30 or 34 < min < 40:
        print(f'{minutes_count[min - min%10][0]} {minutes_count[min%10][0]} минут {counting_hours[h+1][1]}')

elif int(min) == 30:
    print(f'половина {counting_hours[h+1][1]}')

elif min >= 45:
    if min == 59:
        print(f'без {minutes_count[60-min][1]} минуты {counting_hours[h+1][0]}')
    else:
        print(f'без {minutes_count[60-min][1]} минут {counting_hours[h+1][0]}')


