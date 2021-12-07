class Animal:
    def __init__(self, nick_name, price, power, type):
        self.nick_name = nick_name
        if (not isinstance(price, int) and not isinstance(price, float)):
            raise ValueError("Price should be more than 0")
        if price < 0:
            raise ValueError("Price should be more than 0")
        else:
            self.price = float(price)

        if (not isinstance(power, int) and not isinstance(power, float)):
            raise ValueError("Power should be more than 0 and lower or equal to 100")
        if power > 0 and power <= 100 :
            self.__power = float(power)
        else:
            raise ValueError("Power should be more than 0 and lower or equal to 100")
        self.type = type

    def __repr__(self):
        return "Name: " + self.nick_name + ", Price: " + str(self.price) + " NIS, Power: " + str(self.__power)

    def _get__power(self):
        return self.__power

    def _set__power(self, new_power):
        if (not isinstance(new_power, int) and not isinstance(new_power, float)):
            return
        if new_power > 0 and new_power <= 100:
            self.__power = float(new_power)

    def win(self):
        return str(self.nick_name + " winner")

    def loss(self):
        return str(self.nick_name + " loser")

    def __ge__(self, other):
        if not isinstance(other, Animal):
            raise ValueError("You cannot compare between animal and somthing else")
        if self.__power >= other.__power:
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        return self.nick_name == other.nick_name

    def get_type(self):
        return str(self.type)