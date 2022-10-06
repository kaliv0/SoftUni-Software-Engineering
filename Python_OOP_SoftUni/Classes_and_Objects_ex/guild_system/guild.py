from more_itertools import first_true

from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild != "Unaffiliated":
            if player.guild != self.name:
                return f"Player {player.name} is in another guild."
            return f"Player {player.name} is already in the guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in [p.name for p in self.players]:
            return f"Player {player_name} is not in the guild."

        self.players.remove(first_true(self.players, None, lambda p: p.name == player_name))
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + "\n".join(f"{p.player_info()}" for p in self.players)


if __name__ == "__main__":
    player_ = Player("George", 50, 100)
    print(player_.add_skill("Shield Break", 20))
    print(player_.player_info())
    guild = Guild("UGT")
    print(guild.assign_player(player_))
    print(guild.guild_info())
    print(guild.kick_player("Cyril"))
    print(guild.kick_player("George"))
    print(guild.guild_info())
