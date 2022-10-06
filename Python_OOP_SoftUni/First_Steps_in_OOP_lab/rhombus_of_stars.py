# from timeit import timeit

class Rhombus:
    symbol = '* '

    def __init__(self, star_count: int):
        self._star_count = star_count

    def create_line(self, num: int):
        return (' ' * (self._star_count - num)) + (Rhombus.symbol * num)

    def draw(self):
        for _ in (self.create_line(i) for i in range(1, self._star_count)):
            print(_)

        for _ in (self.create_line(i) for i in range(self._star_count, 0, -1)):
            print(_)


if __name__ == "__main__":
    count = int(input())
    rhombus = Rhombus(count)
    rhombus.draw()
    # print("Single Execution time: ", timeit(stmt=rhombus.draw, number=1), "seconds")
