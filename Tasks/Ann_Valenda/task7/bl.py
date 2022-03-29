import data


def get_wh_categories() -> list:
    return data.get_categories_of_products()


def get_product_by_category(category: str):
    return data.get_wh_products_by_category(category)


def get_id_by_product(product_name: str):
    return data.get_id_by_product_name(product_name)


def add_product_to_cart(product_id: str, quantity: int):
    wh_product_quantity = data.get_wh_product_quantity_by_id(product_id)
    if wh_product_quantity < quantity:
        return wh_product_quantity
    data.add_product_to_cart(product_id)
    data.change_cart_products_value(product_id, delta=quantity)
    data.change_wh_products_value(product_id, delta=-quantity)



def change_quantity_in_cart(product_id: str, quantity: int):
    wh_product_quantity = data.get_wh_product_quantity_by_id(product_id)
    cart_product_quantity = data.get_cart_product_quantity_by_id(product_id)
    if wh_product_quantity + cart_product_quantity < quantity:
        return wh_product_quantity + cart_product_quantity  # process current exception. Not enough products
    remove_product_from_cart(product_id)
    add_product_to_cart(product_id, quantity)


def remove_product_from_cart(product_id):
    cart_product_quantity = data.get_cart_product_quantity_by_id(product_id)
    wh_product_quantity = data.get_wh_product_quantity_by_id(product_id)
    data.set_wh_products_value(product_id, cart_product_quantity + wh_product_quantity)
    data.delete_cart_product(product_id)


def show_cart():
    return data.get_cart_products()


def add_to_order_list():
    data.copy_cart_to_order()
    data.clear_cart_products()


def get_order_receipt():
    list_order = data.get_order_products()
    return list_order


def get_order_price():
    list_order = data.get_order_products()
    order_price = 0
    for product in list_order:
        order_price += product['price'] * product['quantity']
    return order_price


def is_category_exists(category_name: str) -> bool:
    categories = data.get_categories_of_products()
    if category_name in categories:
        return True
    else:
        return False


def is_product_exists(product_name: str) -> bool:
    products = list(map(lambda x: x['product_name'], data.get_wh_products()))
    if product_name in products:
        return True
    else:
        return False

