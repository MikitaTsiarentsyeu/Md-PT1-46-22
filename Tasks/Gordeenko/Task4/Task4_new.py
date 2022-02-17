# 1. Прочитать содержимое файла text.txt
# 2. Дать пользователю ввести с клавиатуры параметр "максимальное количество символов в строке", который должен быть больше 35
# 3. Отформатировать текст с учётом максимального количества символов как ограничения на длину строки, при этом если слово целиком не умещается в строке, оно должно быть перенесено на следующую, а отступы между словами равномерно увеличены (по аналогии с функцией "Выровнять по ширине" текстовых редакторов)
# 4. Записать получившийся текст в новый файл и оповестить об этом пользователя.(модуль textwrap использовать нельзя)

user_input = int(input("Please input maximum number of characters in a string (from 35 to ...)\n"))     

if user_input < 35:
    print("incorrect input, number greater than 35 ")
    exit()


import os
#print(os.getcwd())


with open (os.path.join(os.getcwd(), "Task4", "text.txt"), 'r', encoding="utf8") as f:
    f.seek(0)
    for l in f:
        l.split()
        z = 0
        for i in l:
            z += 1
            print(i, end ="")
            if (z>= user_input) and (i == " "):
                z = 0
                print('\r')


with open (os.path.join(os.getcwd(), "Task4", "text_new.txt"), 'w', encoding="utf8") as f:
    f.seek(0)
    f.writelines(l)

    
print("\nDear user! The text is written to a new file 'text_new.txt' ")
