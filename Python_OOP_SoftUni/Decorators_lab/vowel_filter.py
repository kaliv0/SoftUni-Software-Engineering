from functools import wraps


def vowel_filter(func):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]

    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        return [char for char in result if char in vowels]

    return wrapper


if __name__ == "__main__":
    @vowel_filter
    def get_letters(text):
        return text


    print(get_letters(["a", "b", "c", "d", "e"]))
    print(get_letters("GoGo"))
