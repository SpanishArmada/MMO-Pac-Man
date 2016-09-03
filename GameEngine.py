from Arena import Arena
from Player import Player
from Ghost import Ghost
from threading import Timer

class GameEngine:
    def __init__(self):
        self.__players = {}
        self.__arena = Arena(self, 2001, 2001)
        self.__ghosts = {}

        self.__sec_per_tick = .5
        self.__timer = Timer(self.__sec_per_tick, self.update)

    def update(self):
        for player in self.__players:
            player.early_update()

        for player in self.__players:
            player.update();

        for ghost in self.__ghosts:
            ghost.update()

    def start(self):
        self.__timer.start()

    def stop(self):
        self.__timer.stop()

    def get_arena(self):
        return self.__arena

    def get_players(self):
        return self.__players

    def get_player(self, pid):
        return self.__players[pid]

    def get_ghosts(self):
        return self.__ghosts

    def get_sec_per_tick(self):
        return self.__sec_per_tick

    def new_player(self, player):
        self.__players[player.get_id()] = player

    def new_ghost(self):
        pass

    def delete_player(self, pid):
        del self.__players[pid]

    def delete_ghost(self, gid):
        del self.__ghosts[gid]
