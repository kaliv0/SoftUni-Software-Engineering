class Shop:
    def __init__(self, name: str, items: list):
        self._name = name
        self._items = items

    @property
    def name(self):
        return self._name

    @property
    def items(self):
        return self._items

    def get_items_count(self):
        return len(self._items)


if __name__ == "__main__":
    shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
    print(shop.get_items_count())
