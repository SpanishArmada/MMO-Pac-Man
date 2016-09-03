import tornado.ioloop
import tornado.web
import tornado.websocket
import os
import json
from GameEngine import GameEngine
from Arena import Arena
from Player import Player
from Ghost import Ghost
from random import randint

data = []
players = []
ghosts = []
counter = 0
GE = None
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index1.html")

class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    def open(self):
        global counter
        if(self not in data):
            data.append(self)
            counter += 1
            player_x = 1
            player_y = 1
            players.append(Player(GE, counter, "dummy_name", player_x, player_y))
            msg = {"type": 0, "player_id": counter, "x": player_x, "y": player_y}
            self.write_message(msg)
            
    def on_message(self, msg):
        global counter
        incoming_data = json.loads(msg)
        msg_type = incoming_data["type"]
        print(msg_type)
        if(msg_type == 0):
            row = incoming_data["row"]
            col = incoming_data["col"]
            player_id = incoming_data["player_id"]
            player_name = incoming_data["player_name"]

            p = None
            for x in players:
                if x.get_id() == player_id:
                    x.name = player_name
                    p = x
                    break
                    
            left_boundary = col - 9
            right_boundary = col + 9
            top_boundary = row - 16
            bottom_boundary = row + 16
            local_grids = GE.get_arena().grids[top_boundary:bottom_boundary+1]
            
            grids = []
            food_pos = []
            for i in local_grids:
                current_row = i[left_boundary:right_boundary]
                r = []
                for j in current_row:
                    if(j.get_type() == 4):
                        r.append(1)
                    else:
                        r.append(0)
                    if(j.get_type() == 1):
                        food_pos.append({"x": j.get_x(), "y": j.get_y()})
                grids.append(r)
            print(grids)
            pac_pos = dict()
            ghost_pos = dict()
            for i in players:
                player_row = i.get_y()
                player_col = i.get_x()
                if(left_boundary <= player_col <= right_boundary and top_boundary <= player_row <= bottom_boundary):
                    pac_pos[str(i.get_id())] = {"x": i.get_x(), "y": i.get_y(), "orientation": i.orientation, "player_name": i.name}

            for i in ghosts:
                ghost_row = i.get_y()
                ghost_col = i.get_x()
                if(left_boundary <= ghost_col <= right_boundary and top_boundary <= ghost_row <= bottom_boundary):
                    ghost_pos[str(i.get_id())] = {"x": i.get_x(), "y": i.get_y(), "orientation": i.orientation, "ghost_type": i.ghost_type}

            print(len(players))
            data = {"type": 1, "grids": grids, "pac_pos": pac_pos, "ghost_pos": ghost_pos, "food_pos": food_pos, "score": p.get_score()}
            self.write_message(data)
        else:
            # closed
            print("in")
            player_id = incoming_data["player_id"]
            print("delete", player_id)
            p = None
            for x in players:
                if x.get_id() == player_id:
                    p = x
                    break
            players.remove(p)

    def on_close(self):
        if self in data:
            data.remove(self)
            

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", SocketHandler),
    ])

if __name__ == "__main__":
    global counter
    global GE
    GE = GameEngine()
    # for i in range(20):
    #     ghosts.append(Ghost(GE, i, i, i))
    ghost_counter = 1
    print("in")
    for i in range(0, 2000, 20):
        for j in range(0, 2000, 30):
            for k in range(3):
                while(True):
                    ghost_row = randint(i, min(i+18, 1999))
                    ghost_col = randint(j, min(j+32, 1999))
                    if(GE.get_arena().grids[ghost_row][ghost_col].get_type() != 4):
                        break
                ghosts.append(Ghost(GE, ghost_counter, ghost_counter % 4, ghost_col, ghost_row))
                ghost_counter += 1
    print(ghosts[0].get_x(), ghosts[0].get_y())
    print(ghost_counter)
    print(ghosts[10000].get_x(), ghosts[10000].get_y())
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()