import tornado.ioloop
import tornado.web
import tornado.websocket
import os
import json
from GameEngine import GameEngine
from Arena import Arena

data = []
players = []
ghosts = []
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index1.html")

class SocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        if(self not in data):
            data.append(self)
            
    def on_message(self, msg):
        incomingData = json.loads(msg)
        row = incomingData["row"]
        col = incomingData["col"]

        grids = []
        pacPos = dict()
        ghostPos = dict()
        
        pacPos["p1"] = 1
        pacPos["p2"] = 2

        data = {"grids": grids, "pacPos": pacPos, "ghostPos": ghostPos}
        self.write_message(data)
    def on_close(self):
        if self in data:
            data.remove(self)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", SocketHandler),
    ])

if __name__ == "__main__":
    GE = GameEngine()

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()