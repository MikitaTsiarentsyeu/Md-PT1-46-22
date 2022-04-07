import bl

def main_flow():
    while True:
        choose_action = show_query(
        '''\n<<< Main menu >>>\nEnter the number of your operation:
        0. Exit
        1. Show all spare parts
        2. Show all categories
        3. Add to a cart
        4. Show a cart
        5. Search by id number
        6. Search by name
        7. Make an order\n''')
        if choose_action == '0':
            break 
        elif choose_action == '1':
            show_catalogue()
        elif choose_action == '2':
            show_categories()
            category_flow()
        elif choose_action == '3':
            add_to_cart()
        elif choose_action == '4':
            show_my_cart()
            cart_flow()
        elif choose_action == '5':
            search_by_id()
        elif choose_action == '6':
            search_name()
        elif choose_action == '7':
            make_an_order()
            
def cart_flow():
    while True:
        choose_action = show_query(
        '''\n<<< Your cart menu >>>\nEnter the number of your operation:
        0. Exit
        1. Change quantity of item
        2. Remove all from your cart
        3. Remove some spare part from your cart
        4. Make an order\n''')
        if choose_action == '0':
            break
        elif choose_action == '1':
            change_quantity()
            show_my_cart()
        elif choose_action == '2':
            remove_all_from_cart()
            show_my_cart()
        elif choose_action == '3':
            remove_one()
            show_my_cart()
        elif choose_action == '4':
            make_an_order()

def category_flow():
    while True:
        choose_action = show_query(
        '''\n<<< Category menu >>>\nEnter the number of your operation:
        0. Exit
        1. Choose category
        2. Add to a cart
        3. Show a cart\n''')
        if choose_action == '0':
            break
        elif choose_action == '1':
            choose_category()
        elif choose_action == '2':
            add_to_cart()
        elif choose_action == '3':
            show_my_cart()
            cart_flow() 

def change_quantity():
    id = show_query('Enter id of the spare part which quantity you want to change:\n')
    value = show_query('Enter a new quantity of selected spare part:\n')
    res = bl.change_quantity_in_cart(int(id), int(value))
    show_data(res)

def show_catalogue():
    res = (f'\nOur catalogue:\n{bl.get_all()}')
    show_data(res)

def show_categories():
    res = bl.get_categories()
    show_data(res)

def choose_category():
    name = show_query('Enter the name of category:\n')
    res = bl.get_category(name)
    show_data(res)

def add_to_cart():
    id = show_query('Enter id of the spare part which you want to add:\n')
    res = bl.add_to_cart(id)
    show_data(res)

def remove_all_from_cart():
    res = bl.remove_all_from_cart()
    show_data(res)

def remove_one():
    id = show_query('Enter an id of the spare part which you want to remove\n')
    res = bl.remove_one(id)
    show_data(res)

def show_my_cart():
    res = f'\nYour cart:\n{bl.show_cart()}'
    show_data(res)

def search_by_id():
    id = show_query('Enter an id of the spare part for search:\n')
    res = bl.search_by_id(id)
    show_data(res)

def search_name():
    name = show_query('Enter the name of the spare part\n')
    res = bl.search_name(name)
    show_data(res)

def make_an_order():
    choice = show_query('If you want to confirm your order enter "Y", if you want to decline your order enter "N":\n')
    res = bl.make_an_order(choice)
    show_data(res)

def show_data(data):
    print(data)

def show_query(message):
    return input(message)
    