class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type_: str, sound: str):
        self._name = name
        self._type = type_
        self._sound = sound

    def make_sound(self):
        return f"{self._name} makes {self._sound}"

    @staticmethod
    def get_kingdom():
        return Mammal.__kingdom

    def info(self):
        return f"{self._name} is of type {self._type}"


if __name__ == "__main__":
    mammal = Mammal("Dog", "Domestic", "Bark")
    print(mammal.make_sound())
    print(mammal.get_kingdom())
    print(mammal.info())
