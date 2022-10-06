class SequenceRepeat:
    def __init__(self, sequence: str, stop: int):
        self._data = sequence
        self._index = 0
        self._counter = 0
        self._stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter == self._stop:
            raise StopIteration
        curr_item = self._data[self._index]
        self._index += 1
        if self._index == len(self._data):
            self._index = 0
        self._counter += 1
        return curr_item


if __name__ == "__main__":
    result = SequenceRepeat('abc', 5)
    for item in result:
        print(item, end='')
