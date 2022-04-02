repo = {'Кпп': ('Вилка КПП 5320', ['14-1702033'], ['39,01 руб.']),
        'Двс': ('Клапан электромагнитный', ['64226-1115030'], ['55,40 руб.']),
        'Кузов': ('Крыло кабины', ['5336-8403016'], ['88,32 руб.'])}


def get_all_spare_parts():
    return repo.values()


def get_category_spare_parts():
    for key, value in repo.items():
        print(key, ':', value[0], value[1], '-', value[2])

shop={}
def dob():
    kod = input(f"Введите код запчасти\n")
    title = input(f"Введите код запчасти\n")
    shop[kod] = title
    return shop.items()
def basket():
    return shop.items()


def add_spare_part(category, title, kod, price):
    try:
        new_spare_part = (category, title, kod, price)
        for i in range(1, len(repo) + 2):
            if i not in repo:
                repo[i] = new_spare_part
        return True
    except:
        return False
