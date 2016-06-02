import cherrypy
import os

def superBeginningSignal():
    print("superBeginningSignal")

def alsoSuperBeginningSignal():
    print("alsoSuperBeginningSignal")

def sortaBeginningSIgnal():
    print("sortaBeginningSIgnal")

cherrypy.tools.firstOne = cherrypy.Tool('before_handler', superBeginningSignal)
cherrypy.tools.maybe = cherrypy.Tool('before_handler', alsoSuperBeginningSignal)
cherrypy.tools.sorta = cherrypy.Tool('before_finalize', sortaBeginningSIgnal)

class TestCherryPyThres(object):

    @cherrypy.expose
    def hello(self):
        s = "hello, you goddamn motherfucker"
        print(s)
        return s

    @cherrypy.expose
    def crackhead(self):
        s = "You crackhead!"
        print(s)
        return s

class TestCherryPyDos(object):

    @cherrypy.expose
    @cherrypy.tools.sorta()
    def index(self):
        print("index")
        return open('testweb/WebPage2.html',encoding='utf-8')

    @cherrypy.expose
    @cherrypy.tools.maybe()
    def generator(self):
        print("in generator")
        return "Hello, motherfucker"

    @cherrypy.expose
    def mypost(self):
        print("in posted")
        return "posted!"

    @cherrypy.expose
    def putt_putt(self,another_string):
        print("in putt putt")
        print(another_string)

    @cherrypy.expose
    def oops_deleted(self):
        print("in deleted")
        print("deletatron!")

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'tools.firstOne.on': True
        },
        '/yodal':{
            },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = TestCherryPyDos()
    webapp.yodal = TestCherryPyThres()
    cherrypy.quickstart(webapp, '/', conf)

