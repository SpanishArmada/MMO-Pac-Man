import random
from Grid import Grid
import Player

class Ghost:
    def __init__(self, game_engine, id, ghost_type, x, y):
        self.orientation_choices = [0, 1, 2, 3]
        self.id = id
        self.x = x
        self.y = y
        self.orientation = 0
        self.has_moved = False
        self.is_dead = False
        self.game_engine = game_engine
        self.ghost_type = ghost_type

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_id(self):
        return self.id
    
    def get_next_x(self, orientation=self.orientation):
        if self.orientation == 0:
            return self.x - 1
        elif self.orientation == 2:
            return self.x + 1
        return self.x
    
    def get_next_y(self):
        if self.orientation == 1:
            return self.y - 1
        elif self.orientation == 3:
            return self.y + 1
        return self.y

    def update(self):
        arena = self.game_engine.get_arena()
        next_x = self.get_next_x()
        next_y = self.get_next_y()
        new_grid = arena[next_x, next_y]
        arr = filter(lambda obj: self != obj, new_grid.get_objects_on_top())

        for obj in arr:
            obj_new_x, obj_new_y = obj.get_next_x(), obj.get_new_y()
            if type(obj) == Player:
                if obj.is_powered_up:
                    if obj.has_moved:
                        obj.calculate_score(5)
                        self.is_dead = True
                    elif obj_new_x == next_x and obj_new_y == next_y or obj_new_x == self.x and obj_new_y == self.y:
                        obj.calculate_score(5)
                        self.is_dead = True
                else:
                    if obj.has_moved:
                        obj.is_dead = True
                    elif obj_new_x == next_x and obj_new_y == next_y or obj_new_x == self.x and obj_new_y == self.y:
                        obj.is_dead = True
        
        self.has_moved = True
        self.x = next_x
        self.y = next_y

    def early_update(self):
        self.has_moved = False
        
        arena = self.game_engine.arena

        possible_direction = []
        for dir in range(0, 4):
            self.orientation = dir
            new_x, new_y = self.get_new_x(), self.get_new_y()
            if x, y != new_x, new_y:
                possible_direction.append(dir)
        
        self.orientation = random.choice(possible_direction)
