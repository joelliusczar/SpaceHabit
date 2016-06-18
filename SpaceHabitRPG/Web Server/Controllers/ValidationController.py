import cherrypy
import AuthenticationLayer

class ValidationController(object):
    """description of class"""

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    @cherrypy.tools.json_out()
    def email(self,email):
        return AuthenticationLayer.validate_email(email)
