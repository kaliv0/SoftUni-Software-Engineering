from functools import wraps


def tags(tag: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper

    return decorator


if __name__ == "__main__":
    @tags('p')
    def join_strings(*args):
        return "".join(args)


    print(join_strings("Hello", " you!"))


    @tags('h1')
    def to_upper(text):
        return text.upper()


    print(to_upper('hello'))
