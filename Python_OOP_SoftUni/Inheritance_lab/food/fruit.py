from food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super().__init__(expiration_date)
        self.name = name


if __name__ == "__main__":
    food = Food("Tomorrow")
    apple = Fruit("Apple", "Next week")

    print(food.expiration_date)
    print(apple.name)
    print(apple.expiration_date)
