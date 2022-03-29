import bl


def show_query(message):
    return input(message)


def show_wh_categories():
    print('Category: ')
    for category in bl.get_wh_categories():
        print(f' - {category}')


def show_products_by_category():
    selected_category = input('Choose category (input name of category):  ').lower()
    if bl.is_category_exists(selected_category):
        products = bl.get_product_by_category(selected_category)
        for product in products:
            print(f'{product["product_name"]:>10}  ${product["price"]:<3} {product["quantity"]:>5} products available')
    else:
        print("The entered category doesn't exist, please try again")


def add_product_to_cart():
    selected_product = input('Choose product:  ').lower()
    if not bl.is_product_exists(selected_product):
        print("The entered name product doesn't exist, please try again")
        return
    selected_quantity = int(input('Input quantity:  '))
    if selected_quantity < 0:
        print(f'Negative value is not acceptable')
        return

    product_id = bl.get_id_by_product(selected_product)
    result = bl.add_product_to_cart(product_id, selected_quantity)
    if result is not None:
        print(f'Ups! Max available quantity is {result}')
    print('Product has been added to cart.  ')


def remove_product_form_cart():
    selected_product = input('Choose product for remove from cart:  ').lower()
    if not bl.is_product_exists(selected_product):
        print("The entered name product doesn't exist, please try again")
        return
    product_id = bl.get_id_by_product(selected_product)
    bl.remove_product_from_cart(product_id)


def change_quantity_in_cart():
    selected_product = input('Choose product:  ').lower()
    if not bl.is_product_exists(selected_product):
        print("The entered name product doesn't exist, please try again")
        return
    selected_quantity = int(input('Input quantity: '))
    if selected_quantity < 0:
        print(f'Negative value is not acceptable')
        return
    product_id = bl.get_id_by_product(selected_product)
    result = bl.change_quantity_in_cart(product_id, selected_quantity)
    if result is not None:
        print(f'Ups! Max available quantity is {result}')
    print('Quantity has been change successfully. Call "menu"')


def show_cart():
    products_in_cart = bl.show_cart()
    if not products_in_cart:
        print("Cart is empty")
    print("In your cart has been added:")
    for product in products_in_cart:
        print(f' *{product["product_id"]:<5}* {product["product_name"]:^10} {product["quantity"]:} pcs ')


def prepare_order():
    bl.add_to_order_list()
    print(f'Your order has been added successfully\n')


def submit_order():
    products_list = bl.get_order_receipt()
    result_price = bl.get_order_price()
    for product in products_list:
        print(f'{product["product_id"]:<10} {product["product_name"]:^10} *{product["quantity"]:<10.3f} ${product["price"]:<10.2f} = ${product["price"]*product["quantity"]:<10.2f}')
    print("-"*53)
    print(f"total: ${result_price:.2f}")


def main_flow():
    menu_str = """
    Call menu by 'menu' command.
    Enter the number of your operation:
        1. Show all categories
        2. Show products in category
        3. Add a new product to cart
        4. Show cart
        5. Change a quantity
        6. Remove a product from cart
        7. Prepare order
        8. Submit oder
        0. Exit"""
    print(menu_str)
    while True:
        chose_action = show_query(message='Choose action: ')
        if chose_action == 'menu':
            print(menu_str)
        elif chose_action == '0':
            break
        elif chose_action == '1':
            show_wh_categories()
        elif chose_action == '2':
            show_products_by_category()
        elif chose_action == '3':
            add_product_to_cart()
        elif chose_action == '4':
            show_cart()
        elif chose_action == '5':
            change_quantity_in_cart()
        elif chose_action == '6':
            remove_product_form_cart()
        elif chose_action == '7':
            prepare_order()
        elif chose_action == '8':
            submit_order()
