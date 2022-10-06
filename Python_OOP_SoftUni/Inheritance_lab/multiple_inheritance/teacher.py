from person import Person
from employee import Employee


class Teacher(Employee, Person):
    def __init__(self, name):
        super().__init__(name)

    def teaching(self):
        return f"{self.name} is teaching"


if __name__ == "__main__":
    professor = Teacher("Doncho")
    print(professor.name)
    print(professor.sleep())
    print(professor.teaching())
    print(professor.get_fired())
