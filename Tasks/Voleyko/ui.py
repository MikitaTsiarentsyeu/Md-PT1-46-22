import bl

def show_menu():
    menu = bl.menu()
    return menu
def search(id):
    return bl.search(id)
def clean():
    return bl.clean()
def len_basket():
    return bl.len_basket()
def add_items(id,quantity):
    return bl.add_items(id,quantity)
def remove_item(id):
    return bl.remove_items(id)
def receipt():
    return bl.get_receipt()


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
            print(show_menu())
        elif chosed_action == '2':
            id = int(input('Please,enter id of the item: '))
            print(search(id))            
        elif chosed_action == '3':
            id = int(input('Please,enter id of the item: '))
            quantity = int(input('Please,enter quantity of items: '))
            print(add_items(id,quantity))            
        elif chosed_action == '4':
            id = int(input('Please,enter id of the item: '))
            print(remove_item(id))           
        elif chosed_action == '5':
            print(len_basket())            
        elif chosed_action == '6':
            print(clean())          
        elif chosed_action == '7':
            print(receipt())   
        elif chosed_action == '8':
            print('Goodbye! Have a good day!')
            break 
