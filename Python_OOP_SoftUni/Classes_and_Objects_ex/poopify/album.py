from more_itertools import first_true

from song import Song


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.published = False
        self.songs = []
        self.songs.extend(songs)

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        if song_name not in [s.name for s in self.songs]:
            return "Song is not in the album."

        self.songs.remove(first_true(self.songs, None, lambda s: s.name == song_name))
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n" + "\n".join([f"== {song.get_info()}" for song in self.songs])
