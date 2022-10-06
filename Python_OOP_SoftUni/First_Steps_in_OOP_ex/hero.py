class Hero:
    def __init__(self, name: str, health: int):
        self._name = name
        self._health = health

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    def defend(self, damage: int):
        self._health -= damage
        if self._health <= 0:
            self._health = 0
            return f"{self._name} was defeated"
        else:
            return None

    def heal(self, amount: int):
        self._health += amount


if __name__ == "__main__":
    hero = Hero("Peter", 100)
    print(hero.defend(50))
    hero.heal(50)
    print(hero.defend(99))
    print(hero.defend(1))
