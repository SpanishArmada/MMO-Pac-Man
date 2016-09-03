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
            counter += 1
            players.append(Player(GE, counter, 1, 1))
            msg = {"type": 0, "player_id": counter}
            self.write_message(msg)

            
    def on_message(self, msg):
        incoming_data = json.loads(msg)
        msg_type = incoming_data["type"]
        print(msg_type)
        if(msg_type == 0):
            row = incoming_data["row"]
            col = incoming_data["col"]
            player_id = incoming_data["player_id"]
            print("row", row)
            local_grids = GE.get_arena().grids[row - 9:row + 10]
            print("len", len(local_grids))
            grids = []
            food_pos = []
            for i in local_grids:
                current_row = i[col - 16:col + 17]
                r = []
                for j in current_row:
                    if(j.get_typ == 4):
                        r.append(1)
                    else:
                        r.append(0)
                    if(j.get_typ == 1):
                        food_pospend([j.get_x(), j.get_y()])
                grids.append(r)
            print(grids)
            pac_pos = dict()
            ghost_pos = dict()
            for i in players:
                pac_pos[str(i.get_id())] = (i.get_x(), i.get_y())
            for i in ghosts:
                ghost_pos[str(i.get_id())] = (i.get_x(), i.get_y())
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
            #TODO: remove player
            #players.remove()
            

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