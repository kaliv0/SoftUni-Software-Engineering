from itertools import permutations


def possible_permutations(collection):
    for perm in permutations(collection):
        # yield list(perm)
        yield [*perm]


if __name__ == "__main__":
    [print(n) for n in possible_permutations([1, 2, 3])]
