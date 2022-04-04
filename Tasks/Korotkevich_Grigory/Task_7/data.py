repo = {"Fruit" : ("pineapple", ["54578365","54809642"]),
    "Vegetables" : ("cucumbers", ["63809242","63575365"]),
    "Drinks" : ("fanta", ["98766689"])}

repo_price = {
    "54578365":("4.84","50"),
    "54809642":("4.29","48"),
    "63809242":("1.95","32"),
    "63575365":("2.10","38"),
    "98766689":("2.08","54")
    }


def get_all_catalog():
    return repo.values()

def get_category_catalog():
    return repo.keys()

def get_input_category_catalog():
    input_category_items = input(f"Enter a category to view items in that category\n")
    return repo.get(input_category_items)

new_order_dictionary = {}

def get_new_order():
    input_product_code = input(f"Enter the product code\n")
    input_product_quantity = input(f"Enter product quantity\n")
    new_order_dictionary[input_product_code] = input_product_quantity
    return new_order_dictionary.items()


def get_final_order():
    return new_order_dictionary.items()
