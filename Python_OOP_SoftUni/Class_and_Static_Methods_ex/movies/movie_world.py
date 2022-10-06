from typing import List
from more_itertools import first_true

from customer import Customer
from dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = first_true(self.customers, None, lambda c: c.id_ == customer_id)
        dvd = first_true(self.dvds, None, lambda d: d.id_ == dvd_id)
        if not customer or not dvd:
            raise ValueError("Invalid customer or DVD id!")

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = first_true(self.customers, None, lambda c: c.id_ == customer_id)
        if not customer:
            raise ValueError("Invalid customer id")

        dvd = first_true(customer.rented_dvds, None, lambda d: d.id_ == dvd_id)
        if not dvd:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        info = ''
        for customer in self.customers:
            info += f'{customer}\n'
        for dvd in self.dvds:
            info += f'{dvd}\n'
        return info
