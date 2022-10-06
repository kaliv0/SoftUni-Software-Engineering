class Worker:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Keeper(Worker):
    pass


class Caretaker(Worker):
    pass


class Vet(Worker):
    pass
