from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str) -> None:
        if type(element) != str:
            raise TypeError("Invalid element type")
        else:
            self.data.append(element)

    def pop(self) -> str:
        if self.is_empty() is False:
            return self.data.pop()

    def top(self) -> str:
        if self.is_empty() is False:
            return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def count(self):
        return len(self.data)

    def __str__(self) -> str:
        return f"[{', '.join([f'{{{element}}}' for element in self.data])}]"


if __name__ == "__main__":
    stack = Stack()
    stack.push("abc")
    stack.push("pqr")
    stack.push("xyz")
    print(stack.top())
    print(stack.count())
    print(stack)
    stack.pop()
    print(stack.top())
    print(stack.count())
    print(stack.is_empty())

    stack2 = Stack()
    print(stack2.top())
    print(stack2.push(7))
