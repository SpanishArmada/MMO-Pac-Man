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

            
    def on_message(self, msg):
        incomingData = json.loads(msg)
        row = incomingData["row"]
        col = incomingData["col"]

        grids = []
        pacPos = dict()
        ghostPos = dict()
        for i in players:
            pacPos[str(i.get_id())] = (i.get_x(), i.get_y())
        for i in ghosts:
            ghostPos[str(i.get_id())] = (i.get_x(), i.get_y())
         
        print(len(players))
        print(len(ghosts))
        print(ghosts[15].get_x())
        data = {"grids": grids, "pacPos": pacPos, "ghostPos": ghostPos}
        self.write_message(data)
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
    GE = GameEngine()
    for i in range(20):
        ghosts.append(Ghost(GE, i, i, i))
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()