import cherrypy
import UserDBLayer
import AuthenticationLayer

class ValidationController(object):
    """description of class"""

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def email(self,email):
        return AuthenticationLayer.validate_email(email)
