import cherrypy
from Daily import Daily

class AllDailiesController(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        print("got here")
        return "Hello"


    def POST(self):
        pass

    def PUT(self):
        pass

    def DELETE(self):
        pass

