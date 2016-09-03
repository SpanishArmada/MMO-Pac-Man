

class Player:

    #Attribute
    

    #Method

    def __init__(self, game_engine, id, x = -1, y = -1):
        self.id = id
        self.x = x
        self.y = y
        self.ori = 0
        self.score = 0
        self.power_up = False
        self.game_engine = game_engine

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_score(self):
        return self.score

    def get_id(self):
        return self.id

    def is_powered_up(self):
        return self.power_up

    def has_pressed_arrow_key(self):
        return False

    def change_orientation(self, ori):
        self.ori = ori

    def can_move_forward(self):
        new_x = get_next_x()
        new_y = get_next_y()

        if(self.game_engine.get_arena().get_grid(new_x, new_y).get_grid().get_typ() == 4):
            return False
        else:
            return True

    def get_next_x(self):
        next_x = self.x
        if(self.ori ==1):
            new_x -= 1
        elif(self.ori ==3):
            new_x += 1
        return next_x
    
    def get_next_y(self):
        next_y = self.y
        if(self.ori == 0):
            new_y -= 1
        elif(self.ori ==2):
            new_y += 1
        return next_y

    def move_forward(self):
        new_x = get_next_x()
        new_y = get_next_y()
        new_grid  = self.game_engine.get_arena().get_grid(new_x, new_y)
        if(new_grid == 1 or new_grid == 3):
            calculate_score(new_grid)
        elif(new_grid ==2):
            self.power_up
        return False

    def calculate_score(self, additional):
        if(additional == 1):
            self.score += 10
        elif(additional == 3):
            self.score += 100
