import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def calculate_area(self):
        return math.pi * (self._radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self._radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


if __name__ == "__main__":
    circle = Circle(5)
    print(circle.calculate_area())
    print(circle.calculate_perimeter())

    rectangle = Rectangle(10, 20)
    print(rectangle.calculate_area())
    print(rectangle.calculate_perimeter())
