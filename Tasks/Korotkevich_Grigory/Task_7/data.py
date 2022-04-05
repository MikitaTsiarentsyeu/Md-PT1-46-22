repo = {"greengrocery" : ("apple", ["111648531","111455687"]),
    "bakery" : ("bread", ["333158435","333671524","333648253"]),
    "stationers" : ("stapler", ["555364899"])}

repo_price = {
    "111648531":("3.75","30"),
    "111455687":("3.19","45"),
    "222564899":("4.05","12"),
    "333158435":("1.15","120"),
    "333671524":("1.55","99"),
    "333648253":("1.67","57"),
    "444157731":("18.45","21"),
    "444647253":("32.75","11"),
    "444964827":("13.7","3"),
    "555364899":("11.05","10")
    }


def get_all_catalog():
    return repo.values()

def get_category_catalog():
    return repo.keys()

def get_input_category_catalog():
    input_category_items = input(f"Enter a category to view items in that category (for example: greengrocery, bakery...)\n")
    return repo.get(input_category_items)

new_order_dictionary = {}

def get_new_order():
    input_product_code = input(f"Enter the product code\n")
    input_product_quantity = input(f"Enter product quantity\n")
    new_order_dictionary[input_product_code] = input_product_quantity
    #print(new_order_dictionary)
    return new_order_dictionary.items()


def get_final_order():
    return new_order_dictionary.items()