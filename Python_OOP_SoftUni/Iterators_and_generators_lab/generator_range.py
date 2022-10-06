def genrange(start, end):
    for n in range(start, end + 1):
        yield n


if __name__ == "__main__":
    print(list(genrange(1, 10)))
