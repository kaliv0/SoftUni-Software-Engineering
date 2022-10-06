from Polymorphism_and_abstraction_ex.wild_farm.project.animals.animal import Mammal
from Polymorphism_and_abstraction_ex.wild_farm.project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE_RATE = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_INCREASE_RATE * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_INCREASE_RATE = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Meat):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_INCREASE_RATE * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE_RATE = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food: (Vegetable, Meat)):
        if not isinstance(food, (Vegetable, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_INCREASE_RATE * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASE_RATE = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Meat):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_INCREASE_RATE * food.quantity
        self.food_eaten += food.quantity
