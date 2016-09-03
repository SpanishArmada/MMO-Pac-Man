import tornado.ioloop
import tornado.web
import tornado.websocket
import os
import json

data = []

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

class ApiHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, *args):
        row = self.get_argument("row")
        col = self.get_argument("col")
        grids = []
        pacPos = dict()
        ghostPos = dict()
        data = {"grids": grids, "pacPos": pacPos, "ghostPos": ghostPos}
        for x in data:
            x.write_message(data)



def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", SocketHandler),
        (r"/update", ApiHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()