import GameEngine

class Player:

    #Attribute
    next_id = 0
    id = next_id
    next_id = next_id + 1

    x = -1
    y = -1
    ori = 0
    game_engine = None


    #Method

    def __init__(self, game_engine, x = -1, y = -1):
        self.x = x
        self.y = y
        self.game_engine = game_engine
        
