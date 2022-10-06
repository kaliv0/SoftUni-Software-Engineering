from typing import List

from dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, id_: int):
        self.name = name
        self.age = age
        self.id_ = id_
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        dvds = ', '.join([dvd.name for dvd in self.rented_dvds])
        return f"{self.id_}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({dvds})"
