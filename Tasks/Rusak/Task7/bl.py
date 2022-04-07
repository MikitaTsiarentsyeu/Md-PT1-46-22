import data

def add_to_cart(id):
    try:
        id = int(id)
        if id not in data.cart.keys():
            data.add_to_cart(id)
            if data.change_wh_quantity(id) != False:
                return f"\n{id} has been successfully added to your cart.\n"
            else:
                return f"\nNot enougth quantity of {id} at warehouse.\n"
        else:
            return f"\n{id} is already in your cart. If you want to add one more, go to your cart and change the quantity there.\n"
    except TypeError:
        return '\nNo spare part with such id number in stock.\n'
    except ValueError:
        return '\nA spare part id number must consist only digits.\n'

def make_an_order(choice):
    choice = choice.capitalize()
    if choice == 'Y':
        if not data.get_cart():
            return "Your cart is empty. You can't to checkout.\n"
        else:
            total_price = sum([(int(v[1])*v[2]) for k, v in data.get_cart()])
            remove_all_from_cart()
        return f'You confirmed your order, total price is {total_price}$. Our sales manager call you back as soon as possible. Have a nice day.'
    elif choice == 'N':
        return 'Order was declined.\n'
    else:
        return 'Unknown command, repeat your choice.\n'

def remove_one(id):
    try:
        id = int(id)
        data.remove_one(id)
        return f'{id} has been seccessfully removed from your cart.\n'
    except KeyError:
        return f'No spare part with id number {id} in your cart.\n'
    except TypeError:
        return f'No spare part with id number {id} in your cart.\n'
    except ValueError:
        return 'A spare part id number must consist only digits.\n'

def change_quantity_in_cart(id, value):
    if id in data.cart.keys():
        if int(value) > (data.warehouse[id][-1] + 1):
            return f"The value cannot be changeв. Only {(data.warehouse[id][-1] + data.cart[id][-1])} items left in stock\n"
        elif int(value) <= (data.warehouse[id][-1] +1):
            data.change_product_quantity(id, value)
            return 'Value successfully changed.\n'
    else:
        return f'There is no spare part with id number {id} in your cart\n'

def search_by_id(id):
    try:
        id = int(id)
        res = data.search_num(id)
        return f'\nWe have this part in our stock:\nid: {id};  category: {res[0]};  part name: {res[1]};  price = {res[2]};  quantity = {res[3]}'
    except TypeError:
        return '\nThere is no spare part with such id number.\n'    
    except ValueError:
        return '\nA spare part id number must consist only digits.\n'

def search_name(name):
    name = name.capitalize()
    catalogue = data.search_name(name)
    if not catalogue:
        return 'There is no such spare part.\n'
    else:
        return '\n'.join([f'id: {k};  category: {v[0]};  part name: {v[1]};  price = {v[2]};  quantity = {v[3]}' for k, v in catalogue])

def get_categories():
    catalogue = data.get_categories()
    list_cat = []
    for c in catalogue:
        if c[0] not in list_cat:
            list_cat.append(c[0])
    return '\n'.join(list_cat)
       
def show_cart():
    catalogue = data.get_cart()
    if not catalogue:
        return 'The cart is empty.\n'
    else:
        return '\n'.join([f'id: {k};  part name: {v[0]};  price = {v[1]};  quantity = {v[2]};  summary price = {int(v[1])*v[2]}' for k, v in catalogue])

def get_category(name):
    catalogue = data.get_all_parts()
    return '\n'.join([f'id: {k};  category: {v[0]};  part name: {v[1]};  price = {v[2]};  quantity = {v[3]}' for k, v in catalogue if v[0] == name])

def get_all():
    catalogue = data.get_all_parts()
    return '\n'.join([f'id: {k};  category: {v[0]};  part name: {v[1]};  price = {v[2]};  quantity = {v[3]}' for k, v in catalogue])

def remove_all_from_cart():
    data.remove_all_from_cart()
    return 'All items have been successfully removed from your cart.\n'
