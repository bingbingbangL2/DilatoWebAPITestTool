#-coding:UTF8-*-
'''
Created on Jan 18, 2016

@author: bxia
'''

import tornado.web
import tornado.httpserver
from tornado.options import define, options 

define("port", default = 8888, type = int)

# vcip = "10.155.191.216"
# user = "administrator@vsphere.local"
# password = "Admin!23"

class DoNetdumpActionHandler(tornado.web.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        arguments = self.request.arguments
        if arguments:
            self.write("hello world")
        else:
            self.write("No arguments")

class RemoveDCActionHandler(tornado.web.RequestHandler):
    def get(self):
        arguments = self.request.arguments
        if arguments:
            self.write("hello world")
        else:
            self.write("No arguments")
    def post(self):
        arguments = self.request.arguments
        if arguments:
            self.write("hello world")
        else:
            self.write("No arguments")
            
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.post()
    def post(self):
        arguments = self.request.arguments
        if arguments:
            
            print arguments
            self.write(self.get_argument('who'))
        else:
            msg = "Hello World"
            self.write(msg)

class ServerApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler)
#             (r"/remove", RemoveDCActionHandler)
                   ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, settings)

def create_server():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(ServerApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

def stop_server():
    tornado.ioloop.IOLoop.instance().stop()

if __name__ == '__main__':
    create_server()
#     stop_server()