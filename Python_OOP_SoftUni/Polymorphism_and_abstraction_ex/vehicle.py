from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self._fuel_quantity = fuel_quantity
        self._fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def refuel(self, fuel: float):
        ...

    @property
    def fuel_quantity(self):
        return self._fuel_quantity

    @property
    def fuel_consumption(self):
        return self._fuel_consumption


class Car(Vehicle):
    EXTRA_COST = 0.9

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: float):
        curr_consumption = distance * (self._fuel_consumption + self.EXTRA_COST)
        if self._fuel_quantity >= curr_consumption:
            self._fuel_quantity -= curr_consumption

    def refuel(self, fuel: float):
        self._fuel_quantity += fuel


class Truck(Vehicle):
    EXTRA_COST = 1.6
    LEAKAGE = 0.95

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: float):
        curr_consumption = distance * (self._fuel_consumption + self.EXTRA_COST)
        if self._fuel_quantity >= curr_consumption:
            self._fuel_quantity -= curr_consumption

    def refuel(self, fuel: float):
        self._fuel_quantity += (fuel * self.LEAKAGE)


if __name__ == "__main__":
    car = Car(20, 5)
    car.drive(3)
    print(f"{car.fuel_quantity:.2f}")
    car.refuel(10)
    print(f"{car.fuel_quantity:.2f}")

    truck = Truck(100, 15)
    truck.drive(5)
    print(truck.fuel_quantity)
    truck.refuel(50)
    print(truck.fuel_quantity)
