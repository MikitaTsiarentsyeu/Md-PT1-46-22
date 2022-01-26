import datetime

time1 = {0:['ноль'], 1:['один','одной минуты','одна минута'], 2:['два','двух','две минуты' ],3:['три','трёх'], 
    4:['четыре', 'четырех'], 5:['пять','пяти'], 6:['шесть','шести'], 7:['семь','семи'], 
    8:['восемь','восьми'], 9:['девять','девяти'], 10:['десять','десяти'], 11:['одиннадцать', 'одиннадцати'], 12:['двенадцать','двенадцати'], 
    13:['тринадцать','тринадцати'], 14:['четырнадцать','четырнадцати' ], 15:['пятнадцать','пятнадцати'], 
    16:['шестнадцать','шестнадцати'], 17:['семнадцать','семнадцати' ], 18:['восемнадцать','восемнадцати' ],
    19:['девятнадцать','девятнадцати' ], 20:['двадцать','двадцати'], 21:['двадцать одна минута','двадцати одной минуты'],
    22:['двадцать две минуты','двадцати двух'], 23:['двадцать три','двадцати трех'], 24:['двадцать четыре','двадцати четырех'],
    25:['двадцать пять','двадцати пяти'], 26:['двадцать шесть','двадцати шести'], 27:['двадцать семь','двадцати семи'], 
    28:['двадцать восемь','двадцати восьми'], 29:['двадцать девять','двадцати девяти']}

time2 = {1: 'первого', 2: 'второго', 3: 'третьего', 4: 'четвертого', 5: 'пятого',
    6: 'шестого', 7: 'седьмого', 8: 'восьмого', 9: 'девятого', 10: 'десятого', 11: 'одиннадцатого', 12: 'двенадцатого'}

# getting data from user
working_mode = input('Выберите режим работы: 1.Ввести время с клавиатуры 2.Вывести текущее время: (1/2)')
working_mode = working_mode.replace(' ', '')
if working_mode in ['1', '2']:
    if working_mode == '1':
        time = input('Введите время в формате ЧЧ:ММ: ').replace(' ', '')
    elif working_mode == '2':
        time = str(datetime.datetime.now())
        time = time [11:16]  


    #validation
    if ':' in time and time.replace(':', '').isdigit():
        print(f'Текущее время: {time}')
        time = time.split(':')
        h = int(time[0])
        m = int(time[1])

        if h in range(0,25) and m in range(0,60):
            h = h - 12 if h > 12 else h
            hour1 = time2[1] if h == 12 else time2[h+1] #hours value before 30min + half an hour
            hour2 = 'час' if h in [0,12] else time1[h+1][0] #hours value after 30min
    
            #showing the time

            #exact time
            if m == 0:
                if h == 1:
                    print(f'{time1[h][0]} час ровно')
                elif h > 1 and h < 5:
                    print(f'{time1[h][0]} часа ровно')
                else:
                    print(f'{time1[h][0]} часов ровно')

            #time before 30 min
            if m >= 1 and m < 30:

                if m in [1,2]:
                    print(f'{time1[m][2]} {hour1}')
                elif m in [21,22]:
                    print(f'{time1[m][0]} {hour1}')
                elif m in [3,4,23,24]:
                    print(f'{time1[m][0]} минуты {hour1}')
                else:
                    print(f'{time1[m][0]} минут {hour1}')

            # 30 min
            if m == 30:
                print(f'половина {hour1}')

            # time after 30 min
            if m > 30:
                if 60-m in [1,21]:
                    print(f'Без {time1[60-m][1]} {hour2}')
                else:
                    print(f'Без {time1[60-m][1]} минут {hour2}')

# Sorry for such validation but I couldn't think of other ways to do that :)

        else:
            print('Неверно введены данные. Пожалуйста, перезапустите программу и попробуйте снова.')
    else:
        print('Неверно введены данные. Пожалуйста, перезапустите программу и попробуйте снова.')
else:
    print('Неверно введены данные. Пожалуйста, перезапустите программу и попробуйте снова.')




   
