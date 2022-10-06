from typing import List

from more_itertools import first_true

from room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(name=f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        # curr_room = [r for r in self.rooms if r.number == room_number]
        # if curr_room:
        #     curr_room[0].take_room(people)
        room = first_true(self.rooms, None, lambda r: r.number == room_number)
        if room:
            room.take_room(people)

    def free_room(self, room_number):
        # curr_room = [r for r in self.rooms if r.number == room_number]
        # if curr_room:
        #     curr_room[0].free_room()
        room = first_true(self.rooms, None, lambda r: r.number == room_number)
        if room:
            room.free_room()

    def status(self):
        return f'''Hotel {self.name} has {self.guests} total guests
Free rooms: {", ".join([str(r.number) for r in self.rooms if not r.is_taken])}
Taken rooms: {", ".join([str(r.number) for r in self.rooms if r.is_taken])}'''
