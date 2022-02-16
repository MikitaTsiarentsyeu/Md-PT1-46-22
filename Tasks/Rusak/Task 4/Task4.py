import os

curdir = os.getcwd()
os.chdir(curdir)

def format_line(any_line, len_line):
    space_count = any_line.count(' ')
    if 0 <= space_count <= 2:
        return any_line
    else:
        gap_width, max_replace = divmod(len_line - len(any_line) + space_count, space_count)
        any_line = any_line.replace(' ', ' ' * gap_width).replace(' ' * gap_width, ' ' * (gap_width + 1), max_replace)
        return any_line

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

with open('text.txt', 'r', encoding='utf8') as oldfile:
    while True:
        rline = oldfile.readline()
        if rline:
            linelist = []
            outlist = []
            outline = ''
            len_w = len_line

            for i in rline:
                linelist.append(i)

            while linelist != []:
                while len(linelist) > len_w:
                    while not linelist[len_w-1] == ' ':
                        len_w -= 1
                    for i in range(len_w):
                        outline += linelist.pop(0)
                    outline = outline.rstrip()
                    outlist.append(format_line(outline, len_line) + '\n')
                    outline = ''
                    len_w = len_line
                else:
                    for i in range (len(linelist)):
                        outline += linelist.pop(0)
                    outlist.append(format_line(outline, len_line))

            with open('newtext.txt', 'a', encoding='utf_8') as newfile:
                newfile.writelines(outlist)
        else:
            break
print('Created a new file "newtext.txt" formatted to the required line length. You can find it in the current working directory.')
