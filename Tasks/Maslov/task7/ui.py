import bl


def show_data(data):
    print(data)


def show_query(message):
    return input(message)


def show_all_spare_parts():
    data = bl.get_all()
    show_data(data)


def show_category_spare_parts():
    category = bl.get_category_spare_part()
    show_data(category)


def dob():
    res = bl.get_dob()
    show_data(res)


def show_remais():
    remais = bl.get_remais()
    show_data(remais)


def show_basket():
    baskets = bl.get_basket()
    show_data(baskets)


def checkout():
    cat = show_query("1.Оформить заказ?:\n")
    full_name = show_query("Имя,фамилия:")
    country = show_query("Страна,Город:")
    adress = show_query("Адресс:")
    zakaz = (cat, full_name, country, adress, 'Успешно отправлено')
    show_data(zakaz)


def add_spare_part():
    category = show_query("Введите категорию запчасти:\n")
    title = show_query("Введите новое название запчасти:\n")
    kod = show_query("Введите код запчасти:\n")
    price = show_query('Введите цену для запчасти:\n')
    res = bl.add_spare_part(category, title, kod, price)
    show_data(res)


def main_flow():
    while True:
        chosed_action = show_query(
            "Введите номер вашей операции:\n0.Выход\n1.Показать все запчасти\n2.Выбрать категорию запчастей\n3.Добавить новую запчасть\n4.Остатки товара на складе\n5.Добавить в корзину\n6.Корзина\n")
        if chosed_action == '0':
            break
        elif chosed_action == '1':
            show_all_spare_parts()
        elif chosed_action == '2':
            show_category_spare_parts()
        elif chosed_action == '3':
            add_spare_part()
        elif chosed_action == '4':
            show_remais()
        elif chosed_action == '5':
            dob()
        elif chosed_action == '6':
            show_basket()
            checkout()