class Grid:

    EMPTY = 0
    PILL = 1
    POWER_UP = 2
    CHERRY = 3
    WALL = 4

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__type = Grid.EMPTY
        self.objects_on_top = []

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_type(self):
        return self.__type
    
    def get_objects_on_top(self):
        return self.objects_on_top
    
    def insert_object_on_top(self, obj):
        self.objects_on_top.append(obj)

    def remove_object_on_top(self, obj):
        self.objects_on_top.remove(obj)
    
    def set_type(self, T):
        self.__type = T
    
    def consume(self):
        if self.__type == Grid.WALL:
            raise Exception('You cannot consume wall!')
        
        T = self.__type
        self.__type = Grid.EMPTY
        return T
