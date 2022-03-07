base = {
    'wh': [
        {'product_id': 'f123454-888', 'category': 'fruit', 'product_name': 'apples', 'price': 2, 'quantity': 54},
        {'product_id': 'f543221-098', 'category': 'fruit', 'product_name': 'bananas', 'price': 1.5, 'quantity': 45},
        {'product_id': 'f787543-980', 'category': 'fruit', 'product_name': 'oranges', 'price': 2.50, 'quantity': 23},
        {'product_id': 'f234876-463', 'category': 'fruit', 'product_name': 'mangoes', 'price': 8, 'quantity': 8},
        {'product_id': 'd999564-098', 'category': 'drinks', 'product_name': 'soda', 'price': 1, 'quantity': 12},
        {'product_id': 'd343255-676', 'category': 'drinks', 'product_name': 'juice', 'price': 2.30, 'quantity': 33},
        {'product_id': 'd342657-611', 'category': 'drinks', 'product_name': 'water', 'price': 0.80, 'quantity': 100}

    ],
    'cart': [],
    'orders': [],
        }


# wh functions
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


def get_id_by_product_name(product_name: str):
    for product in get_wh_products():
        if product['product_name'] == product_name:
            return product['product_id']


def get_categories_of_products() -> set:
    categories = []
    for product in get_wh_products():
        categories.append(product['category'])
    return list(set(categories))


def get_order_products():
    return base['orders']


# change quantity
def set_wh_products_value(product_id, delta, key='quantity'):
    for product in get_wh_products():
        if product['product_id'] == product_id:
            product[key] += delta


def set_cart_products_value(product_id, delta, key='quantity'):
    for product in get_cart_products():
        if product['product_id'] == product_id:
            product[key] += delta


def set_orders_products_value(product_id, delta, key='quantity'):
    for product in get_order_products():
        if product['product_id'] == product_id:
            product[key] = delta


# add product
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


def copy_cart_to_orders():
    base['orders'] = base['cart'].copy()
