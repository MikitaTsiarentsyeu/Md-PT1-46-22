import bl

def show_data(data):
    print(data)

def show_query(message):
    return input(message)

def search_by_type(type):
    value = show_query(f'Enter the {type} of books you\'d like to display\n').lower()
    res = bl.search_by_type(type,value)
    show_data(res)

def add_basket():
    name = show_query("Enter a name of the book to add\n").lower()
    number = show_query("Enter a number of books you want to purchase\n")
    res = bl.add_basket(name, number)
    show_data(res)

def show_basket():
    show_data(bl.show_basket())

def make_order():
    res = bl.make_order()
    show_basket()
    bl.clean_basket()
    show_data(res)


def main():
    while True:
        chosen_action = show_query("""
        ***Welcome to the BookWorm store***
        
        0. Exit
        1. Search for book by name
        2. Show books of certain category
        3. Show books by a certain author
        4. Add a book / books to the basket
        5. Show basket
        6. Make an order

        """)
        if chosen_action == '0':
            break
        elif chosen_action == '1':
            search_by_type('name')
        elif chosen_action == '2':
            search_by_type('category')
        elif chosen_action == '3':
            search_by_type('author')
        elif chosen_action == '4':
            add_basket()
        elif chosen_action == '5':
            show_basket()
        elif chosen_action == '6':
            make_order()
        else:
            show_data("Invalid input. There is no such an option in our store.")