from collections import Counter
user_text = input('Input your text:')

user_text = user_text.lower().replace(',','').replace('.','').split(' ')
#print(user_text)
user_number_of_items = int(input('Please,enter the number of items you would like to see:'))

for i in range(1, len(user_text)):
    key = user_text[i]
    j = i-1
    while j >=0 and key < user_text[j] :
        user_text[j+1] = user_text[j]
        j -= 1
        user_text[j+1] = key 

dict_token_items = {}

for items in user_text:
    dict_token_items[items] = dict_token_items.get(items,0) + 1
#print(dict_token_items)

dict_token_items2 = dict(Counter(dict_token_items).most_common(user_number_of_items))
for keys, values in dict_token_items2.items():
    print("'",keys,"'", 'meets',values,'times')
