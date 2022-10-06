class CustomRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        index = self.start
        if index > self.end:
            raise StopIteration
        self.start += 1
        return index


if __name__ == "__main__":
    one_to_ten = CustomRange(1, 10)
    for num in one_to_ten:
        print(num)
