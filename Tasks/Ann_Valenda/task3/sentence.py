input_string = input(str('input some text, please: '))
elem_amount = int(input('input how many elements you want search: '))

string_set = set(input_string)
print(string_set)

counter: int = 0
result = {}
for set_item in string_set:
    for letter in input_string:
        if set_item == letter:
            counter += 1
        result[set_item] = counter
    counter = 0
print(result)
sorted_values = sorted(result.items(), key=lambda item: item[1], reverse=True)
sorted_dict = {k: v for k, v in sorted_values}
print(sorted_dict)

for key, value in list(sorted_dict.items())[:elem_amount]:
    if 2 <= value < 5 or 22 <= value < 25:
        print(f'{key} встречается {value} разa')
    else:
        print(f'{key} встречается {value} раз')













