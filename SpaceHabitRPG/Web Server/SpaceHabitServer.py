import cherrypy
from HeroController import HeroController
import os

class SpaceHabitHome(object):
    @cherrypy.expose
    def index(self):
        return open("HabitFrontend/login.html",encoding="utf-8")



if __name__ == "__main__":
    subdir = ""
    static = ""
    if os.name == "nt":
        subdir = "\\HabitFrontend"
    else:
        subdir = "/HabitFrontend"
    conf = {
        '/':{
            'tools.staticdir.root': (os.path.abspath(os.getcwd()) + subdir)
            },
        '/hero':{
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            },
        '/static':{
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "public"
            }
        }
    webapp = SpaceHabitHome()
    webapp.hero = HeroController()
    cherrypy.quickstart(webapp,"/",conf)

