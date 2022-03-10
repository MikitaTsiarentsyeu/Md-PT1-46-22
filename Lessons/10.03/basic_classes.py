
class Simpleton: pass

s = Simpleton()
print(s, type(s))
print(Simpleton, type(Simpleton))

s.test = 4
print(s.test)

Simpleton.test = 77
print(Simpleton.test, s.test)

s2 = Simpleton()
print(s2.test)

s2.test = 88
print(Simpleton.test, s.test, s2.test)


class Student:

    # name = ""
    # year = 0
    # speciality = ""

    def init(self, name, year, speciality):
        self.__name = name
        self.year = year
        self.speciality = speciality

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.year

    def set_year(self, year):
        if 0 < year < 6:
            self.year = year
        # else:
        #     raise AttributeError("incorrect year value")

    def provide_info(self):
        print(f"I'm {self.__name}, {self.speciality} student of {self.year} year")

    def lear(self):
        print("I'm learning!")

    
s1 = Student()
s1.init("Mikita", 1, "engenering")
# s1.name = "Mikita"
# s1.year = 1
# s1.speciality = "engenering"

s2 = Student()
s2.init("Sasha", 3, "economist")
# s2.name = "Sasha"
# s2.year = 3
# s2.speciality = "economist"

s1.provide_info()
s2.provide_info()

# s1.year = 0
# s2.year = 100

# print(s1.year, s2.year)

s1.set_year(0)
s2.set_year(100)

print(s1.get_year(), s2.get_year())

s1.set_name("Ivan")
print(s1.get_name())

print(s1._Student__name)