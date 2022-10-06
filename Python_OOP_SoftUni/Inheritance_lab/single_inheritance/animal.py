class Animal:

    def __init__(self, name: str):
        self.name = name

    def eat(self):
        return f"The {self.name} is eating..."
