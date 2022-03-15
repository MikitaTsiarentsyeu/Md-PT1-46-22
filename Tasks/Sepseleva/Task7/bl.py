import data 
from prettytable import PrettyTable

def search_by_type(type, value):
    res = data.search_by_type(type, value, l=[])
    t = show_contents(res)
    if t:
       return f"""
        ***All the results of your search '{type}: {value} '***
{t}"""
    return f'There are no such books in our store'
    #Used formatting like that first: 
    # f"Category: {category}\n\n"+"\n".join([f"{i['name']}, {i['author']} (price - ${i['price']:.2f}, quantity in stock - {i['number']})" for i in res]) 
    #Then decided to use prettytable, seems to me it looks a bit nicer

def add_basket(name, number):
    try:
        validate_number(number)
    except ValueError:
        return "The quantity of books should be a positive number"
    try:
        res = data.add_basket(name, number)
    except RuntimeError as er:
        return er
    if res:
        return "The items have been added to the basket"
    return "There's no such a book in our store"
    
def show_basket():
    res = data.show_basket()
    t = show_contents(res)
    if t:
        return f"""
        ***Items in your basket***
{t}"""
    return "Your basket is empty now. To add items input '2'"

def make_order():
    try:
        res = data.make_order()
        with open('orders.txt', 'a') as f:
            f.write(f'New Order\n')
            f.write(f'{show_contents(data.show_basket())}')
            f.write(f'\nTotal: ${res:.2f}\n\n')   
        return f"\nThe total sum of your purchase: ${res:.2f}\nYour order has been registered successfully."    
    except RuntimeError as er:
        return er

def clean_basket():
    data.clean_basket()
       
def validate_number(n):
    n = int(n)
    if n <= 0:
        raise ValueError
    return n

def show_contents(l):
    if l:
        t = PrettyTable()
        t.field_names = [i for i in l[0].keys()]
        t.add_rows([[v for v in i.values()] for i in l])
        return t

