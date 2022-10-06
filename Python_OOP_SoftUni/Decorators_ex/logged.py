from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"you called {func.__name__}{args}\nit returned {result}"

    return wrapper


if __name__ == "__main__":
    @logged
    def function(*args):
        return 3 + len(args)


    print(function(4, 4, 4))


    @logged
    def sum_func(a, b):
        return a + b


    print(sum_func(1, 4))
