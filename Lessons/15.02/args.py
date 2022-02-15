x, y = 2, 3

def func(x, y):
    x[0] += 2
    print(x, y)

l = [2]
func(l, 5)
print(l)

def evaluate(value1, value2, value3):
    return value1+value2*value3

print(evaluate(value3=2,value1=3,value2=4))

# print(1,2,3,4,5,6,sep=',',end='.')

def choose_pet_name(name_one, name_two="Kisa"):
    print(f"Do you want to name your pet {name_one} or {name_two}?")

choose_pet_name("Totoshka", name_two="Tigger")

def sum(*args):
    res = 0
    for i in args:
        res += i
    return res

l = [1,2,3,4,5]
print(sum(*l))
print(sum(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

def sum(**kwargs):
    res = 0
    for k, v in kwargs.items():
        res += v
    return res

d = {"one": 1, "two": 2}
print(sum(**d))

def calling_pets(**kwargs):
    for k, v in kwargs.items():
        print(f"{v} the {k}!")

calling_pets(cat="Kitty", dog="Barker")

def my_print(x, y, z="test", *args, **kwargs):
    print(x, y, z)
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,3,4,5,6,7,8,9, sep=',', end='.')