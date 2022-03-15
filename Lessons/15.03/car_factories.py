class Engine():

    def __init__(self, power, volume) -> None:
        self.power = power
        self.volume = volume

    def get_power(self):
        return self.__power

    def get_volume(self):
        return self.__volume

    def set_power(self, power):
        self.__power = power

    def set_volume(self, volume):
        self.__volume = volume

    power = property(get_power, set_power)
    volume = property(get_volume, set_volume)



class SerialCar:

    def __init__(self, make, model, engine) -> None:
        self.make = make
        self.model = model
        self.engine = engine

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine

    model = property(get_model)
    make = property(get_make)
    engine = property(get_engine, set_engine)

v4 = Engine(100, 4)

camry = SerialCar("Toyota", "Camry", v4)

v8 = Engine(250, 8)

camry.engine = v8




class SuperCar:

    def __init__(self, make, model, power, volume) -> None:
        self.make = make
        self.model = model
        self.engine = Engine(power, volume)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_engine(self):
        return self.__engine

    model = property(get_model)
    make = property(get_make)
    engine = property(get_engine)


s = SuperCar("Ferrari", "la Ferrari", 300, 12)