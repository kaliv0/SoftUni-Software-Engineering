def solution():
    def integers():
        n = 1
        while True:
            yield n
            n += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        res = []
        for el in seq:
            if len(res) == n:
                return res
            res.append(el)

    return take, halves, integers


if __name__ == "__main__":
    take_ = solution()[0]
    halves_ = solution()[1]
    print(take_(5, halves_()))
