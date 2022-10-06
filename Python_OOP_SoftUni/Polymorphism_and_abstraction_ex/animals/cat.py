from animal import Animal


class Cat(Animal):
    def make_sound(self):
        return "Meow meow!"


class Kitten(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Female")

    def make_sound(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender="Male")

    def make_sound(self):
        return "Hiss"
