class DictionaryIter:
    def __init__(self, dictionary):
        self.data = [*dictionary.items()]
        self.index = 0
        self.stop = len(dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        curr_index = self.index
        if curr_index >= len(self.data):
            raise StopIteration
        self.index += 1
        return self.data[curr_index]


if __name__ == "__main__":
    result = DictionaryIter({1: "1", 2: "2"})
    for x in result:
        print(x)
