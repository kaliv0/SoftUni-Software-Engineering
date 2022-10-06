class Employee:
    def __init__(self, id_: int, first_name: str, last_name: str, salary: int):
        self._id = id_
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary

    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def salary(self):
        return self._salary

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount: int):
        self._salary += amount
        return self._salary


if __name__ == "__main__":
    employee = Employee(744423129, "John", "Smith", 1000)
    print(employee.get_full_name())
    print(employee.raise_salary(500))
    print(employee.get_annual_salary())
