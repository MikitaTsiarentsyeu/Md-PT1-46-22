import bl


def show_data(data):
    print(data)


def show_query(message):
    return input(message)


def show_all_spare_parts():
    data = bl.get_all()
    show_data(data)


def show_category_spare_parts_kyzov():
    category = bl.get_category_spare_part_kyzov()
    show_data(category)


def show_category_spare_parts_kpp():
    category = bl.get_category_spare_part_kpp()
    show_data(category)


def show_remais():
    remais = bl.get_remais()
    show_data(remais)


def show_basket():
    baskets = bl.get_basket()
    show_data(baskets)


def show_basket1():
    baskets = bl.get_basket1()
    show_data(baskets)


def show_basket2():
    baskets = bl.get_basket2()
    show_data(baskets)


def checkout():
    cat = show_query("1.Оформить заказ?:\n")
    full_name = show_query("Имя,фамилия:")
    country = show_query("Страна,Город:")
    adress = show_query("Адресс:")
    zakaz = (cat, full_name, country, adress, 'Успешно отправлено')
    show_data(zakaz)


def show_category_spare_parts_dvs():
    category = bl.get_category_spare_part_dvs()
    show_data(category)


def show_basket5():
    basket1 = show_basket()
    basket2 = show_basket1()
    basket3 = show_basket2()
    res = (basket3, basket2, basket1)
    show_data(res)


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
            "Введите номер вашей операции:\n0.Выход\n1.Показать все запчасти\n2.Выбрать категорию запчастей\n3.Добавитьтк новую запчасть\n4.Остатки товара на складе\n5.Корзина\n")
        if chosed_action == '0':
            break
        elif chosed_action == '1':
            show_all_spare_parts()
        elif chosed_action == '2':
            category = show_query("\n0.Выход\n1.Кузов\n2.Кпп\n3.Двс\nВведите номер вашей операции:\n")
            show_data(category)
            if category == '0':
                show_data(main_flow())
            elif category == '1':
                if category == '0':
                    category = show_query("\n0.Выход\n1.Кузов\n2.Кпп\n3.Двс\nВведите номер вашей операции:\n")
                    show_data(category)
                elif category == '1':
                    show_data(show_category_spare_parts_kyzov())
                    category = show_query('\n0.Выход\n1.Добавить в корзину?\n')
                    show_data(category)
                    if category == '1':
                        show_basket1()

            elif category == '2':
                if category == '0':
                    category = show_query("\n0.Выход\n1.Кузов\n2.Кпп\n3.Двс\nВведите номер вашей операции:\n")
                    show_data(category)
                elif category == '2':
                    show_data(show_category_spare_parts_kpp())
                    category = show_query('\n0.Выход\n1.Добавить в корзину?\n')
                    show_data(category)
                    if category == '1':
                        show_basket()



            elif category == '3':
                if category == '0':
                    category = show_query("\n0.Выход\n1.Кузов\n2.Кпп\n3.Двс\nВведите номер вашей операции:\n")
                    show_data(category)
                elif category == '3':
                    show_data(show_category_spare_parts_dvs())
                    category = show_query('\n0.Выход\n1.Добавить в корзину?\n')
                    show_data(category)
                    if category == '1':
                        show_basket2()

        elif chosed_action == '3':
            add_spare_part()
        elif chosed_action == '4':
            show_remais()
        elif chosed_action == '5':
            show_basket5()
            show_data(checkout())
