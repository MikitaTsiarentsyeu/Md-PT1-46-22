
def validate_number(control_value):

    while True:
        x = input(f"Enter your value higher then {control_value}\n")
        
        try:
            x = int(x)

            if x <= control_value:
                raise(RuntimeError("The value is too low"))
        except ValueError:
            print("It was not a number")
            continue
        except RuntimeError as er:
            print(er)
            continue
        else:
            break
        
    return x


# while True:
#     x = validate_number(35)
#     if x:
#         break

# print(x)
