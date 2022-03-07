import data


def get_wh_categories():
    return data.get_categories_of_products()


def get_product_by_category(category: str):
    return data.get_wh_products_by_category(category)


def get_id_by_product(product_name: str):
    return data.get_id_by_product_name(product_name)


def add_product_to_cart(product_id: str, quantity: int):
    data.add_product_to_cart(product_id)
    data.set_cart_products_value(product_id, delta=quantity)
    data.set_wh_products_value(product_id, delta=-quantity)
# print("quantity = zero")


def change_quantity_in_cart(product_id: str, quantity: int):
    data.set_cart_products_value(product_id, delta=quantity)


def remove_product_from_cart(product_id):
    data.delete_cart_product(product_id)


# def change_quantity_in_order():
#     quantity = data.set_orders_products_value()


def show_cart():
    return data.get_cart_products()


# save cart
def add_to_order_list():
    data.copy_cart_to_orders()


def get_order_receipt():
    pass


def get_order_price():
    list_order = data.get_order_products()
    order_price = 0
    for product in list_order:
        order_price += product['price'] * product['quantity']

    return f"Product: {list_order}, quantity: \n Order price is: {order_price} $\n Thank you for order!"




