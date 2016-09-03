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
        self.has_move = False
        self.is_death = False
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

    def has_pressed_arrow_key(self):
        # Not yet implemented
        return False

    def change_orientation(self, ori):
        self.orientation = orientation

    def can_move_forward(self):
        new_x = self.get_next_x()
        new_y = self.get_next_y()

        if(self.game_engine.get_arena().get_grid(new_x, new_y).get_type() == Grid.WALL):
            return False
        else:
            return True

    def get_next_x(self):
        if (self.orientation == 1) and (game_engine.get_arena().get_grid(self.x - 1, self.y).get_type() != Grid.WALL):
            return self.x - 1
        elif (self.orientation == 3) and (game_engine.get_arena().get_grid(self.x + 1, self.y).get_type() != Grid.WALL):
            return self.x + 1
        return self.x
    
    def get_next_y(self):
        if (self.orientation == 0) and (game_engine.get_arena().get_grid(self.x, self.y - 1).get_type() != Grid.WALL) :
            return self.y - 1
        elif (self.orientation == 2) and (game_engine.get_arena().get_grid(self.x, self.y + 1).get_type() != Grid.WALL):
            return self.y + 1
        return self.y

    def move_forward(self):
        new_x = self.get_next_x()
        new_y = self.get_next_y()

        return self.process_player(new_x, new_y)

    def process_player(self, next_x, next_y):
        new_grid = self.game_engine.get_arena().get_grid(next_x, next_y)

        if powered_up:
            for obj in new_grid.get_objects_on_top():
                obj_new_x = obj.get_next_x()
                obj_new_y = obj.get_next_y()
                if type(obj) == Player:
                    if obj.is_powered_up:
                        continue
                    elif obj.has_move:
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
                    elif obj.has_move:
                        obj.calculate_score(7)
                        self.is_death = True
                    elif ((obj_new_x == next_x) and (obj_new_y == next_y)) or ((obj_new_x == self.x) and (obj_new_y == self.y)):
                        obj.calculate_score(7)
                        self.is_death = True
                elif ((obj_new_x == next_x) and (obj_new_y == next_y)) or ((obj_new_x == self.x) and (obj_new_y == self.y)):
                    self.is_death = True
        if not self.is_death:
            if (new_grid.get_type() == Grid.PILL) or (new_grid.get_type() == Grid.CHERRY):
                new_grid.consume()
                self.calculate_score(new_grid.get_type())
            elif new_grid.get_type() == Grid.POWER_UP:
                new_grid.consume()
                self.powered_up = True
                self.power_duration = 20
    
    def final_update(self):
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
