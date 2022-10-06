class CountdownIterator:
    def __init__(self, start):
        self._index = start
        self._stop = 0

    def __iter__(self):
        return self

    def __next__(self):
        num = self._index
        if num < self._stop:
            raise StopIteration
        self._index -= 1
        return num


if __name__ == "__main__":
    iterator = CountdownIterator(10)
    for item in iterator:
        print(item, end=" ")
