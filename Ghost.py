import GameEngine

class Player:

    #Attribute
    next_id = 0
    self.id = next_id
    next_id = next_id + 1

    self.x = -1
    self.y = -1
    self.ori = 0
    self.game_engine = None


    #Method

    def __init__(self, game_engine, x = -1, y = -1):
        self.x = x
        self.y = y
        self.game_engine = game_engine
        
