from collections import Counter
user_line = input('Please,enter your line:')
#print(user_line)
user_line = user_line.lower().replace('',' ').split()
user_number_of_items = int(input('Please,enter the number of items you would like to see:'))
#print(user_number_of_items)

#for i in range(1, len(user_line)):
#    key = user_line[i]
#    j = i-1
#    while j >=0 and key < user_line[j] :
#        user_line[j+1] = user_line[j]
#        j -= 1
#        user_line[j+1] = key 

dict_token_items = {}

for items in user_line:
    dict_token_items[items] = dict_token_items.get(items, 0) + 1 
print(dict_token_items)
dict_token_items2 = dict(Counter(dict_token_items).most_common(user_number_of_items))

for keys, values in dict_token_items2.items():
    print("'",keys,"'", 'meets',values,'times')