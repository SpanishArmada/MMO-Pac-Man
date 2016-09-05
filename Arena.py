import random
from Grid import Grid

class Arena:

    #Attribute

    #Method

    def __init__(self, game_engine, width=1002, height=1002):
        if width % 3 != 0 or height % 3 != 0:
            raise Exception('Width and height has to be divisible by 3.')
        
        self.width = width
        self.height = height
        self.game_engine = game_engine
        self.grids = []
        for i in range(height):
            self.grids.append([])
            for j in range(width):
                self.grids[i].append(Grid(j, i, Grid.WALL))
        self.__next_update = 100
        self.__power_up_spawn_chance = 0.001
        self.__pill_spawn_chance = self.__power_up_spawn_chance + 0.60
        self.__init_pup_chance = 0.001
        self.generate()
        # self.__emptied_grids = {}
        

    def __getitem__(self, p):
        # I strictly expect that parameter 'p' is a tuple of two
        return self.grids[p[1]][p[0]]

    def in_boundary(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
    
    def generate(self):
        next_vid = 0
        vertex_mapper = {}
        inverse_mapper = {}
        edge_list = []
        parent = []
        
        for i in range(1, self.height, 3):
            for j in range(1, self.width, 3):
                self[j, i].set_type(Grid.EMPTY)
                
                vertex_mapper[next_vid] = j, i
                inverse_mapper[j, i] = next_vid
                parent.append(next_vid)
                
                next_vid = next_vid + 1

        for x in range(1, self.width, 3):
            for y in range(1, self.height, 3):
                a = inverse_mapper[x, y]
                if self.in_boundary(x + 3, y):
                    b = inverse_mapper[x + 3, y]
                    edge_list.append((a, b, ))
                
                if self.in_boundary(x, y + 3):
                    b = inverse_mapper[x, y + 3]
                    edge_list.append((a, b, ))

        random.shuffle(edge_list)

        def find(u):
            if parent[u] == u:
                return u
            
            parent[u] = find(parent[u])
            return parent[u]

        def is_same(u, v):
            return find(u) == find(v)

        def connect(u, v):
            parent[find(v)] = parent[find(u)]

        connected = set()
        for a, b in edge_list:
            if is_same(a, b):
                continue

            connect(a, b)
            connected.add((a, b, ))
            # x <= next_x and y <= next_y
            x, y = vertex_mapper[a]
            next_x, next_y = vertex_mapper[b]

            for j in range(x, next_x + 1):
                for i in range(y, next_y + 1):
                    self[j, i].set_type(Grid.EMPTY)

        n_random = self.width + self.height
        for a, b in edge_list:
            if n_random <= 0:
                break
            n_random = n_random - 1
            
            if (a, b, ) in connected:
                continue

            connected.add((a, b, ))
            # x <= next_x and y <= next_y
            x, y = vertex_mapper[a]
            next_x, next_y = vertex_mapper[b]

            for j in range(x, next_x + 1):
                for i in range(y, next_y + 1):
                    self[j, i].set_type(Grid.EMPTY)
        
        for i in range(self.height):
            for j in range(self.width):
                if self[j, i].get_type() == Grid.EMPTY:
                    self[j, i].set_type(Grid.PILL)
                    if random.random() < self.__init_pup_chance:
                        self[j, i].set_type(Grid.POWER_UP)
        
        return True

    def get_grid(self, x, y):
        return self.grids[y][x]

    def late_update(self):
        # temp = []
        # for (x, y), t in self.__emptied_grids.items():
        #     if t <= 0:
        #         self[x, y].set_type(Grid.PILL)
        #         temp.append((x, y, ))
        #     else:
        #         self.__emptied_grids[x, y] = t - 1
        
        # Preventing RTE
        # for key in temp:
        #     del self.__emptied_grids[key]

        if self.__next_update <= 0:
            self.__next_update = random.randint(100, 200)

            for i in range(1, self.height):
                for j in range(1, self.width):
                    if self[j, i].get_type() != Grid.EMPTY:
                        continue

                    r = random.random()
                    if r < self.__power_up_spawn_chance:
                        self[j, i].set_type(Grid.POWER_UP)
                    elif r < self.__pill_spawn_chance:
                        self[j, i].set_type(Grid.PILL)

        else:
            self.__next_update = self.__next_update - 1

    def take(self, x, y):
        T = self[x, y].consume()

        # If recently emptied
        # if T != Grid.EMPTY and self[x, y].get_type() == Grid.EMPTY:
        #     self.__emptied_grids[x, y] = random.randint(100, 200)

        return T

    def lift(self, who):
        self[who.x, who.y].remove_object_on_top(who)

    def move(self, who, new_x, new_y):
        self.lift(who)
        self[new_x, new_y].insert_object_on_top(who)
