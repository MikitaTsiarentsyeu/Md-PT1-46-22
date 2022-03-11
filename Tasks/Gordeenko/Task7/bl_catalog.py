import data_catalog

def get_all():
    catalog = data_catalog.get_all_catalog()
    return '\n'.join([f"{k[0]}: {','.join(k[1])}" for k in catalog])

def get_category():
    catalog_category = data_catalog.get_category_catalog()
    return '\n'.join([f"category -  {k}" for k in catalog_category])

def get_input_category():
    catalog_input_category = data_catalog.get_input_category_catalog()
    return ' - '.join([f"{k}" for k in catalog_input_category])


def add_order_dictionary():
    new_order = data_catalog.get_new_order()
    return new_order


def print_final_order_user():
    final_order_print = data_catalog.get_final_order()
    return final_order_print