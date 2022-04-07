menu = [
    {'id':1001, 'name' :'Big Mac','category':'Burgers','price' : 8, 'available':15},
    {'id':1002, 'name' :'Cheeseburger','category':'Burgers','price' : 5, 'available':12},
    {'id':1003, 'name' :'Hamburger','category':'Burgers','price' : 4,'available':10},
    {'id':1004, 'name' :'McFlurry with OREO cookies','category':'Desserts','price' : 7,'available':11},
    {'id':1005, 'name' :'Vanilla Cone','category':'Desserts','price' : 9,'available':19},
    {'id':1006, 'name' :'Baked Cherry pie','category':'Desserts','price' : 5,'available':10},
    {'id':1007, 'name' :'Sprite','category':'Beverages','price' : 2,'available':8},
    {'id':1008, 'name' :'Coca-Cola','category':'Beverages','price' : 2,'available':19},
    {'id':1009, 'name' :'Fanta Orange','category':'Beverages','price' : 2,'available':13}
]

def get_menu(): 
    return menu

def search_item(id):
    for items in menu:
        if items['id']==id:
            return items

basket = []

def add_item(id,quantity):
    id_items = search_item(id)
    id_items['quantity'] = quantity
    if id_items['quantity']<=id_items['available']:
        id_items['available']-=quantity
        basket.append(id_items)
        return basket
    else:
        return f'Expected no more than {id_items["available"]}items'
        

def remove_item(id):
    for items in basket:
        if items['id']==id:
            return f' Deleted:{basket.pop(basket.index(items))}'
        else:    
            return 'No id in the basket'

def get_len_basket():
    return f'{len(basket)} items'

def clean_basket():
    basket.clear()
    return('Basket is empty')

def get_receipt():
   return basket.copy()