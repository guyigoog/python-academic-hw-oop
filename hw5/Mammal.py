from hw5.Animal import Animal

class Mammal(Animal):
    def __init__(self, nick_name, price, power, type):
        Animal.__init__(self,nick_name, price, power, type)

    def speak(self):
        return str(self.nick_name + " says")