import data

def show_animals():
    animals = data.show_all_animals()
    return '\n'.join([f"{c[0]}: color - {c[1]}, code - {c[2]}, price - {c[3]} byn, amount - {c[4]} pcs" for c in animals])


def show_pet_food():
    food = data.show_all_pet_food()
    return '\n'.join([f"{c[0]}: weight - {c[1]}, code - {c[2]}, price - {c[3]} byn, amount - {c[4]} pcs" for c in food])

def show_cart():
    prod = data.show_all_cart()    
    return '\n'.join([f"{c[0]}: description - {c[1]}, code - {c[2]}, price - {c[3]} byn" for c in prod])

def add_cart(code, rep):
    validation_result1 = validate_rep(rep)
    validation_result2 = validate_code(code, rep)
    if validation_result1 and validation_result2 :
        rep = int(rep)
        code = int(code)        
        data.add_cart(code, rep)    
        return "Item has been added to the cart"
    else:   
        return "You choose wrong category or code"

def del_cart():
    data.del_cart()
    return "All items in the cart have been deleted"

def confirme_cart():
    data.confirme_cart()    
    return "Purchase has been confirmed and added to the cart.txt"
    
def validate_rep(rep):    
    if rep.isdigit() and (rep =="1" or rep == "2"):        
        return True
    return False

def validate_code(code, rep):     
    if code.isdigit() and data.search_code(code, rep):        
        return True
    return False    