import Grid
import GameEngine

class ClassName:

    #Attribute
    self.grids = []
    self.game_engine = None

    #Method

    def __init__(self, game_engine, x, y):
        self.game_engine = game_engine
        for i in range(x):
            for i in range(y):
                self.grids = Grid(x,y)

    def generate_map(self):
        return None

    def get_grid_typ(self, x, y):
        return self.grids[x][y].get_typ

    def set_grid_typ(self, x, y, typ):
        self.grids[x][y].set_typ(typ)
        
