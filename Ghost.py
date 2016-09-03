import random
import Grid

class Ghost:

    #Attribute
    orientation_choices = [0, 1, 2, 3]

    #Method

    def __init__(self, game_engine, id, ghost_type, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.orientation = 0
        self.game_engine = game_engine
        self.ghost_type = ghost_type

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_id(self):
        return self.id
    
    def get_next_x(self):
        if self.orientation == 1:
            return self.x - 1
        elif self.orientation == 3:
            return self.y + 1
        return self.x
    
    def get_next_y(self):
        if self.orientation == 0:
            return self.y - 1
        elif self.orientation == 2:
            return self.y + 1
        return self.y

    def set_random_orientation(self):
        arena = game_engine.__arena
        self.orientation = random.choice(orientation_choices)
        while True:
            new_x = get_next_x()
            new_y = get_next_y()
            if arena.grids[new_x][new_y].get_typ() != Grid.WALL:
                break
            self.ori = random.choice(orientation_choices)
        self.x = new_x
        self.y = new_y
