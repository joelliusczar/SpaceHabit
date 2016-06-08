import cherrypy
from HeroController import HeroController
from LoginController import LoginController
from ValidationController import ValidationController
import EverywhereConstants
import os


SERVER_PORT = 8080

def check_login_state():
    username = cherrypy.session.get(EverywhereConstants.SESSION_KEY)
    if not username:
        raise cherrypy.HTTPRedirect("/login")

cherrypy.tools.check_login = cherrypy.Tool("before_handler",check_login_state)

class SpaceHabitHome(object):

    def __init__(self):
        self.testModeEnabled = False

    @cherrypy.expose
    @cherrypy.tools.check_login()
    def index(self):
        return open("HabitFrontend/index.html",encoding="utf-8")

    @cherrypy.expose
    def enable_test_mode(self):
        import MockSetUp
        self.testModeEnabled = True
        MockSetUp.set_up_mock_db_connections()

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
            webapp.hero = HeroController()
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

