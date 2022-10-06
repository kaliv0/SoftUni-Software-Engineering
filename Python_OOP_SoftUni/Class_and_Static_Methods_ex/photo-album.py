import math


class PhotoAlbum:
    PAGE_CAPACITY = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / cls.PAGE_CAPACITY))

    def add_photo(self, label: str):
        for p in range(self.pages):
            if len(self.photos[p]) < self.PAGE_CAPACITY:
                self.photos[p].append(label)
                photo_index = self.photos[p].index(label) + 1
                return f"{label} photo added successfully on page {p + 1} slot {photo_index}"
        return "No more free slots"

    def display(self):
        delimiter = '-' * 11
        pages = f'\n{delimiter}\n'.join([('[] ' * len(p)).rstrip(' ') for p in self.photos])
        return f'{delimiter}\n' + pages + f'\n{delimiter}'


if __name__ == "__main__":
    album = PhotoAlbum(2)

    print(album.add_photo("baby"))
    print(album.add_photo("first grade"))
    print(album.add_photo("eight grade"))
    print(album.add_photo("party with friends"))
    print(album.photos)
    print(album.add_photo("prom"))
    print(album.add_photo("wedding"))

    print(album.display())
