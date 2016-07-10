from AllDBFields import BaseFields
import cherrypy
import os
import AuthenticationLayer
import json

class LoginController(object):
  """description of class"""

  @cherrypy.expose
  @cherrypy.tools.redirect_authenticated()
  def index(self):
    return open("HabitFrontend/login.html",encoding="utf-8")


  @cherrypy.expose
  @cherrypy.tools.json_out()
  @cherrypy.tools.allow(methods=['POST'])
  def login(self,login,pw):
    validationResults = AuthenticationLayer.authenticate_user(login,pw)
    if validationResults['success']:

      userId = AuthenticationLayer.get_loginPk_by_login(login)
      accountId = AuthenticationLayer.get_accountPk_by_loginPk(userId)
      heroId = AuthenticationLayer.get_heroPk_by_accountPk(accountId)

      cherrypy.session[BaseFields.SESSION_KEY] = login
      cherrypy.session[BaseFields.LOGIN_PK_KEY] = userId
      cherrypy.session[BaseFields.ACCOUNT_PK_KEY] = accountId
      cherrypy.session[BaseFields.HERO_PK_KEY] = heroId
    return validationResults
  

  @cherrypy.expose
  @cherrypy.tools.json_out()
  @cherrypy.tools.allow(methods=['POST'])
  def save_new_user(self,email1,email2,pw1,pw2,shipName):
    resultDict = {'errors':[],'success':False}
    validationFlags = AuthenticationLayer.check_all_validations_for_new_login(email1,email2,pw1,pw2,shipName)
    if len(validationFlags) > 0:
      resultDict['error'] = validationFlags
      return resultDict
    newUserTuple = AuthenticationLayer.insert_new_user(email1,pw1,shipName)
    cherrypy.session[BaseFields.SESSION_KEY] = email1
    cherrypy.session[BaseFields.LOGIN_PK_KEY] = newUserTuple[0]
    cherrypy.session[BaseFields.ACCOUNT_PK_KEY] = newUserTuple[1]
    cherrypy.session[BaseFields.HERO_PK_KEY] = newUserTuple[2]
    resultDict['success'] = True
    return resultDict










