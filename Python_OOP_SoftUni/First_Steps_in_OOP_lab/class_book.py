class Book:
    def __init__(self, name: str, author: str, pages: int):
        self._name = name
        self._author = author
        self._pages = pages

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages
