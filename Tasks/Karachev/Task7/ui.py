from unicodedata import digit
import bl

def show_data(data):
    print(data)

def show_query(message):
    return input(message)

def get_animals():
    data = bl.show_animals()
    show_data(data)

def get_pet_food():
    data = bl.show_pet_food()
    show_data(data)

def ask_rep():
    return show_query("Enter 1 to choose products from animal category, and 2 from food category:\n")        

def ask_code():
    return show_query("Enter the code of the product you want to add:\n")

def get_cart():
    print("Items in the cart:")
    data = bl.show_cart()
    show_data(data)

def add_cart():
    rep = ask_rep()
    code = ask_code()
    res = bl.add_cart(code, rep)
    show_data(res)


def del_cart():
    res = bl.del_cart()
    show_data(res)

def confirme_cart():
    res = bl.confirme_cart()
    show_data(res)


def main_flow():
    while True:
        chosed_action = show_query("""Enter the number of your operation:
        0. Exit
        1. Show animals category
        2. Show food for animals category
        3. Show the cart
        4. Add to the cart
        5. Clear the cart
        6. Confirm your purchase
        """)
        if chosed_action == '0':
            break
        elif chosed_action == '1':
            get_animals()
        elif chosed_action == '2':
            get_pet_food()
        elif chosed_action == '3':
            get_cart()
        elif chosed_action == '4':
            add_cart()
        elif chosed_action == '5':
            del_cart()
        elif chosed_action == '6':
            confirme_cart()
        
        