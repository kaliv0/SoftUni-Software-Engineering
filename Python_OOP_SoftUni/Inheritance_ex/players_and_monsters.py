class Hero:
    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level

    def __str__(self):
        return f"{self.username} of type {type(self).__name__} has level {self.level}"


class Elf(Hero):
    pass


class MuseElf(Elf):
    pass


class Wizard(Hero):
    pass


class DarkWizard(Wizard):
    pass


class SoulMaster(DarkWizard):
    pass


class Knight(Hero):
    pass


class DarkKnight(Knight):
    pass


class BladeKnight(DarkKnight):
    pass


if __name__ == "__main__":
    hero = Hero("H", 4)
    print(hero.username)
    print(hero.level)
    print(str(hero))
    elf = Elf("E", 4)
    print(str(elf))
    print(elf.__class__.__bases__[0].__name__)
    print(elf.username)
    print(elf.level)
