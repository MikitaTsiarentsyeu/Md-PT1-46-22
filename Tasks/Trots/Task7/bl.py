import data


def get_all():
    films = data.get_all_films()
    return '\n'.join([f"Title: {f[0]}. Genre - {','.join(f[1])}. Product code - {f[5]}. Price - {f[2]}$.  In stock - {f[3]}. Rating - {f[4]:.2f}. Reviews - {f[6]}"for f in films])


def get_all_category():
    category = data.get_all_category()
    return "\n".join([f"{i + 1}. {category[i]}" for i in range(0, len(category))])


def choose_category(name):
    choose = data.chose_category(name)
    if choose:
        return "\n".join(
            [f"Title: {c[0]}. Product code - {c[5]}. Rating - {c[4]:.2f}. Price - {c[2]}$." for c in choose])
    else:
        return "There is no such category."


def add_to_cart(product_code, count):
    products = data.get_all_codes_films()
    if product_code not in products:
        return 'There is no product with this product code.'
    elif data.add_to_cart(product_code, count):
        return f'This product was successfully added to your cart.'
    return 'The specified number of items in stock is missing.'


def delete_from_cart(product_code, count):
    products = data.get_codes_cart()
    if product_code not in products:
        return "There is no such item in the cart"
    if data.delete_from_cart(product_code, count):
        return 'Product removed from the cart.'
    return f'The item is completely removed from the cart.'


def show_cart():
    cart = data.show_cart()
    if cart == {}:
        return "Your shopping cart is empty."
    cart_values = cart.values()
    return "In your cart:\n" + '\n'.join(
        [f"Movie - {f[0]}. Genre - {','.join(f[1])}. Product code - {f[5]}. Number of items in cart - {f[3]}" for f in
         cart_values])


def get_price_all():
    return f'Total price is {data.get_price_all()}$'


def buy():
    summ = data.get_price_all()
    data.buy()
    return f'Thank you for choosing us. You paid - {summ}$'


def rate(product_code, rating):
    if not data.rate(product_code, rating):
        return f"There is no product with this product code"
    elif not (1 <= rating <= 10):
        return f"The rating value should be from 1 to 10"
    rating = data.rate(product_code, rating)
    return f'Thanks for the review. New rating is {rating:.2f}'
