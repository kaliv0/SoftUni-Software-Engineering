from car import Car


class SportsCar(Car):
    @staticmethod
    def race():
        return "racing..."


if __name__ == '__main__':
    ferrari = SportsCar()
    print(ferrari.move())
    print(ferrari.drive())
    print(ferrari.race())
