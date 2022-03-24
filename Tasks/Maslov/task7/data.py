repo = {1: ('Кпп', ['Вилка КПП 5320'], ['14-1702033'], ['39,01']),
        2: ('Двс', ['Клапан электромагнитный'], ['64226-1115030'], ['55,40']),
        3: ('Кузов', ['Крыло кабины'], ['5336-8403016'], ['88,32'])}


def get_all_spare_parts():
    return repo.values()


def get_category_spare_parts():
    return repo.values()


shopping_cart = []


def basket(title):
    new_spare_part=(title)
    for i in repo:
        if i in repo:
            repo[i] = new_spare_part
            return True




def add_spare_part(category, title, kod, price):
    try:
        new_spare_part = (category, title, kod, price)
        for i in range(1, len(repo) + 2):
            if i not in repo:
                repo[i] = new_spare_part
        return True
    except:
        return False
