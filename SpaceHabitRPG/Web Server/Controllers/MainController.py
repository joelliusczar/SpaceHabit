import cherrypy
import AuthenticationLayer

class MainController(object):
  """
    this will be the mvc controller to handle ajax requests on the main page
    for global type stuff, e.g. start up, settings. Stuff like dailies and 
    habits will go in their own controller.
  """

  @cherrypy.expose
  @cherrypy.tools.json_out()
  @cherrypy.tools.allow(methods=['POST'])
  @cherrypy.tools.redirect_unauthenticated()
  def check_in(self):
    """
      this is called by the main page when the site loads.
    """
