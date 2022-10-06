from functools import wraps


def multiply(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args):
            return function(*args) * times

        return wrapper

    return decorator


if __name__ == "__main__":
    @multiply(3)
    def add_ten(number):
        return number + 10


    print(add_ten(3))


    @multiply(5)
    def add_ten(number):
        return number + 10


    print(add_ten(6))
