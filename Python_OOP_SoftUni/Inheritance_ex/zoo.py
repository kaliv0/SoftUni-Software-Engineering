class Animal:
    def __init__(self, name: str):
        self.name = name


class Reptile(Animal):
    pass


class Lizard(Reptile):
    pass


class Snake(Reptile):
    pass


class Mammal(Animal):
    pass


class Gorilla(Mammal):
    pass


class Bear(Mammal):
    pass


if __name__ == "__main__":
    mammal = Mammal("Stella")
    print(mammal.__class__.__bases__[0].__name__)
    print(mammal.name)
    lizard = Lizard("John")
    print(lizard.__class__.__bases__[0].__name__)
    print(lizard.name)
