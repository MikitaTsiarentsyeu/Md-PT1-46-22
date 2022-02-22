import bl

def show_data(data):
    print(data)

def show_query(message):
    return input(message)

def show_all_contacts():
    data = bl.get_all()
    show_data(data)

def add_contact():
    name = show_query("Enter new name:\n")
    phones = show_query("Enter phones separated by a comma:\n")
    res = bl.add_contact(name, *phones.split(','))
    show_data(res)

def main_flow():
    while True:
        chosed_action = show_query("Enter the number of your operation:\n0. Exit\n1. Show all contacts\n2. Add a new contact\n")
        if chosed_action == '0':
            break
        elif chosed_action == '1':
            show_all_contacts()
        elif chosed_action == '2':
            add_contact()