from cv2 import add
import bl
import data

def show_data(data):
    print(data)

def show_query(message):
    return input(message)

# def ask_for_name():
#     return show_query("Enter new name:\n")

# def ask_for_phone():
#     return show_query("Enter a new phone:\n")

# def ask_for_phones():
#     return show_query("Enter phones separated by a comma:\n").split(',')

def user_action_factory(method, phone = True, phones = False):
    def user_action():
        _name = ask_for_name()
        if phone:
            _phone = ask_for_phone()
        if phones:
            _phones = ask_for_phones()
        if not phone and not phones:
            return method(_name)
        return method(_name, _phone) if phone else method(_name, *_phones)

    return user_action


add_contact = user_action_factory(bl.add_contact, False, True)
remove_contact = user_action_factory(bl.remove_contact, False, False)
remove_phone = user_action_factory(bl.remove_phone)
search = user_action_factory(bl.search, False, False)

# def add_contact():
#     name = ask_for_name()
#     phones = ask_for_phones()
#     res = bl.add_contact(name, *phones.split(','))
#     show_data(res)

# def add_phone():
#     name = ask_for_name()
#     phone = ask_for_phone()
#     res = bl.add_phone(name, phone)
#     show_data(res)

# def remove_contact():
#     name = ask_for_name()
#     res = bl.remove_contact(name)
#     show_data(res)

# def remove_phone():
#     name = ask_for_name()
#     phone = ask_for_phone()
#     res = bl.remove_phone(name, phone)
#     show_data(res)

# def search():
#     name = ask_for_name()
#     res = bl.search(name)
#     show_data(res)

def main_flow():
    while True:
        chosed_action = show_query("""Enter the number of your operation:
        0. Exit
        1. Show all products
        2. Show categories
        3. Add a new contact
        4. Add a new phone
        5. Remove a contact
        6. Remove a phone
        7. Search for a contact by name\n""")
        if chosed_action == '0':
            break
        elif chosed_action == '1':
            data.get_all_products()
        elif chosed_action == '2':
            data.show_categories()
        elif chosed_action == '3':
            add_phone()
        elif chosed_action == '4':
            remove_contact()
        elif chosed_action == '5':
            remove_phone()
        elif chosed_action == '6':
            search()