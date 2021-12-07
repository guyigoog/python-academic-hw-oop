import unittest

from hw5.AnimalFactory import AnimalFactory
from hw5.Shop import Shop


class Test(unittest.TestCase):

    def test_1(self):
        """
        Check init method of shop
        """
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.get_name(), "My shop",
                         msg="The name is not the same")
        self.assertEqual(shop.balance, 10000,
                         msg="The balance is not the same")
        self.assertEqual(shop.get__animals(), {},
                         msg="The dict is not the same")

    def test_2(self):
        """
        Check if one animal add to shop
        """
        dog_1 = AnimalFactory.create("Dog", "dog_1", 10, 60)
        shop = Shop("My shop", 10000)
        shop.__add__(dog_1)
        dict_compare = {dog_1.nick_name: dog_1}
        self.assertEqual([i for i in dict_compare if i not in shop.get__animals()], [],
                         msg="The animal was not added to the shop")

    def test_3(self):
        """
        Check if list animals add to shop
        """
        cat_1 = AnimalFactory.create("Cat", "cat_1", 10, 10)
        cat_2 = AnimalFactory.create("Cat", "cat_2", 5, 20)
        cat_3 = AnimalFactory.create("Cat", "cat_3", 15, 30)
        shop = Shop("My shop", 10000)
        list_animals = [cat_1, cat_2, cat_3]
        shop.__add__(list_animals)
        dict_compare = {x.nick_name: x for x in list_animals}
        self.assertEqual([i for i in dict_compare if i not in shop.get__animals()], [],
                         msg="The animals was not added to the shop")

    def test_4(self):
        """
        Check the count of animal in shop
        """
        shop = Shop("My shop", 100)
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)
        shop.__add__(parrot_1)
        self.assertEqual(shop.num_of_animals(), 1)

        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 10)
        snake_1 = AnimalFactory.create("Snake", "snake_1", 10, 10)
        list_add = [snake_1, parrot_2]
        shop.__add__(list_add)
        self.assertEqual(shop.num_of_animals(), 3)

    def test_5(self):
        """
        Check remove animal from shop
        """
        shop = Shop("My shop", 100)
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)
        shop.__add__(parrot_1)
        self.assertEqual(shop.sell("parrot_1"), parrot_1)

    def test_6(self):
        """
        Check play method
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 9)
        snake_1 = AnimalFactory.create("Snake", "snake_1", 20, 25)
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        shop.__add__(list_add)
        print(shop.play("parrot_1", "snake_1"))
        self.assertEqual(shop.play("parrot_1", "snake_1"), "snake_1 winner\nparrot_1 loser")


    def test_7(self):
        """
        Too bad there's no documentation in the code.
        Now you're going to have to read it to understand what the test does.
        """
        cat_1 = AnimalFactory.create("Cat", "cat_1", 8, 9)
        self.assertEqual(cat_1.speak(), "cat_1 says meow")

    def test_8(self):
        """
        Too bad there's no documentation in the code.
        Now you're going to have to read it to understand what the test does.
        """
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 9)
        dog_1 = AnimalFactory.create("Dog", "dog_1", 20, 25)
        list_add = [parrot_1, dog_1]
        shop = Shop("My shop", 10000)
        shop.__add__(list_add)
        print(shop.play("parrot_1", "dog_1"))


    def test_9(self):
        """
        Too bad there's no documentation in the code.
        Now you're going to have to read it to understand what the test does.
        """
        cat_1 = AnimalFactory.create("Cat", "cat_1", 8, 9)
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 9)
        dog_1 = AnimalFactory.create("Dog", "dog_1", 20, 25)
        list_add = [parrot_1, dog_1, cat_1]
        shop = Shop("My shop", 10000)
        shop.__add__(list_add)
        print()
        print(shop.get__animals())
        self.assertEqual(cat_1.win(), "cat_1 winner")

    def test_12(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 10)  # power = 10
        list_add = [parrot_1, parrot_2]
        shop = Shop("My test 2", 20)
        self.assertEqual(shop.__add__(list_add), 2)
        self.assertEqual(shop.play("parrot_1", "parrot_2"), "parrot_1 winner\nparrot_2 loser")
        parrot_3 = AnimalFactory.create("Parrot", "parrot_3", 10, 10)  # power = 10
        parrot_3.fly = False
        new_animal = [parrot_3]
        shop.balance += 10
        self.assertEqual(shop.__add__(new_animal), 1)
        print(parrot_3.fly)
        self.assertEqual(shop.play("parrot_1", "parrot_3"), "parrot_1 winner\nparrot_3 loser")
        self.assertEqual(shop.play("parrot_3", "parrot_1"), "parrot_1 winner\nparrot_3 loser")


    def test_13(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 8, 9)  # power = 10
        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 10)  # power = 10
        list_add = [parrot_1, parrot_2]
        shop = Shop("My test 2", 20)
        self.assertEqual(shop.__add__(list_add), 2)
        self.assertEqual(parrot_1 == parrot_2, False)
        print(parrot_1)
        self.assertEqual(parrot_1.__repr__(), "Name: parrot_1, Price: 8.0 NIS, Power: 9.0")
        self.assertEqual(shop.__add__("stom"), 0)
        self.assertEqual(shop.num_of_animals(), 2)
        parrot_1.fly = False
        parrot_2.fly = False
        self.assertEqual(shop.play("parrot_2", "parrot_1"), "parrot_2 winner\nparrot_1 loser")

    def test_14(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 8, 9)  # power = 10
        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 10)  # power = 10
        dog_1 = AnimalFactory.create("Dog", "dog_1", 10, 10)  # power = 10
        turtle_1 = AnimalFactory.create("Turtle", "turtle_1", 10, 10)  # power = 10
        list_add = [parrot_1, parrot_2]
        shop = Shop("My test 2", 20)
        self.assertEqual(shop.__add__(list_add), 2)
        parrot_1._set__power(5)
        self.assertEqual(parrot_1._get__power(),5)
        parrot_1._set__power("5.15")
        self.assertEqual(parrot_1._get__power(),5)
        parrot_1._set__power(-1)
        self.assertEqual(parrot_1._get__power(),5)
        parrot_1._set__power(250)
        self.assertEqual(parrot_1._get__power(),5)
        parrot_1._set__power(100.0)
        self.assertEqual(parrot_1._get__power(),100.0)
        parrot_1._set__power(0)
        self.assertEqual(parrot_1._get__power(),100.0)
        self.assertEqual(parrot_1.win(), "parrot_1 winner")
        self.assertEqual(parrot_1.loss(), "parrot_1 loser")
        self.assertEqual(turtle_1.loss(), "turtle_1 loser I always lose")
        self.assertEqual(dog_1.win(), "dog_1 says woof woof dog_1 winner")
if __name__ == "__main__":
    unittest.main()
