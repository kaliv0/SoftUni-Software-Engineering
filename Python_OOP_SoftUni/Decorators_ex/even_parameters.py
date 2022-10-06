from functools import wraps


def even_parameters(func):
    @wraps(func)
    def wrapper(*args):
        if [n for n in args if isinstance(n, str) or n % 2 != 0]:
            return "Please use only even numbers!"
        return func(*args)

    return wrapper


if __name__ == "__main__":
    @even_parameters
    def add(a, b):
        return a + b


    print(add(2, 4))
    print(add("Peter", 1))


    @even_parameters
    def multiply(*nums):
        result = 1
        for num in nums:
            result *= num
        return result


    print(multiply(2, 4, 6, 8))
    print(multiply(2, 4, 9, 8))
