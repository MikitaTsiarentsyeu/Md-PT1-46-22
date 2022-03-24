import data


def get_all():
    pare_parts = data.get_all_spare_parts()
    return '\n'.join([f"{c[0]}: {''.join(c[1])},{''.join(c[2])} - {''.join(c[3])}, руб." for c in pare_parts])


cart = []


def get_category_spare_part_dvs():
    category_pare_parts = data.get_category_spare_parts()
    prices = [product[1] for product in category_pare_parts if product[0] == 'Двс']

    return prices[0]


def get_category_spare_part_kpp():
    category_pare_parts = data.get_category_spare_parts()
    prices = [product[1] for product in category_pare_parts if product[0] == 'Кпп']
    return prices[0]


def get_category_spare_part_kyzov():
    category_pare_parts = data.get_category_spare_parts()
    prices = [product[1] for product in category_pare_parts if product[0] == 'Кузов']
    return prices[0]


def get_remais():
    pare_parts = data.get_all_spare_parts()
    return '\n'.join([f"{''.join(c[1])} - {len(c[1])} шт." for c in pare_parts])


shop = []


def get_basket():
    name = get_category_spare_part_kpp()
    if name == 'Кпп':
        shop.append(name)
    print("{0} has been added".format(name))

def get_basket1():
    name1 = get_category_spare_part_kyzov()
    if name1 == 1:
        shop.append(name1)
    print("{0} has been added".format(name1))

def get_basket2():
    name2 = get_category_spare_part_dvs()
    if name2 == 'Двс':
        shop.append(name2)
    print("{0} has been added".format(name2))



def add_spare_part(category, title, kod, price):
    res = data.add_spare_part(category, title, kod, price)
    if res:
        return "Успешно!"
    else:
        return "Что-то пошло не так..."
