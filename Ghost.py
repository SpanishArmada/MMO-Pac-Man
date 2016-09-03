import random

class Ghost:

    #Attribute
    



    #Method

    def __init__(self, game_engine, id, x = -1, y = -1):
        self.id = id
        self.x = x
        self.y = y
        self.ori = 0
        self.game_engine = game_engine
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_id(self):
        return self.id
    
    def get_next_x(self):
        next_x = self.x
        if(self.ori ==1):
            next_x -= 1
        elif(self.ori ==3):
            next_x += 1
        return next_x
    
    def get_next_y(self):
        next_y = self.y
        if(self.ori == 0):
            next_y -= 1
        elif(self.ori ==2):
            next_y += 1
        return next_y

    def set_random_orientation(self):
        choices = [0, 1, 2, 3]
        arena = game_engine.__arena
        new_x = 0
        new_y = 0
        self.ori = random.choice(choices)
        while(True):
            new_x = get_next_x()
            new_y = get_next_y()
            if(arena.grids[new_x][new_y].get_typ() != 4):
                break
            self.ori = random.choice(choices)
        self.x = new_x
        self.y = new_y


            


