import cherrypy
import AuthentificationLayer

class AuthenticationController(object):
    """description of class"""

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def login(self,username=None,pw=None):
        pass
