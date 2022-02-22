repo = {1 : ("some name", ["25646547", "5465472"]), 2 : ("test name", ["6576575"])}

def get_all_contacts():
    return repo.values()

def add_contact(name, *phones):
    try:
        new_contact = (name, list(phones))
        for i in range(1, len(repo)+2):
            if i not in repo:
                repo[i] = new_contact
        return True
    except:
        return False

def add_phone(name, phone): pass

def remove_contact(name): pass

def remove_phone(name, phone): pass

def search(name): pass