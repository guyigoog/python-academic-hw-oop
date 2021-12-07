from hw5.Cat import Cat
from hw5.Snake import Snake
from hw5.Dog import Dog
from hw5.Turtle import Turtle
from hw5.Parrot import Parrot

class AnimalFactory(object):

    @staticmethod
    def create(type_animal, nick_name, price, power):
        """
        Function to create animals
        :param type_animal: type of animal
        :param nick_name: nick name
        :param price: price
        :param power: power
        :return: string if animal created
        """
        if type_animal == "Dog":
            d = Dog(nick_name, price, power)
            print("Dog created")
            return d
        if type_animal == "Cat":
            c = Cat(nick_name, price, power)
            print("Cat created")
            return c
        if type_animal == "Parrot":
            p = Parrot(nick_name, price, power)
            print("Parrot created")
            return p
        if type_animal == "Turtle":
            t = Turtle(nick_name, price, power)
            print("Turtle created")
            return t
        if type_animal == "Snake":
            s = Snake(nick_name, price, power)
            print("Snake created")
            return s
        return None