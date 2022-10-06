from typing import List

from more_itertools import first_true


class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int):
        if quantity <= self.quantity:
            self.quantity -= quantity

    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self):
        return self.name


class Drink(Product):
    def __init__(self, name: str):
        super().__init__(name, quantity=10)


class Food(Product):
    def __init__(self, name: str):
        super().__init__(name, quantity=15)


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        return first_true(self.products, None, lambda p: p.name == product_name)

    def remove(self, product_name: str):
        self.products.remove(first_true(self.products, None, lambda p: p.name == product_name))

    def __repr__(self):
        return "\n".join([f"{product.name}: {product.quantity}" for product in self.products])


if __name__ == "__main__":
    food = Food("apple")
    drink = Drink("water")
    repo = ProductRepository()
    repo.add(food)
    repo.add(drink)
    print(repo.products)
    print(repo.find("water"))
    repo.find("apple").decrease(5)
    print(repo)
