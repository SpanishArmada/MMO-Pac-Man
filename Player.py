import Grid

class Player:
    #Attribute

    #Method
    def __init__(self, game_engine, id, name, x, y):
        self.id = id
        self.name = name
        self.x = x
        self.y = y
        self.orientation = 0
        self.score = 0
        self.powered_up = False
        self.power_duration = 0
        self.has_moved = False
        self.is_dead = False
        self.game_engine = game_engine

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_score(self):
        return self.score

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def is_powered_up(self):
        return self.powered_up

    def pressed_arrow_key(self, arrow_key):
        # Not yet implemented
        return False

    def change_orientation(self, ori):
        self.orientation = orientation

    def get_next_x(self):
        arena = self.game_engine.get_arena()
        if self.orientation == 1 and arena[self.x - 1, self.y].get_type() != Grid.WALL:
            return self.x - 1
        elif self.orientation == 3 and arena[self.x + 1, self.y].get_type() != Grid.WALL:
            return self.x + 1
        return self.x
    
    def get_next_y(self):
        arena = self.game_engine.get_arena()
        if self.orientation == 0 and arena[self.x, self.y - 1].get_type() != Grid.WALL:
            return self.y - 1
        elif self.orientation == 2 and arena[self.x, self.y + 1].get_type() != Grid.WALL:
            return self.y + 1
        return self.y

    def update(self):
        arena = self.game_engine
        next_x = self.get_next_x()
        next_y = self.get_next_y()
        new_grid = arena[next_x, next_y]

        if new_grid.get_type() == Grid.WALL:
            # Immediately recognize that this player has moved
            self.has_moved = True
            return
        
        if powered_up:
            for obj in new_grid.get_objects_on_top():
                obj_new_x = obj.get_next_x()
                obj_new_y = obj.get_next_y()
                if type(obj) == Player:
                    if obj.is_powered_up:
                        continue
                    elif obj.has_moved:
                        self.calculate_score(7)
                    elif ((obj_new_x == next_x) and (obj_new_y == next_y)) or ((obj_new_x == self.x) and (obj_new_y == self.y)):
                        self.calculate_score(7)
                elif ((obj_new_x == next_x) and (obj_new_y == next_y)) or ((obj_new_x == self.x) and (obj_new_y == self.y)):
                    self.calculate_score(5)
        else:
            for obj in new_grid.get_objects_on_top():
                obj_new_x = obj.get_next_x()
                obj_new_y = obj.get_next_y()
                if type(obj) == Player:
                    if not obj.is_powered_up:
                        continue
                    elif obj.has_moved:
                        obj.calculate_score(7)
                        self.is_dead = True
                    elif ((obj_new_x == next_x) and (obj_new_y == next_y)) or ((obj_new_x == self.x) and (obj_new_y == self.y)):
                        obj.calculate_score(7)
                        self.is_dead = True
                elif ((obj_new_x == next_x) and (obj_new_y == next_y)) or ((obj_new_x == self.x) and (obj_new_y == self.y)):
                    self.is_dead = True

        if not self.is_dead:
            if (new_grid.get_type() == Grid.PILL) or (new_grid.get_type() == Grid.CHERRY):    
                self.calculate_score(new_grid.get_type())
            elif new_grid.get_type() == Grid.POWER_UP:
                self.powered_up = True
                self.power_duration = 20

            new_grid.consume()
            self.has_moved = True
            self.x = next_x
            self.y = next_y
    
    def final_update(self):
        self.has_moved = False
        if powered_up:
            self.power_duration -= 1

        if self.power_duration == 0:
            self.powered_up = False


    def calculate_score(self, additional):
        if additional == 1:
            self.score += 10
        elif additional == 3:
            self.score += 100
        elif additional == 5:
            self.score += 200
        elif additional == 7:
            self.score += 400
