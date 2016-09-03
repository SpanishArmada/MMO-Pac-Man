import tornado.ioloop
import tornado.web
import tornado.websocket
import os
import json
from GameEngine import GameEngine
from Arena import Arena
from Player import Player
from Ghost import Ghost

data = []
players = []
ghosts = []
counter = 0
GE = None
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index1.html")

class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        global counter
        if(self not in data):
            data.append(self)
            msg = {"type": 0, "player_id": counter + 1}
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

            counter += 1
            players.append(Player(GE, counter, player_name, 1, 1))
            
            local_grids = GE.get_arena().grids[row - 9:row + 10]
            
            grids = []
            food_pos = []
            for i in local_grids:
                current_row = i[col - 16:col + 17]
                r = []
                for j in current_row:
                    if(j.get_type() == 4):
                        r.append(1)
                    else:
                        r.append(0)
                    if(j.get_type() == 1):
                        food_pos.append([j.get_x(), j.get_y()])
                grids.append(r)
            print(grids)
            pac_pos = dict()
            ghost_pos = dict()
            for i in players:
                pac_pos[str(i.get_id())] = {"x": i.get_x(), "y": i.get_y(), "orientation": i.orientation, "player_name": i.name} 
            for i in ghosts:
                ghost_pos[str(i.get_id())] = {"x": i.get_x(), "y": i.get_y(), "orientation": i.orientation} 
            print(len(players))
            p = None
            for x in players:
                if x.get_id() == player_id:
                    p = x
                    break
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
    for i in range(20):
        ghosts.append(Ghost(GE, i, i, i))
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()