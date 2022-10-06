def fibonacci():
    previous, curr = 0, 1
    while True:
        yield previous
        previous, curr = curr, previous + curr


if __name__ == "__main__":
    generator = fibonacci()
    for i in range(5):
        print(next(generator))
