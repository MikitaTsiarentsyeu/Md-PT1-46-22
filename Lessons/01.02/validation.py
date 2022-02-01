while True:
    user_input = input("Input your value in format hh:mm\n")

    if len(user_input) != 5:
        print("incorrect input, the string is too short")
        continue

    if user_input[2] != ':':
        print("incorrect input, the string lacks ':' sign")
        continue

    values = user_input.split(':')
    hours, minutes = values[0], values[1]

    if not (hours.isdigit() and minutes.isdigit()):
        print("incorrect input, the hours and minutes values should be digits")
        continue

    hours, minutes = int(hours), int(minutes)

    if hours > 24 or minutes > 60:
        print("incorrect input, the hours and minutes values are wrong")
        continue
    
    break

print("main logic")