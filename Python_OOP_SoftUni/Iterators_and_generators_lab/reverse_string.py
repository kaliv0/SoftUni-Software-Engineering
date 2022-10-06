def reverse_text(text: str):
    # for i in range((len(text) - 1), -1, -1):
    #     yield text[i]

    for c in text[::-1]:
        yield c


if __name__ == "__main__":
    for char in reverse_text("step"):
        print(char, end='')
