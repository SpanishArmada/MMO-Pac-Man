class Grid:

    self.x = -1
    self.y = -1
    self.typ = 0

    def __init__(self, x=-1, y=-1):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_typ(self):
        return self.typ

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def set_typ(self, typ):
        self.typ = typ
