import data

def get_all():
    contacts = data.get_all_contacts()
    return '\n'.join([f"{c[0]}: {','.join(c[1])}" for c in contacts])

def add_contact(name, *phones):
    correct_phones = []
    incorrect_phones = []
    for phone in phones:
        try:
            validate_phone_by_error(phone)
            correct_phones.append(phone)
        except ValueError:
            incorrect_phones.append(phone)
    res = data.add_contact(name, *correct_phones)
    if res:
        phones_added = "all phones were added"
        final_message = phones_added if len(incorrect_phones) == 0 else phones_added + f", except for {','.join(incorrect_phones)}"
        return f"The new contact was created, {final_message}"
    else:
        return "Something went wrong..."

def add_phone(name, phone):
    # validation_result = validate_phone_by_if(phone)
    # try:
    #     validation_result = validate_phone_by_number(phone)
    # except ValueError:
    #     return "The phone number should consist of 7 digits"
    # if not validation_result:
    #     return "The phone number should consist of 7 digits"
    try:
        validate_phone_by_error(phone)
    except ValueError:
        return "The phone number should consist of 7 digits"
    try:
        res = data.add_phone(name, phone)
    except NameError as er:
        return str(er)
    except:
        return "Something went wrong..."
    if res:
        return "Success!"
    else:
        return "The number is already present in the list"

def remove_contact(name):
    try:
        res = data.remove_contact(name)
    except NameError as er:
        return str(er)
    if res:
        return "The contact was removed"
    else:
        return "Something went wrong"

def remove_phone(name, phone):
    try:
        validate_phone_by_error(phone)
    except ValueError:
        return "The phone number should consist of 7 digits"
    try:
        res = data.remove_phone(name, phone)
    except NameError as er:
        return str(er)
    except:
        return "Something went wrong..."
    if res:
        return "Success!"
    else:
        return "The number is not present in the list"

def search(name):
    res = data.search(name)
    if res:
        return f"{res[0]}: {','.join(res[1])}"
    else:
        return "nothing was found"

def validate_phone_by_if(phone):
    if phone.isdigit() and len(phone) == 7:
        return True
    return False

def validate_phone_by_number(phone):
    phone = int(phone)
    if phone >= 1000000 and phone < 100000000:
        return True
    return False

def validate_phone_by_error(phone):
    phone = int(phone)
    if phone < 1000000 and phone >= 100000000:
        raise ValueError