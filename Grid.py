class Grid:


    def __init__(self, x=-1, y=-1):
        self.x = x
        self.y = y
        self.typ = 0
        self.ghosts = []
        self.player = []

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_typ(self):
        return self.typ

    def get_ghosts(self):
        return self.ghosts

    def get_players(self):
        return self.player

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_typ(self, typ):
        self.typ = typ
    
    def ghost_come(self, ghost):
        self.ghosts.append(ghost)

    def ghost_leave(self, ghost):
        self.ghosts.remove(ghost)

    def player_come(self):
        self.players.append(player)

    def player_leave(self):
        self.players.remove(player)
