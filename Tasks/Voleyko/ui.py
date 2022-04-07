import bl

def show_menu():
    menu = bl.menu()
    print(menu)
def search(id):
    print(bl.search(id))
def clean():
    print(bl.clean())
def len_basket():
    print(bl.len_basket())
def add_items(id,quantity):
    print( bl.add_items(id,quantity))
def remove_item(id):
    print(bl.remove_items(id))
def receipt():
    print(bl.get_receipt())


def main_flow():
    while True:
        chosed_action = input("""
        ---------------------------------------------------------
        Select a number for the action that you would like to do:

        1. View the menu
        2. Search product by id
        3. Add item to the basket
        4. Remove item from the basket
        5. How many items on the basket
        6. Clear basket
        7. Make order
        8. Exit
        
        """)
        if chosed_action == '1':
            show_menu()
        elif chosed_action == '2':
            id = int(input('Please,enter id of the item: '))
            search(id)            
        elif chosed_action == '3':
            id = int(input('Please,enter id of the item: '))
            quantity = int(input('Please,enter quantity of items: '))
            add_items(id,quantity)        
        elif chosed_action == '4':
            id = int(input('Please,enter id of the item: '))
            remove_item(id)          
        elif chosed_action == '5':
            len_basket()            
        elif chosed_action == '6':
            clean()         
        elif chosed_action == '7':
            receipt() 
        elif chosed_action == '8':
            print('Goodbye! Have a good day!')
            break 

