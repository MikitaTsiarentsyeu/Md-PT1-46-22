class Animal: 

    def SaySomething(self):
        print("Hello, I'm an animal")

class Dog(Animal):

    def SaySomething(self):
        print("Woof!")

class Cat(Animal):

    def SaySomething(self):
        print("Nyaaa!")

class Human:

    def SaySomething(self, name):
        print(f"Hello, I'm {name}")


a = Animal()
d = Dog()
c = Cat()
h = Human()

for elem in [a, d, c, h]:
    elem.SaySomething()