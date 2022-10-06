class Vowels:
    VOWEL_LIST = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]

    def __init__(self, word: str):
        self.data = word
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        curr_char = self.data[self.index]
        self.index += 1
        if curr_char in Vowels.VOWEL_LIST:
            return curr_char
        return self.__next__()


if __name__ == "__main__":
    my_string = Vowels('Abcedifuty0o')
    for char in my_string:
        print(char)
