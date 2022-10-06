from typing import List

from more_itertools import first_true

from animals import *

from workers import *


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity > len(self.animals):
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = first_true(self.workers, None, lambda w: w.name == worker_name)
        # worker = [w for w in self.workers if w.name == worker_name]
        if worker:
            # self.workers.remove(worker[0])
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum([w.salary for w in self.workers])
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_cost = sum([a.money_for_care for a in self.animals])
        if self.__budget >= total_cost:
            self.__budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions_list = [a.__repr__() for a in self.animals if isinstance(a, Lion)]
        tigers_list = [a.__repr__() for a in self.animals if isinstance(a, Tiger)]
        cheetahs_list = [a.__repr__() for a in self.animals if isinstance(a, Cheetah)]
        delimiter = '\n'

        return f'''You have {len(self.animals)} animals
----- {len(lions_list)} Lions:
{delimiter.join(lions_list)}
----- {len(tigers_list)} Tigers:
{delimiter.join(tigers_list)}
----- {len(cheetahs_list)} Cheetahs:
{delimiter.join(cheetahs_list)}'''

    def workers_status(self):
        keepers_list = [w.__repr__() for w in self.workers if isinstance(w, Keeper)]
        caretakers_list = [w.__repr__() for w in self.workers if isinstance(w, Caretaker)]
        vets_list = [w.__repr__() for w in self.workers if isinstance(w, Vet)]
        delimiter = '\n'

        return f'''You have {len(self.workers)} Workers
----- {len(keepers_list)} Keepers:
{delimiter.join(keepers_list)}
----- {len(caretakers_list)} Caretakers:
{delimiter.join(caretakers_list)}
----- {len(vets_list)} Vets:
{delimiter.join(vets_list)}'''
