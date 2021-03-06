from Arena import Arena
from Player import Player
from Ghost import Ghost

class GameEngine:
    def __init__(self, arena_width=501, arena_height=501, max_num_ghost=35000):
        
        self.arena_width = arena_width
        self.arena_height = arena_height
        self.max_num_ghost = max_num_ghost
        self.arena = Arena(self, arena_width, arena_height)
        self.players = {}
        self.ghosts = {}

        self.__sec_per_tick = .5

    def update(self):
        
        for player in self.players.values():
            player.early_update()
        
        for ghost in self.ghosts.values():
            ghost.early_update()

        for player in self.players.values():
            player.update()

        for ghost in self.ghosts.values():
            ghost.update()

        players_to_delete = []
        for player in self.players.values():
            if player.is_dead:
                players_to_delete.append(player.id)
        
        for pid in players_to_delete:
            self.delete_player(pid)

        ghosts_to_delete = []
        for ghost in self.ghosts.values():
            if ghost.is_dead:
                ghosts_to_delete.append(ghost.id)
        
        for gid in ghosts_to_delete:
            self.delete_ghost(gid)

        self.arena.late_update()

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

    def add_ghost(self, counter, ghost_type, x, y):
        ghost = Ghost(self, counter, ghost_type, x, y)
        
        self.ghosts[counter] = ghost
        self.arena[x, y].insert_object_on_top(ghost)
    
    def new_player(self, player):
        self.players[player.get_id()] = player

    def new_ghost(self):
        raise Exception("Not implemented!")

    def delete_player(self, pid):
        p = self.players[pid]
        self.arena.lift(p)
        del self.players[pid]

    def delete_ghost(self, gid):
        g = self.ghosts[gid]
        self.arena.lift(g)
        del self.ghosts[gid]
