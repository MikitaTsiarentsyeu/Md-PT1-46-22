import data

def menu():
    menu = data.get_menu()
    return '\n'.join([f'Id: {d["id"]}\nName: {d["name"]}\nCategory: {d["category"]} \nPrice: {d["price"]} BYN\nAvailable: {d["available"]} \n' for d in menu])

def search(id):
    res = data.search_item(id)
    if res:
        return '\n'.join([f' {k.capitalize()} : {v}' for k,v in res.items()])
    else:
        return 'There is no items with this id',id

def add_items(id,quantity):
    return data.add_item(id,quantity)
    
def remove_items(id):
    return data.remove_item(id)

    

def len_basket():
    return data.get_len_basket()

def clean():
    return data.clean_basket()

def get_receipt():
    receipt = data.get_receipt()
    view = '\n'.join([f' Name: {d["name"]} {d["price"]}BYN*{d["quantity"]} ={d["price"]*d["quantity"]} BYN ' for d in receipt])
    total = [i['price']*i['quantity'] for i in receipt]
    return f'{view}\n Total: {sum(total)} BYN'

