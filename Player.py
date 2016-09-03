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
        new_x = get_next_x()
        new_y = get_next_y()

        if(self.game_engine.get_arena().get_grid(new_x, new_y).get_type() == Grid.WALL):
            return False
        else:
            return True

    def get_next_x(self):
        if self.orientation == 1:
            return self.x - 1
        elif self.orientation == 3:
            return self.x + 1
        return self.x
    
    def get_next_y(self):
        if self.orientation == 0:
            return self.y - 1
        elif self.orientation == 2:
            return self.y + 1
        return self.y

    def move_forward(self):
        new_x = get_next_x()
        new_y = get_next_y()

        if self.game_engine.get_arena().get_grid(new_x, new_y).get_type() == Grid.WALL:
            return self.process_player(self.x, self.y)
        else:
            return self.process_player(new_x, new_y)

    def process_player(self, next_x, next_y):
        life = True

        old_grid = self.game_engine.get_arena().get_grid(self.x, self.y)
        new_grid = self.game_engine.get_arena().get_grid(next_x, next_y)

        if powered_up:
            for obj in new_grid.get_objects_on_top():
                if (type(obj) == Ghost) or (obj.is_powered_up() == False):
                    return False
                    #check orientation

    
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
