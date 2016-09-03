from Grid import Grid

class Arena:

    #Attribute

    #Method

    def __init__(self, game_engine, x, y):
        self.game_engine = game_engine
        self.grids = []
        for i in range(x):
            self.grids.append([])
            for j in range(y):
                self.grids[i].append(Grid(x,y))

    def generate_map(self):
        return None

    def get_grid_typ(self, x, y):
        return self.grids[x][y].get_typ

    def set_grid_typ(self, x, y, typ):
        self.grids[x][y].set_typ(typ)
        
