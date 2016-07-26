from AllDBFields import BaseFields
from Hero import Hero
from Account import Account
import StartUpRoutine
import cherrypy
import AuthenticationLayer
import GeneralUtilities as gu

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
    heroPk = cherrypy.session.get(BaseFields.HERO_PK_KEY)
    accountPk = cherrypy.session.get(BaseFields.ACCOUNT_PK_KEY)
    utcElapsedTime = gu.adjust_timestamp_from_js_to_python(utcElapsedTime)
    messages = StartUpRoutine.\
      check_in_and_get_notices(heroPk,accountPk,utcElapsedTime,utcOffset)
    return messages

  @cherrypy.expose
  @cherrypy.tools.redirect_unauthenticated()
  def disable_popups(self):
    accountPk = cherrypy.session.get(BaseFields.ACCOUNT_PK_KEY)
    account = Account.create_model_from_pk(accountPk)
    account.preventPopups = True
    account.save_changes()