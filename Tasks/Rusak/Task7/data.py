warehouse = {
    1664200101 : ['Break system', 'Break pads', '250', 2],
    2124200101 : ['Break system', 'Break pads', '240', 8],
    1664200201 : ['Break system', 'Break disc', '320', 4],
    1663300101 : ['Suspension', 'Front spring', '540', 10],
    2123300101 : ['Suspension', 'Front spring', '415', 4],
    1663200102 : ['Suspension', 'Front shock absorber', '635', 8]
    }

cart = {}

def change_product_quantity(id, value):
    start_qn = cart[id][-1]
    new_qn = value
    if new_qn > start_qn:
        warehouse[id][-1] -= (new_qn - start_qn)
    elif new_qn < start_qn:
        warehouse[id][-1] += (start_qn - new_qn)
    cart[id][-1] = new_qn
    return True

def search_name(name):
    res = {}
    for k, v in warehouse.items():
        for i in v:
            if i == name:
                res[k] = v
    return res.items()

def change_wh_quantity(id):
    if warehouse[id][-1] > 0:
        warehouse[id][-1] -= 1
    else:
        return False

def remove_all_from_cart():
    for k in cart.keys():
        warehouse[k][-1] += cart[k][-1]
    cart.clear()
    return True

def remove_one(id):
    res = cart.pop(id)
    warehouse[id][-1] += res[-1]
    return True

def search_num(id):
    for k in warehouse.keys():
        if k == id:
            return warehouse.get(id)

def add_to_cart(id):
    cart_values = warehouse.get(id)
    cart.update({id:[cart_values[1], cart_values[2], 1]})

def get_cart():
    return cart.items()

def get_all_parts():
    return warehouse.items()

def get_categories():
    return warehouse.values()
