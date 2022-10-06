from typing import List


class ReverseIter:
    def __init__(self, nums: List[int]):
        self.data = nums
        self.index = len(self.data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        curr_index = self.index
        self.index -= 1
        return self.data[curr_index]


if __name__ == "__main__":
    reversed_list = ReverseIter([1, 2, 3, 4])
    for item in reversed_list:
        print(item)
