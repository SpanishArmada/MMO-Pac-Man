

class Ghost:

    #Attribute
    next_id = 0
    



    #Method

    def __init__(self, game_engine, x = -1, y = -1, id):
        self.id = id
        self.x = x
        self.y = y
        ori = 0
        self.game_engine = game_engine
        
