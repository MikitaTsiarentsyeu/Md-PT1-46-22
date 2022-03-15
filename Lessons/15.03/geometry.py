# from basic_classes import Student

# s = Student("Mikita", 1, "engenering")
# print(s.year)

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    x = property(get_x, set_x)
    y = property(get_y, set_y)

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

p1 = Point(2, 3)
print(p1)

p2 = Point(5, -9)
print(p2)

class SegmentV1:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    a = property(get_a, set_b)
    b = property(get_a, set_b)

    def __str__(self) -> str:
        return f"A - {self.a}; B - {self.b};"

class SegmentV2:

    def __init__(self, x1, y1, x2, y2) -> None:
        self.a = Point(x1, y1)
        self.b = Point(x2, y2)

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b

    a = property(get_a, set_b)
    b = property(get_a, set_b)

    def __str__(self) -> str:
        return f"A - {self.a}; B - {self.b};"

s1 = SegmentV1(p1, p2)
print(s1)
    

s2 = SegmentV2(2, 4, 6, 9)
print(s2)