from hw5.Animal import Animal
from hw5.AnimalFactory import AnimalFactory

class Shop:

    def __init__(self, name, balance):
        """
        :param name: shop name
        :param balance: shop balance
        """
        self.name = str(name)
        self.balance = float(balance)
        self.__animal_list = {}

    def get_name(self):
        return self.name

    def __add__(self, other):
        """
        Function to add animals to shop
        :param other: animal or list of animals
        :return: how many animals added
        """
        counter = 0
        if other == None:
            return 0
        if isinstance(other, Animal):
            if self.balance - other.price >= 0:
                self.__animal_list[other.nick_name] = other
                self.balance -= other.price
                counter += 1
        if isinstance(other, list):
            sorted_list = sorted(other, key=lambda other: other.price)
            for i in range(len(sorted_list)):
                if self.balance - sorted_list[i].price >= 0:
                    self.__animal_list[sorted_list[i].nick_name] = sorted_list[i]
                    self.balance -= sorted_list[i].price
                    counter += 1
        return counter

    def get__animals(self):
        """
        :return: return the animals in the shop
        """
        __new_dic = {}
        for i in self.__animal_list.keys():
            anim = AnimalFactory.create(self.__animal_list[i].get_type(), self.__animal_list[i].nick_name, self.__animal_list[i].price, self.__animal_list[i]._get__power())
            __new_dic[i] = anim
        return __new_dic

    def sell(self, nick_name):
        """
        :param nick_name: nick name of animal
        :return: the animal sold
        """
        if isinstance(nick_name, str):
            if nick_name in self.__animal_list:
                self.balance += self.__animal_list[nick_name].price
                temp = self.__animal_list.pop(nick_name)
                return temp
            else:
                return None
        return None

    def num_of_animals(self):
        """
        :return: how many animals in shop
        """
        count = 0
        for i in self.__animal_list:
            count += 1
        return count

    def play(self, animal_1, animal_2):
        """
        Function to compare animals power
        :param animal_1: animal 1
        :param animal_2: animal 2
        :return: return winning animal and losing animal
        """
        if animal_1 in self.__animal_list and animal_2 in self.__animal_list:
            animal1 = self.__animal_list[animal_1]
            animal2 = self.__animal_list[animal_2]
            test = animal1.__ge__(animal2)
            if test == True:
                st = str(animal1.win()) + "\n" + str(animal2.loss())
            else:
                st = str(animal2.win()) + "\n" + str(animal1.loss())
            return st
        return False
