animals = {2955: ("Hamster", "grey", "2955", 10, 5), 2855: ("Golden fish", "orange", "2855", 8, 20), 2566: ("Rabbit", "white", "2566", 20, 4)}
pet_food = {4544: ("Bird food", "1000 g", "4544", 6, 10), 4568: ("Fish food", "950 g", "4568", 5, 40), 4855: ("Hamster food", "450 g", "4855", 20, 20)}
cart = []
def show_all_animals():    
    return animals.values()

def show_all_pet_food():
    return pet_food.values()

def search_code(code, rep):
    if rep == "1":
        for v in animals.values():
            if v[2] == code:
                return True
    elif rep == "2":
        for v in pet_food.values():
            if v[2] == code:
                return True    
    return False

def show_all_cart():
    return cart

def add_cart(code, rep):
    if rep == 1:    
        new_item = animals.get(code)
        cart.append(new_item)             

    elif rep == 2:   
        new_item = pet_food.get(code)
        cart.append(new_item)          

def del_cart():
    cart.clear()

def confirme_cart():
    with open("cart.txt", 'w', encoding= "utf8") as f:        
            for j in cart:
                j = str(''.join([f"{j[0]}: description - {j[1]}, code - {j[2]}, price - {j[3]} byn"]))            
                j = j +"\n"              
                f.writelines(j)
            
    return             
        

    

