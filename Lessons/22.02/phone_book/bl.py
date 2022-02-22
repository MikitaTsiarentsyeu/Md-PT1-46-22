import data

def get_all():
    contacts = data.get_all_contacts()
    return '\n'.join([f"{c[0]}: {','.join(c[1])}" for c in contacts])

def add_contact(name, *phones):
    res = data.add_contact(name, *phones)
    if res:
        return "Success!"
    else:
        return "Something went wrong..."

def add_phone(name, phone): pass

def remove_contact(name): pass

def remove_phone(name, phone): pass

def search(name): pass