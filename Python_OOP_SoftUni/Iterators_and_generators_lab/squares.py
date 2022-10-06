def squares(end: int):
    num = 1
    while num <= end:
        yield num ** 2
        num += 1


if __name__ == "__main__":
    print(list(squares(5)))
