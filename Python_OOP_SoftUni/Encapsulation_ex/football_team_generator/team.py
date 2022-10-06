from typing import List

from player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        player = [p for p in self.__players if p.name == player_name]
        if not player:
            return f"Player {player_name} not found"
        player_index = self.__players.index(player[0])
        return self.__players.pop(player_index)
