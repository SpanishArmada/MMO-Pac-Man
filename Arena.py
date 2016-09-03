from Grid import Grid
import random

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
        self.generate()
        print("done")

    def __getitem__(self, p):
        # I strictly expect that parameter 'p' is a tuple of two
        return self.grids[p[0]][p[1]]

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
                self[i, j].set_type(Grid.EMPTY)
                
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
                    self[i, j].set_type(Grid.EMPTY)

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
                    self[i, j].set_type(Grid.EMPTY)
        
        return True
    
    def get_grid(self, x, y):
        return self.grids[y][x]
