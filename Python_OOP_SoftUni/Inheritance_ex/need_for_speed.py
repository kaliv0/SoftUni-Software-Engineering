class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= kilometers * self.fuel_consumption


class Motorcycle(Vehicle):
    pass


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = RaceMotorcycle.DEFAULT_FUEL_CONSUMPTION


class CrossMotorcycle(Motorcycle):
    pass


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION


class FamilyCar(Car):
    pass


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION


if __name__ == "__main__":
    vehicle = Vehicle(50, 150)
    print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
    print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
    print(vehicle.fuel)
    print(vehicle.horse_power)
    print(vehicle.fuel_consumption)
    vehicle.drive(100)
    print(vehicle.fuel)
    family_car = FamilyCar(150, 150)
    family_car.drive(50)
    print(family_car.fuel)
    family_car.drive(50)
    print(family_car.fuel)
    print(family_car.__class__.__bases__[0].__name__)
