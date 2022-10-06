from typing import List

from more_itertools import first_true

from song import Song
from album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in [a.name for a in self.albums]:
            return f"Album {album_name} is not found."

        curr_album = first_true(self.albums, None, lambda a: a.name == album_name)
        if curr_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(curr_album)
        return f"Album {album_name} has been removed."

    def details(self):
        return f"Band {self.name}\n" + "\n".join([f"== {album.details()}" for album in self.albums])


if __name__ == "__main__":
    song = Song("Running in the 90s", 3.45, False)
    print(song.get_info())
    album_ = Album("Initial D", song)
    second_song = Song("Around the World", 2.34, False)
    print(album_.add_song(second_song))
    print(album_.details())
    print(album_.publish())
    band = Band("Manuel")
    print(band.add_album(album_))
    print(band.remove_album("Initial D"))
    print(band.details())
