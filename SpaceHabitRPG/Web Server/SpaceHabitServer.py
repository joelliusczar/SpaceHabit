from LoginController import LoginController
from ValidationController import ValidationController
from MainController import MainController
import cherrypy
import os
import AuthenticationLayer






class SpaceHabitHome(object):

    def __init__(self):
        self.testModeEnabled = False

    @cherrypy.expose
    @cherrypy.tools.redirect_unauthenticated()
    def index(self):
        return open("HabitFrontend/index.html",encoding="utf-8")

    @cherrypy.expose
    def playground(self):
        import ConfigLayer
        if ConfigLayer.get_is_debug():
            return open("HabitFrontend/TestPlayground.html",encoding="utf-8")

import threading

class HabitServer(threading.Thread):
    def __init__(self,port=8080,host="127.0.0.1"):
        self.port = port
        self.host = host
        subdir = ""
        static = ""
        if os.name == "nt":
            subdir = "\\HabitFrontend"
        else:
            subdir = "/HabitFrontend"
        self.conf = {
            '/':{
                'tools.sessions.on': True,
                'tools.staticdir.root': (os.path.abspath(os.getcwd()) + subdir)
                },
            '/login':{
                },
            '/static':{
                'tools.staticdir.on': True,
                'tools.staticdir.dir': "public"
                }
            }
        threading.Thread.__init__(self)
        self.sync = threading.Condition()
        self.daemon = True

    def run(self):
        with self.sync:
            cherrypy.server.socket_port = self.port
            cherrypy.server.socket_host = self.host
            webapp = SpaceHabitHome()
            webapp.login = LoginController()
            webapp.login.validate = ValidationController()
            webapp.main = MainController()
            cherrypy.tree.mount(webapp,"/",self.conf)
            cherrypy.engine.start()
        cherrypy.engine.block()

    def stop(self):
        with self.sync:
            cherrypy.engine.exit()
            cherrypy.engine.stop()


def server_starter():
    server = HabitServer()
    server.start()


if __name__ == "__main__":

    server_starter()

