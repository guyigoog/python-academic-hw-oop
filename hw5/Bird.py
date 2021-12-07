from hw5.Animal import Animal
class Bird(Animal):
    def __init__(self, nick_name, price, power, type):
        Animal.__init__(self, nick_name, price, power, type)
        self.fly = False

    def __ge__(self, other):
        if isinstance(other, Bird):
            if not other.fly and self.fly:
                return True
            if other.fly and not self.fly:
                return False
            else:
                return Animal.__ge__(self, other)
        return Animal.__ge__(self, other)