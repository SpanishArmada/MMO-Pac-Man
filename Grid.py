class Grid:


    def __init__(self, x=-1, y=-1):
        self.x = x
        self.y = y
        self.typ = 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getTyp(self):
        return self.typ

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def setTyp(self, typ):
        self.typ = typ
