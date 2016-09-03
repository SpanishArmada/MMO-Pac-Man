from Arena import Arena
from Player import Player
from Ghost import Ghost
from threading import Timer
import random

class GameEngine:
    def __init__(self, arena_width=501, arena_height=501, max_num_ghost=35000):
        self.arena_width = arena_width
        self.arena_height = arena_height
        self.max_num_ghost = max_num_ghost
        
        self.players = {}
        self.arena = Arena(self, arena_width, arena_height)
        self.ghosts = {}

        self.__sec_per_tick = .5
        self.__timer = Timer(self.__sec_per_tick, self.update)

    def update(self):
        self.__timer = Timer(self.__sec_per_tick, self.update)
        self.__timer.start()
        
        for player in self.players.values():
            # print("Gede")
            player.early_update()
        
        for ghost in self.ghosts.values():
            # print("Bagus")
            ghost.early_update()

        

        for player in self.players.values():
            # print("Bayu")
            player.update()

        for ghost in self.ghosts.values():
            # print("Pentium")
            ghost.update()

        self.arena.late_update()

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
        player = Player(self, counter, name, x, y)

        self.players[counter] = player
        self.arena[x, y].insert_object_on_top(player)

    def add_ghost(self, counter, ghost_type, y, x):
        ghost = Ghost(self, counter, ghost_type, y, x)

        self.ghosts[counter] = ghost
        self.arena[x, y].insert_object_on_top(ghost)
    
    def new_player(self, player):
        self.players[player.get_id()] = player

    def new_ghost(self):
        raise Exception("Not implemented!")

    def delete_player(self, pid):
        del self.players[pid]

    def delete_ghost(self, gid):
        del self.ghosts[gid]
