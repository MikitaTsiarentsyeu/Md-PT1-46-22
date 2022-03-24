class Vehicle:

    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    make = property(get_make, set_make)
    model = property(get_model, set_model)

    def get_info(self):
        print(f"{self.make} {self.model}")


class Car(Vehicle):

    def __init__(self, make, model, power) -> None:
        super().__init__(make, model)
        self.power = power

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    power = property(get_power, set_power)

    def get_info(self):
        super().get_info()
        print(f"power is {self.power}")

    def vroom(self):
        print("vrooom...")

class SuperCar(Car):

    # def vroom(self):
    #     super().vroom()
    #     super().vroom()
    #     super().vroom()

    def vroom(self):
        print("VROOOOOOOOOOOOOOM!!!!!!!!!!!!!!!")

# c = Car("Ford", "Focus", 144)
# c.get_info()
# c.vroom()

# s = SuperCar("Ferrari", "la Ferrari", 34566)
# s.get_info()
# s.vroom()



class Food:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return self.name

class Animal:

    def eat(self, something):
        print(f"eating {something}")

    def phe(self):
        print("phe...")

class Carnivore(Animal):

    def eat(self, something):
        if something.type == "meat":
            # Animal.eat(self, something)
            super().eat(something)
        else:
            # Animal.phe(self)
            super().phe()

class Herbivore(Animal):

    def eat(self, something):
        if something.type == "herbal":
            # Animal.eat(self, something)
            super().eat(something)
        else:
            # Animal.phe(self)
            super().phe()

class Omnivore(Carnivore, Herbivore):

    def eat(self, something):
        if something.type == "meat":
            Carnivore.eat(self, something)
        elif something.type == "herbal":
            Herbivore.eat(self, something)
        else:
            Animal.phe(self)

chicken = Food("chicken", "meat")
grass = Food("grass", "herbal")

c = Carnivore()
h = Herbivore()
o = Omnivore()

# o.eat(chicken)
# o.eat(grass)

# print(Omnivore.mro())


class X: pass

    # name = "X"

class Y:

    name = "Y"

class Z:

    name = "Z"

class A(X, Y, Z):  pass

    # name = "A"

class B(Y, Z):

    name = "B"

class M(B, A, Z, object): pass

    # name = "M"

print(M.mro())

m = M()
print(m.name)