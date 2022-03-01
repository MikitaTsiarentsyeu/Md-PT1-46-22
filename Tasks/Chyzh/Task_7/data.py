"""TO DO: IMPLEMENT FACTORY FOR MAIN METHODS"""

repo = {1 : (["electronics", "PC"], ["2602111", "400"]), 
        2 : (["electronics", "notebook"], ["2602112", "700"]),
        3 : (["electronics", "smartphone"], ["2602113", "500"]),
        4 : (["electronics", "TV"], ["2602114", "1100"]),
        5 : (["network", "router"], ["2802111", "50"]),
        6 : (["network", "switch"], ["2802112", "300"]),
        7 : (["network", "POEinjector"], ["2802113", "30"]),
        8 : (["tools", "drill"], ["2202111", "200"]),
        9 : (["tools", "screwdriver"], ["2202112", "100"]),
        10 : (["tools", "milling_machine"], ["2202113", "400"]),
        11 : (["tools", "planer"], ["2202114", "150"])
        }


def get_all_products():
    for i in repo:
        return repo.items(i[0])

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