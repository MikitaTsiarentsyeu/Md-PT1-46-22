import os
import re

result = {}
source_filename = input("input file name (xmas.txt or my_family) :\n")

_, extension = os.path.splitext(source_filename)
if extension == '':
    source_filename += '.txt'

with open(source_filename, "r") as source_file:
    content = source_file.read().lower()

elem_amount = int(input('input how many elements you want search: '))

match_pattern = re.findall(r'\b(\w+)', content)

for word in match_pattern:
    count = result.get(word, 0)
    result[word] = count + 1

result_list = result.keys()
sorted_values = sorted(result.items(), key=lambda item: (-item[1], item[0]))
sorted_dict = {k: v for k, v in sorted_values}

print(sorted_dict)

for key, value in list(sorted_dict.items())[:elem_amount]:
    if 2 <= value < 5 or 22 <= value < 25:
        print(f'{key} встречается {value} разa')
    else:
        print(f'{key} встречается {value} раз')


