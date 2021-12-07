import unittest

from hw5.Shop import Shop
from hw5.AnimalFactory import AnimalFactory


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
        self.assertEqual(shop.play("parrot_1", "snake_1"), "snake_1 winner\nparrot_1 loser")

    def test_7(self):
        """
        Too bad there's no documentation in the code.
        Now you're going to have to read it to understand what the test does.
        """
        cat_1 = AnimalFactory.create("Cat", "cat_1", 8, 9)
        self.assertEqual(cat_1.speak(), "cat_1 says meow")

    def test_8(self):
        """"
            Check the equal method in Animal class:
            :return:
                bool (True/ False)
        """
        dog_1 = AnimalFactory.create("Dog", "dog_1", 8, 9)
        dog_2 = AnimalFactory.create("Dog", "dog_2", 8, 9)
        # if not equal - False
        self.assertNotEqual(dog_1, dog_2)
        # if equal - True
        self.assertEqual(dog_1, dog_1)
        # if Can't be estimated - False (without raise error)
        self.assertNotEqual(dog_1, 1)

    def test_9(self):
        """"
           Check the __add__ method get a list of animals in Shop class
           :return:
               int ( always return int)
       """
        # Adding all animals
        dog_1 = AnimalFactory.create("Dog", "dog_1", 10, 10)
        cat_1 = AnimalFactory.create("Cat", "cat_1", 5, 20)
        snake_1 = AnimalFactory.create("Snake", "snake_1", 5, 30)
        shop = Shop("My shop", 500)  # balance = 500
        list_animals = [dog_1, cat_1, snake_1]
        self.assertEqual(shop.__add__(list_animals), 3)

        # Adding some of the animals
        dog_1 = AnimalFactory.create("Dog", "dog_1", 10, 10)
        cat_1 = AnimalFactory.create("Cat", "cat_1", 5, 20)
        snake_1 = AnimalFactory.create("Snake", "snake_1", 5, 30)
        shop = Shop("My shop", 10)
        list_animals = [dog_1, cat_1, snake_1]
        self.assertEqual(shop.__add__(list_animals), 2)  # balance = 10

        # without add animal - price animal greater than  shop balance
        dog_1 = AnimalFactory.create("Dog", "dog_1", 10, 10)
        cat_1 = AnimalFactory.create("Cat", "cat_1", 5, 20)
        snake_1 = AnimalFactory.create("Snake", "snake_1", 5, 30)
        shop = Shop("My shop", 0)  # balance = 0
        list_animals = [dog_1, cat_1, snake_1]
        self.assertEqual(shop.__add__(list_animals), 0)

    def test_10(self):
        """
        Check play method
        """
        # The animal_1 win
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 50)  # power = 50
        snake_1 = AnimalFactory.create("Snake", "snake_1", 20, 25)  # power = 25
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        self.assertEqual(shop.play("parrot_1", "snake_1"), "parrot_1 winner\nsnake_1 loser")

        # The animal_2 win
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        snake_1 = AnimalFactory.create("Snake", "snake_1", 20, 25)  # power = 25
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        self.assertEqual(shop.play("parrot_1", "snake_1"), "snake_1 winner\nparrot_1 loser")

        # animal_1 OR animal_2 not in the shop
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        snake_1 = AnimalFactory.create("Snake", "snake_1", 20, 25)  # power = 25
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        self.assertEqual(shop.play("shir", "snake_1"), False)  # shir

    def test_11(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 50)  # power = 50
        snake_1 = AnimalFactory.create("Snake", "snake_1", 20, 25)  # power = 25
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        print(shop.play("parrot_1", "snake_1"))
        self.assertEqual(shop.play("parrot_1", "snake_1"), "parrot_1 winner\nsnake_1 loser")


    def test_12(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        snake_1 = AnimalFactory.create("Snake", "snake_1", 20, 25)  # power = 25
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        print(shop.play("parrot_1", "snake_1"))
        self.assertEqual(shop.play("parrot_1", "snake_1"), "snake_1 winner\nparrot_1 loser")

    def test_13(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        snake_1 = AnimalFactory.create("Snake", "snake_1", 20, 25)  # power = 25
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        self.assertEqual(shop.play("shir", "snake_1"), False)  # shir

    def test_14(self):
        dog_1 = AnimalFactory.create("Dog", "dog_1", 10, 10)  # power = 10
        cat_1 = AnimalFactory.create("Cat", "cat_1", 20, 10)  # power = 25
        list_add = [dog_1, cat_1]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        print(shop.play("cat_1", "dog_1"))
        self.assertEqual(shop.play("dog_1", "cat_1"), "dog_1 says woof woof dog_1 winner\ncat_1 loser")

    def test_15(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 10)  # power = 10
        list_add = [parrot_1, parrot_2]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        print(shop.play("parrot_1", "parrot_2"))
        self.assertEqual(shop.play("parrot_1", "parrot_2"), "parrot_1 winner\nparrot_2 loser")

    def test_16(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 11)  # power = 11
        list_add = [parrot_1, parrot_2]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        print(shop.play("parrot_1", "parrot_2"))
        self.assertEqual(shop.play("parrot_1", "parrot_2"), "parrot_2 winner\nparrot_1 loser")

    def test_17(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, 20)  # power = 11
        parrot_2.fly = False
        list_add = [parrot_1, parrot_2]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        print(shop.play("parrot_1", "parrot_2"))
        self.assertEqual(shop.play("parrot_1", "parrot_2"), "parrot_1 winner\nparrot_2 loser")

    def test_18(self):
        snake_1 = AnimalFactory.create("Snake", "snake_1", 10, 20)  # power = 10
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 11
        parrot_1.fly = False
        list_add = [parrot_1, snake_1]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        print(shop.play("parrot_1", "snake_1"))
        self.assertEqual(shop.play("parrot_1", "snake_1"), "snake_1 winner\nparrot_1 loser")

    def test_19(self):
        parrot_1 = AnimalFactory.create("Parrot", "parrot_1", 10, 10)  # power = 10
        parrot_2 = AnimalFactory.create("Parrot", "parrot_2", 10, '20.1')  # power = 11
        parrot_1.fly = False
        list_add = [parrot_1, parrot_2]
        shop = Shop("My shop", 10000)
        self.assertEqual(shop.__add__(list_add), 2)
        print(shop.play("parrot_1", "parrot_2"))
        print(parrot_1)
        self.assertEqual(shop.play("parrot_1", "parrot_2"), "parrot_2 winner\nparrot_1 loser")

if __name__ == "__main__":
    unittest.main()
