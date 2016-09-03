

class Ghost:

    #Attribute
    



    #Method

    def __init__(self, game_engine, id, x = -1, y = -1):
        self.id = id
        self.x = x
        self.y = y
        ori = 0
        self.game_engine = game_engine
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_id(self):
        return self.id
