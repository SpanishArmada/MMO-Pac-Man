import tornado.ioloop
import tornado.web
import tornado.websocket
import os
import json


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index1.html")
        
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()