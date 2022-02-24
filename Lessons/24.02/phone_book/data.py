"""TO DO: IMPLEMENT FACTORY FOR MAIN METHODS"""

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

def add_phone(name, phone):
    for v in repo.values():
        if v[0] == name:
            if phone not in v[1]:
                v[1].append(phone)
                return True
            else:
                return False
    raise NameError("No such name in the phone book")

def remove_contact(name):
    for k, v in repo.items():
        if v[0] == name:
            del repo[k]
            return True
    raise NameError("No such name in the phone book")


def remove_phone(name, phone):
    for v in repo.values():
        if v[0] == name:
            if phone in v[1]:
                v[1].remove(phone)
                return True
            else:
                return False
    raise NameError("No such name in the phone book")


def search(name):
    for v in repo.values():
        if v[0] == name:
            return v
    return False