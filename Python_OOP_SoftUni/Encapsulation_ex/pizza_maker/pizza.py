from dough import Dough
from topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.__name = None
        self.__dough = None
        self.__toppings_capacity = None
        self.__toppings = {}

        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value: Dough):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value: int):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if len(self.__toppings) == self.__toppings_capacity:
            raise ValueError("Not enough space for another topping")
        if topping not in self.__toppings.keys():
            self.__toppings.update({topping.topping_type: 0})
        self.__toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        return sum(v for v in self.__toppings.values()) + self.__dough.weight
