from hw5.Mammal import Mammal
from hw5.Animal import Animal

class Dog(Mammal):
    def __init__(self, nick_name, price, power, type="Dog"):
        Mammal.__init__(self, nick_name, price, power, type)

    def speak(self):
        return str(Mammal.speak(self) + " woof woof")

    def win(self):
        return str(self.speak() + " " + Animal.win(self))
