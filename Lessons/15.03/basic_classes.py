
class Student:

    # name = ""
    # year = 0
    # speciality = ""

    def __init__(self, name, year, speciality):
        self.set_name(name)
        self.year = year
        self.speciality = speciality

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if 0 < year < 6:
            self.__year = year
        # else:
        #     raise AttributeError("incorrect year value")

    year = property(get_year, set_year)

    def provide_info(self):
        print(f"I'm {self.__name}, {self.speciality} student of {self.year} year")

    def lear(self):
        print("I'm learning!")

    
s1 = Student("Mikita", 1, "engenering")
# s1.name = "Mikita"
# s1.year = 1
# s1.speciality = "engenering"

s2 = Student("Sasha", 3, "economist")
# s2.name = "Sasha"
# s2.year = 3
# s2.speciality = "economist"

s1.provide_info()
s2.provide_info()

# s1.year = 0
# s2.year = 100

# print(s1.year, s2.year)

s1.year = 0
s1.year = 3
s2.year = 100

print(s1.year, s2.year)

s1.set_name("Ivan")
print(s1.get_name())

# print(s1._Student__name)