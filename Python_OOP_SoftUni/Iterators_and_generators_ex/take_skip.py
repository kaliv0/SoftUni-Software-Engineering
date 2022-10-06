class TakeSkip:
    def __init__(self, step: int, count: int):
        self._step = step
        self._count = count
        self._index = 0
        self._end = step * count

    def __iter__(self):
        return self

    def __next__(self):
        curr = self._index
        if curr >= self._end:
            raise StopIteration
        self._index += self._step
        return curr


if __name__ == "__main__":
    numbers = TakeSkip(2, 6)
    for number in numbers:
        print(number)
    numbers = TakeSkip(10, 5)
    for number in numbers:
        print(number)
