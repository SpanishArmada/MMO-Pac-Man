from Arena import Arena
from Player import Player
from Ghost import Ghost
from threading import Timer
import random

class GameEngine:
    def __init__(self, arena_width=2001, arena_height=2001, max_num_ghost=35000):
        self.arena_width = arena_width
        self.arena_height = arena_height
        self.max_num_ghost = max_num_ghost
        
        self.players = {}
        self.arena = Arena(self, arena_width, arena_height)
        self.ghosts = {}

        self.__sec_per_tick = .5
        self.__timer = Timer(self.__sec_per_tick, self.update)

    def update(self):
        for player in self.players.values():
            player.early_update()
        
        for ghost in self.ghosts.values():
            ghost.early_update()

        for player in self.players.values():
            player.update()

        for ghost in self.ghosts.values():
            ghost.update()

    def start(self):
        self.__timer.start()

    def stop(self):
        self.__timer.cancel()

    def get_arena(self):
        return self.arena

    def get_players(self):
        return self.players.values()

    def get_player(self, pid):
        return self.players[pid]

    def get_ghosts(self):
        return self.ghosts.values()

    def get_sec_per_tick(self):
        return self.__sec_per_tick
    
    def add_player(self, counter, name, x, y):
        self.players[counter] = Player(self, counter, name, x, y)

    def add_ghost(self, counter, ghost_type, y, x):
        self.ghosts[counter] = Ghost(self, counter, ghost_type, y, x)
    
    def new_player(self, player):
        self.players[player.get_id()] = player

    def new_ghost(self):
        pass

    def delete_player(self, pid):
        del self.players[pid]

    def delete_ghost(self, gid):
        del self.ghosts[gid]
