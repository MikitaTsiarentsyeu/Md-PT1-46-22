import json

file_name = 'data.json'
with open(file_name, 'r') as f:
    base = json.load(f)


def get_wh_products():
    return base['wh']


def get_wh_products_by_category(category: str):
    products = get_wh_products()
    products_by_category = []
    for product in products:
        if product['category'] == category:
            products_by_category.append(product)
    return products_by_category


def get_wh_product_by_id(product_id):
    for product in get_wh_products():
        if product['product_id'] == product_id:
            return product


def get_wh_product_quantity_by_id(product_id):
    for product in get_wh_products():
        if product['product_id'] == product_id:
            return product['quantity']


def get_cart_product_quantity_by_id(product_id):
    for product in get_cart_products():
        if product['product_id'] == product_id:
            return product['quantity']


def get_id_by_product_name(product_name: str):
    for product in get_wh_products():
        if product['product_name'] == product_name:
            return product['product_id']


def get_categories_of_products() -> list:
    categories = []
    for product in get_wh_products():
        categories.append(product['category'])
    return list(set(categories))


def get_order_products():
    return base['orders']


def set_wh_products_value(product_id, value, key='quantity'):
    for product in get_wh_products():
        if product['product_id'] == product_id:
            product[key] = value


def change_wh_products_value(product_id, delta, key='quantity'):
    for product in get_wh_products():
        if product['product_id'] == product_id:
            product[key] += delta


def set_cart_products_value(product_id, value, key='quantity'):
    for product in get_cart_products():
        if product['product_id'] == product_id:
            product[key] = value


def change_cart_products_value(product_id, delta, key='quantity'):
    for product in get_cart_products():
        if product['product_id'] == product_id:
            product[key] += delta


def change_orders_products_value(product_id, delta, key='quantity'):
    for product in get_order_products():
        if product['product_id'] == product_id:
            product[key] = delta


def add_product_to_cart(product_id):
    product = get_wh_product_by_id(product_id)
    base['cart'].append(product.copy())
    base['cart'][-1]['quantity'] = 0


def get_cart_products():
    return base['cart']


def delete_cart_product(product_id):
    products_list = get_cart_products()
    for index, product in enumerate(products_list):
        if product['product_id'] == product_id:
            del products_list[index]


def clear_cart_products():
    base['cart'].clear()


def clear_orders_products():
    base['orders'].clear()


def copy_cart_to_order():
    base['orders'] = base['cart'].copy()
