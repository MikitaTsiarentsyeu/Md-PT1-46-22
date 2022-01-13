import random

my_number = random.randint(0, 10)

your_number = int(input("Guess my number:"))

if your_number == my_number:
    print("correct!")
else:
    print("looser!")