from Polymorphism_and_abstraction_ex.wild_farm.project.animals.animal import Bird
from Polymorphism_and_abstraction_ex.wild_farm.project.food import Meat


class Owl(Bird):
    WEIGHT_INCREASE_RATE = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Meat):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += self.WEIGHT_INCREASE_RATE * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASE_RATE = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Meat):
        self.weight += self.WEIGHT_INCREASE_RATE * food.quantity
        self.food_eaten += food.quantity
