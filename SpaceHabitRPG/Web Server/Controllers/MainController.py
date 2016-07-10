from AllDBFields import BaseFields
from Hero import Hero
from Account import Account
import StartUpRoutine
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
  @cherrypy.tools.redirect_unauthenticated()
  def checkin(self,utcElapsedTime,utcOffset):
    """
      this is called by the main page when the site loads.
    """
    heroId = cherrypy.session.get(BaseFields.HERO_PK_KEY)
    accountId = cherrypy.session.get(BaseFields.ACCOUNT_PK_KEY)
    messages = StartUpRoutine.\
      check_in_and_get_notices(heroId,accountId,utcElapsedTime,utcOffset)
    return messages