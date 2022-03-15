import bl


def input_test(message):
    if not message.isdigit():
        print("------------------------------")
        print('Please enter an integer value.')
        print("------------------------------")
        return False
    return True


def show_data(data):
    print("-------------------------------------------------------------")
    print(data)
    print("-------------------------------------------------------------")


def show_querry(message):
    flag = False
    while not flag:
        enter = input(message)
        flag = input_test(enter)
    return int(enter)


def show_all_films():
    data = bl.get_all()
    show_data(data)


def show_all_categories():
    data = bl.get_all_category()
    show_data(data)


def choose_category():
    number = int(show_querry("Enter the number of the desired category."))
    data = bl.choose_category(number)
    show_data(data)


def add_to_cart():
    product_code = int(show_querry('Enter the product code\n'))
    count = int(show_querry("How many items do you want to add to your cart?\n"))
    show_data(bl.add_to_cart(product_code, count))


def delete_from_cart():
    product_code = int(show_querry('Enter the product code\n'))
    count = int(show_querry("How many items do you want to remove from the cart?\n"))
    show_data(bl.delete_from_cart(product_code, count))


def show_price_all():
    show_data(bl.get_price_all())


def show_basket():
    show_data(bl.show_cart())
    show_price_all()


def buy():
    show_data(bl.buy())


def rate():
    product_code = show_querry('Enter the product code\n')
    rating = show_querry('Enter your rating from 1 to 10\n')
    show_data(bl.rate(product_code, rating))


def main_flow():
    while True:
        chossed_action = show_querry(
            "Enter an action number:\n\n0. Exit.\n1. Show all films.\n2. Choose a movie category\n3. Add to cart\n4. "
            "Show cart\n5. Rate film.\n") 
        if chossed_action == 0:
            break
        elif chossed_action == 1:
            show_all_films()
        elif chossed_action == 2:
            show_all_categories()
            choose_category()
            while True:
                choosen_value_on_category = show_querry('Choose:\n0. Back to menu;\n1. Choose another category.\n')
                if choosen_value_on_category == 0:
                    break
                elif choosen_value_on_category == 1:
                    show_all_categories()
                    choose_category()
                else:
                    show_data('Please enter the correct value.')
        elif chossed_action == 3:
            while True:
                choosen_value_on_category = show_querry(
                    'Choose:\n0. Back to menu;\n1. Enter the product code of the product you want to add to cart:\n2. '
                    'Show products in cart.\n') 
                if choosen_value_on_category == 0:
                    break
                elif choosen_value_on_category == 1:
                    add_to_cart()
                elif choosen_value_on_category == 2:
                    show_basket()
                else:
                    show_data('Please enter the correct value.')
        elif chossed_action == 4:
            show_basket()
            while True:
                choosen_value_on_category = show_querry(
                    'Choose:\n0. Back to menu;\n1. Remove an item from the cart.\n2. Buy.\n')
                if choosen_value_on_category == 0:
                    break
                elif choosen_value_on_category == 1:
                    delete_from_cart()
                elif choosen_value_on_category == 2:
                    buy()
                else:
                    show_data('Please enter the correct value.')
        elif chossed_action == 5:
            rate()
        else:
            show_data('Please enter the correct value.')
