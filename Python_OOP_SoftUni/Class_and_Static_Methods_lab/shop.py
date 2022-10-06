from typing import Dict


class Shop:
    def __init__(self, name: str, type_: str, capacity: int):
        self.name = name
        self.type = type_
        self.capacity = capacity
        self.items: Dict[str:int] = {}

    @classmethod
    def small_shop(cls, name: str, type_: str):
        return cls(name, type_, capacity=10)

    def add_item(self, item_name: str):
        if self.capacity - 1 < 0:
            return "Not enough capacity in the shop"
        if item_name not in self.items.keys():
            self.items.update({item_name: 0})
        self.items[item_name] += 1
        self.capacity -= 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name not in self.items.keys():
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        self.capacity += amount
        if self.items[item_name] == 0:
            self.items.pop(item_name)
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


if __name__ == "__main__":
    fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
    small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
    print(fresh_shop)
    print(small_shop)

    print(fresh_shop.add_item("Bananas"))
    print(fresh_shop.remove_item("Tomatoes", 2))

    print(small_shop.add_item("Jeans"))
    print(small_shop.add_item("Jeans"))
    print(small_shop.remove_item("Jeans", 2))
    print(small_shop.items)
