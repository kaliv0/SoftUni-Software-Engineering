from typing import Protocol


class Player(Protocol):
    def play(self) -> str:
        pass


def start_playing(obj: Player) -> str:
    return obj.play()


if __name__ == "__main__":
    class Guitar:
        def play(self):
            return f"Playing the {self.__class__.__name__}"


    guitar = Guitar()
    print(start_playing(guitar))


    class Children:
        def play(self):
            return f"{self.__class__.__name__} are playing!"


    children = Children()
    print(start_playing(children))
