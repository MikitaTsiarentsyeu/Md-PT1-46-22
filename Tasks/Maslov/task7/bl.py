import data


def get_all():
    pare_parts = data.get_all_spare_parts()
    for something in pare_parts:
        print(f'{(something[0])} : {something[1]} - {something[2]} ')


def get_category_spare_part():
    category_pare_parts = data.get_category_spare_parts()
    return category_pare_parts


def get_remais():
    pare_parts = data.get_all_spare_parts()
    return '\n'.join([f"{''.join(c[0])} - {len(c[1])} шт." for c in pare_parts])


def get_dob():
    res = data.dob()
    if res:
        return "Успешно!"
    else:
        return "Что-то пошло не так..."


def get_basket():
    res = data.basket()
    return res


def add_spare_part(category, title, kod, price):
    res = data.add_spare_part(category, title, kod, price)
    if res:
        return "Успешно!"
    else:
        return "Что-то пошло не так..."

