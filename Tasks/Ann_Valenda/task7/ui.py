import bl
#
#
# def show_data(data):
#     print(data)
#
#
def show_query(message):
    return input(message)
#
#
# def ask_for_category():
#     return show_query("Choose category:\n")
#
#
# def ask_for_product():
#     return show_query("Choose a product:\n")
#
#
# def ask_for_quantity():
#     return show_query("Enter quantity:\n")
#
# def ask_for_change_quantity():
#     return show_query("Enter new quantity:\n")
#
# #
# # def show_wh_products():
# #     data = bl.get_wh_products()
# #     show_data(data)
#
#
# def user_action_factory(method, category=None, product_name=None):
#     def user_action():
#         _category = ask_for_category()
#         if category == ['category']:
#             _product = ask_for_product()
#         if product_name == ['product_name']:
#             _quantity = ask_for_quantity()
#         if not category and not product_name:
#             return method(_category)
#
#
#     return user_action
#
#
# show_category = user_action_factory(bl.get_wh_category())
# add_to_cart = user_action_factory(bl.add_to_cart)
# remove_product_ = user_action_factory(bl.remove_product_from_cart)


def show_wh_categories():
    for index, category in enumerate(bl.get_wh_categories()):
        print(f'category №{index + 1} - {category}')
    print()


def show_products_by_category():
    selected_category = input('choose category please:  ')
    # some verification
    products = bl.get_product_by_category(selected_category)
    for product in products:
        print(f'{product["product_name"]}   |{product["price"]}$ | {product["quantity"]} products available')
    print()


def add_product_to_cart():
    selected_product = input('choose product please:  ')
    selected_quantity = int(input('input quantity please:  '))
    # some verification
    product_id = bl.get_id_by_product(selected_product)
    bl.add_product_to_cart(product_id, selected_quantity)


def remove_product_form_cart():
    selected_product = input('choose product for remove from cart please:  ')
    product_id = bl.get_id_by_product(selected_product)
    bl.remove_product_from_cart(product_id)

def change_quantity_in_cart():
    """Если хочешь изменить значение в меньшую сторону - набирай "-n", в большую - "n" """
    selected_product = input('choose product please:  ')
    selected_quantity = int(input('input quantity please:  '))
    # some verification
    product_id = bl.get_id_by_product(selected_product)
    bl.change_quantity_in_cart(product_id, selected_quantity)


def show_cart():
    print(f'{bl.show_cart()}')


def prepare_order():
    bl.add_to_order_list()
    print(f'Your order added successfully\n')



def submit_order():
    bl.get_order_receipt()
    bl.get_order_price()
    # return f"Product: {list_order}, quantity: \n Order price is: {order_price} $\n Thank you for order!"



# def show_menu():
#     input('if you want see menu, input "menu":')


def main_flow():
    while True:
        chose_action = show_query("""Enter the number of your operation:
            1. Show all categories
            2. Show products in category
            3. Add a new product to cart
            4. Show cart
            5. Change a quantity
            6. Remove a product from cart
            7. Prepare order
            8. Submit oder
            0. Exit""")
        if chose_action == '0':
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


