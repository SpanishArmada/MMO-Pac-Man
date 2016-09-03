from Grid import Grid

class Player:
    #Attribute
    PILL = Grid.PILL
    CHERRY = Grid.CHERRY
    GHOST = 10
    OTHER_PLAYER = 11
    
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

        T = game_engine.arena.take(x, y)
        self.add_score(T)

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
        self.orientation = arrow_key

    def get_next_x(self):
        arena = self.game_engine.arena
        if self.orientation == 0 and arena[self.x - 1, self.y].get_type() != Grid.WALL:
            return self.x - 1
        elif self.orientation == 2 and arena[self.x + 1, self.y].get_type() != Grid.WALL:
            return self.x + 1
        return self.x
    
    def get_next_y(self):
        arena = self.game_engine.arena
        if self.orientation == 1 and arena[self.x, self.y - 1].get_type() != Grid.WALL:
            return self.y - 1
        elif self.orientation == 3 and arena[self.x, self.y + 1].get_type() != Grid.WALL:
            return self.y + 1
        return self.y

    def update(self):
        arena = self.game_engine.arena
        next_x = self.get_next_x()
        next_y = self.get_next_y()
        new_grid = arena[next_x, next_y]
        arr = filter(lambda obj: self != obj, new_grid.get_objects_on_top())

        if self.powered_up:
            for obj in arr:
                obj_new_x, obj_new_y = obj.get_next_x(), obj.get_next_y()
                if type(obj) == Player:
                    if obj.is_powered_up:
                        continue
                    elif obj.has_moved:
                        self.add_score(Player.OTHER_PLAYER)
                        obj.is_dead = True
                    elif obj_new_x == next_x and obj_new_y == next_y or obj_new_x == self.x and obj_new_y == self.y:
                        self.add_score(Player.OTHER_PLAYER)
                        obj.is_dead = True
                elif obj_new_x == next_x and obj_new_y == next_y or obj_new_x == self.x and obj_new_y == self.y:
                    self.add_score(Player.GHOST)
                    obj.is_dead = True
        else:
            for obj in arr:
                obj_new_x, obj_new_y = obj.get_next_x(), obj.get_next_y()
                if type(obj) == Player:
                    if not obj.is_powered_up:
                        continue
                    elif obj.has_moved:
                        obj.add_score(Player.OTHER_PLAYER)
                        self.is_dead = True
                    elif obj_new_x == next_x and obj_new_y == next_y or obj_new_x == self.x and obj_new_y == self.y:
                        obj.add_score(Player.OTHER_PLAYER)
                        self.is_dead = True
                elif obj_new_x == next_x and obj_new_y == next_y or obj_new_x == self.x and obj_new_y == self.y:
                    self.is_dead = True

        arena.move(self, next_x, next_y)

        if not self.is_dead:

            T = arena.take(next_x, next_y)
            if T == Grid.PILL or T == Grid.CHERRY:    
                self.add_score(T)
            elif T == Grid.POWER_UP:
                self.powered_up = True
                self.power_duration = 20

        self.has_moved = True

        self.x = next_x
        self.y = next_y

    
    def early_update(self):
        self.has_moved = False
        self.power_duration = max(0, self.power_duration - 1)
        self.powered_up = self.power_duration > 0

    def add_score(self, case):
        if case == Player.PILL:
            self.score += 10
        elif case == Player.CHERRY:
            self.score += 100
        elif case == Player.GHOST:
            self.score += 200
        elif case == Player.OTHER_PLAYER:
            self.score += 400
