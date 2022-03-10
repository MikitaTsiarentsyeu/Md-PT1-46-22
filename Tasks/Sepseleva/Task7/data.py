import copy
from decimal import Decimal
repo = {
    12341:{"name":"Harry Potter","author":"J.K. Rowling", "price": '36.99', "category":"Fantasy", "number":5},
    12342:{"name":"Dune","author":"Frank Herbert", "price": '35.00', "category":"Fantasy", "number":2},
    12343:{"name":"The Last Wish","author":"Andrzej Sapkovski", "price": '28.99', "category":"Fantasy", "number":2},
    12344:{"name":"Rebecca","author":"Daphne du Maurier", "price": '8.99', "category":"Classics", "number":8},
    12345:{"name":"Ulysses","author":"James Joyce", "price": '20.00', "category":"Classics", "number":1},
    12346:{"name":"Pride and Prejudice","author":"Jane Austen", "price": '10.99', "category":"Classics", "number":4},
    12347:{"name":"Emma","author":"Jane Austen", "price": '14.99',"category":"Classics", "number":1},
    12348:{"name":"The Shining","author":"Stephen King", "price": '9.99', "category":"Horror", "number":3},
    12349:{"name":"It","author":"Stephen King", "price": '44.99', "category":"Horror", "number":4},
    12350:{"name":"The Call of Cthulhu","author":"Howard Lovecraft", "price": '21.99', "category":"Horror", "number":1},
    12351:{"name":"The Book of Sand","author": "Jorge Luis Borges", "price": '12.99', "category":"Sci-Fi", "number":2},
    12352:{"name":"The Martian", "author": "Andy Weir", "price": '18.99', "category":"Sci-Fi", "number":2},
    12353:{"name":"Solaris","author": " Stanislaw Lem", "price": '8.99', "category":"Sci-Fi", "number":5}    
}

basket = {}

def search_by_type(type, value, l=[]):
    for i in repo.values():
        if value in i[type].lower():
            l.append(i)
    return l

def add_basket(name, number):
    for k,v in repo.items():
        if v['name'].lower() == name:
            if v['number'] == 0:
                raise RuntimeError('There is no such a book in stock now. Sorry for inconveniences.')
            else:
                value = int(v['number']) - int(number)
                if value >= 0:
                    v["number"] = value
                    create_new_item(k, number)
                    return True
                else:
                    number = v['number']
                    v["number"] = 0
                    create_new_item(k, number)
                    raise RuntimeError(f"Only {number} items left in stock. They've been added to the basket")  
        
def show_basket():
    res = copy.deepcopy([repo[i] for i in basket])  
    for i in range(len(basket)):
        res[i]['number'] = list(basket.values())[i]
    return res

def make_order():
    if not basket:
        raise RuntimeError("You cannot make an order. You haven't added any items to your basket yet.")
    total = 0
    for k,v in basket.items():
        total = total + Decimal(repo[k]['price']) * int(v)
    return total

def clean_basket():
    basket.clear()
    
def create_new_item(code,number):
    if code in basket:
        basket[code] = int(basket[code]) + int(number)
    else:
        basket[code] = number
    

