print("before")

x = 10

if x == 0:
    print("it's zero")
elif x == 1:
    print("it's one")
elif x == 2:
    print("it's two")
elif x > 0:
    print("it's positive")
else:
    print("it's negative")


if x >= 0:
    if x == 0:
        print("it's zero")
    else:
        print("it's positive")
else:
    print("it's negative")

print("after")

print("it's true") if x>0 else print("it's not")

y = "it's true" if x>0 else "it's not"
print(y)

print("it's positive") if x > 0 else print("zero") if x == 0 else print("negative")