from hw5.Reptiles import Reptiles
class Snake(Reptiles):
    def __init__(self, nick_name, price, power, type="Snake"):
        Reptiles.__init__(self, nick_name, price, power, type)

    def move(self):
        """
        :return: new power
        """
        if self._get__power() * 2.5 <= 100:
            new = self._get__power() * 2.5
            self._set__power(new)
