from animal import Animal


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return f"The {self.name} is barking..."


if __name__ == "__main__":
    mammal = Animal("mammal")
    muttley = Dog("muttley")

    print(mammal.eat())
    print(muttley.bark())
    print(muttley.eat())
