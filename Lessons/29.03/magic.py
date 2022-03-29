from argparse import ArgumentError

class FreightTrain:

    cart_len = 10

    def __init__(self, cart_count) -> None:
        self.cart_count = cart_count

    def __str__(self) -> str:
        return f"I'm a train of {self.cart_count} carts, choo-choo!"

    def __int__(self):
        return self.cart_count

    def __add__(self, other):
        try:
            return FreightTrain(self.cart_count + other.cart_count)
        except:
            raise ArgumentError("cannot add non-FreightTrain object")

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, FreightTrain):
            return False

        return self.cart_count == __o.cart_count
    
    def __len__(self):
        return self.cart_count * self.cart_len


shorty = FreightTrain(3)
loooong = FreightTrain(10)

print(shorty)
print(loooong)

print(int(shorty))

print(shorty + loooong)
print(shorty == loooong)
print(shorty + loooong == FreightTrain(13))

print(len(loooong))