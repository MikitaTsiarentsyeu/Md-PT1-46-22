import bl

def show_data(data):
    print(data)

def show_data(data_):
    print(data_)

def show_data(data_input):
    print(data_input)

def show_query(message):
    return input(message)

def show_data(order):
    print(order)

def show_data(final_order):
    print(final_order)

def show_all_catalog():
    data = bl.get_all()
    show_data(data)

def show_category_catalog():
    data_ = bl.get_category()
    show_data(data_)

def show_input_category_catalog():
    data_input = bl.get_input_category()
    show_data(data_input)

def add_order():
    order = bl.add_order_dictionary()
    show_data(order) 

def print_final_order():
    final_order = bl.print_final_order_user()
    show_data(final_order) 

def main_flow():
    while True:
        chosed_action = show_query("""\nEnter the number of your operation:
        0. Exit
        1. Show all catalog
        2. Show catalog categories
        3. Show input catalog categories
        4. Add order
        5. Final order\n""")
        if chosed_action == '0':
            break
        elif chosed_action == '1':
            show_all_catalog()
        elif chosed_action == '2':
            show_category_catalog()
        elif chosed_action == '3':
            show_input_category_catalog()
        elif chosed_action == '4':
            add_order()
        elif chosed_action == '5':
            print_final_order() 
