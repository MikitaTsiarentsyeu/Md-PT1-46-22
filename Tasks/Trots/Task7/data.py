import copy

repo = {
    912: ['Lost', ["Serial", 'Adventure', "Mystery", "Science", "Supernatural"], 15, 100, 10.0, 912, 100],
    913: ['Breaking Bad', ['Serial', 'Triler', "Serious", "Drama"], 12, 120, 9.2, 913, 17],
    914: ['The Big Bang theory', ['Serial', 'Comedy', 'Old'], 5, 150, 8.3, 914, 14],
    915: ['Misfits', ['Serial', 'Comedy', 'New', "Supernatural"], 15, 80, 9.0, 915, 25],
    916: ['Prison Break', ['Serial', 'Crime', 'Triler', "Drama"], 20, 90, 8.7, 916, 16],
    917: ['Supernatural', ['Serial', 'Action', "Adventure", "Supernatural", "Mystery"], 11, 100, 7.9, 917, 7],
    918: ['Back to the Future', ['Movie', 'Comedy', 'Adventure'], 14, 18, 7.6, 918, 8],
    919: ['Bad Boys', ['Movie', 'Comedy', "Adventure"], 19, 29, 7.1, 919, 19],
    920: ['Ghostbusters', ['Movie', 'Comedy', "Supernatural"], 17, 35, 7.5, 920, 21]
}

cart = {}


def get_all_films():
    return repo.values()


def get_all_codes_films():
    return repo.keys()


def get_codes_cart():
    return cart.keys()


def get_all_category():
    category = []
    for v in repo.values():
        for i in v[1]:
            if i not in category:
                category.append(i)
    return category


def chose_category(name):
    category = get_all_category()
    try:
        choosen_category = category[name - 1]
    except IndexError:
        return False
    products = filter(lambda x: choosen_category in x[1], repo.values())
    return products


def add_to_cart(product_code, count):
    films = get_all_films()
    for f in films:
        if product_code == f[5]:
            if f[3] - count < 0:
                return False
            elif f[3] - count >= 0 and cart.get(product_code):
                repo[product_code][3] -= count
                cart[product_code][3] += count
            elif f[3] - count >= 0:
                cart[product_code] = copy.deepcopy(f)
                repo[product_code][3] -= count
                cart[product_code][3] = count
            return True
    return False


def delete_from_cart(product_code, count):
    if cart[product_code][3] - count <= 0:
        repo[product_code][3] += count
        del cart[product_code]
        return False
    cart[product_code][3] -= count
    repo[product_code][3] += count
    return True


def show_cart():
    return cart


def get_price_all():
    price = 0
    for f in cart.values():
        price += f[2] * f[3]
    return price


def buy():
    global cart
    cart = {}


def rate(product_code, rating):
    films = get_all_films()
    for i in films:
        if product_code == i[5]:
            repo[product_code][6] += 1
            rating = repo[product_code][4] = (repo[product_code][4] * repo[product_code][6] + rating) / (
                repo[product_code][6])
            return rating
    return False
