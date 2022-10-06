class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Child(Person):
    pass


if __name__ == "__main__":
    person = Person("Peter", 25)
    child = Child("Peter Junior", 5)
    print(person.name)
    print(person.age)
    print(child.__class__.__bases__[0].__name__)
