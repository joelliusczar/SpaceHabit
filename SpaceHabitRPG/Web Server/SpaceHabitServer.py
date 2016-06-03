import cherrypy
from HeroController import HeroController
from LoginController import LoginController
from ValidationController import ValidationController
import EverywhereConstants
import os




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

def server_starter():
    subdir = ""
    static = ""
    if os.name == "nt":
        subdir = "\\HabitFrontend"
    else:
        subdir = "/HabitFrontend"
    conf = {
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
    webapp = SpaceHabitHome()
    webapp.login = LoginController()
    webapp.login.validate = ValidationController()
    webapp.hero = HeroController()
    cherrypy.quickstart(webapp,"/",conf)


if __name__ == "__main__":

    
    server_starter()

