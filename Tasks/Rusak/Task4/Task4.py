from encodings import utf_8
import os

curdir = os.getcwd()
os.chdir(curdir)

while True:
    len_line = input('\nInput the length of the string, its value must not be less than 35:\t')
    if not len_line.isdigit():
        print('\nIncorrect input! Please, input digit value.')
        continue

    len_line = int(len_line)

    if len_line < 35:
        print('\nIncorrect input! Please, input digit value not less than 35.')
        continue
    break

def format_list(any_list, final_list):
    newline = ''
    i = 0
    while any_list != []:
        while len(newline) < len_line:
            if len(newline)+len(any_list[i])+1 > len_line:
                break

            newline = newline + ' ' + any_list.pop(i)
            newline = newline.lstrip()
                    
            if any_list == []:
                break
        final_list.append(newline)
        newline = ''
    return final_list

with open('text.txt', 'r', encoding='utf8') as oldfile:
    s = oldfile.readlines()
    linelist = []
    for i in s:
        linelist.append(i)

linelist2 = []

for i in linelist:
    i = i.replace('\n', '')
    formatted_line = i.split()
    linelist2.append(formatted_line)

finallist = []

for i in range(len(linelist2)):
    format_list(linelist2[i], finallist)

finallist2 = []

for finalline in finallist:
    space_count = finalline.count(' ')
    if 0 <= space_count <= 2:
        finallist2.append(finalline)
        continue
    gap_width, max_replace = divmod(len_line - len(finalline) + space_count, space_count)
    finalline = finalline.replace(' ', ' ' * gap_width).replace(' ' * gap_width, ' ' * (gap_width + 1), max_replace)
    finallist2.append(finalline)

for i in range(len(finallist2)-1):
    finallist2[i] = finallist2[i]+'\n'

with open('newtext.txt', 'w', encoding='utf_8') as newfile:
    newfile.writelines(finallist2)
    print('Created a new file "newtext.txt" formatted to the required line length. You can find it in the current working directory.')
