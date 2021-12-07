from hw5.Animal import Animal

class Reptiles(Animal):
    def __init__(self, nick_name, price, power, type):
        Animal.__init__(self,nick_name, price, power, type)

    def move(self):
        new = self._get__power() / 2
        self._set__power(new)

    def __ge__(self, other):
        if isinstance(other, Reptiles):
            self.move()
            other.move()
            return Animal.__ge__(self, other)
        return Animal.__ge__(self, other)