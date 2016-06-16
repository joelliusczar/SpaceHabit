import cherrypy
import os
import AuthenticationLayer
import EverywhereConstants
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
            cherrypy.session[EverywhereConstants.SESSION_KEY] = login
        return validationResults

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=['POST'])
    def save_new_user(self,email1,email2,pw1,pw2,shipName):
        resultDict = {'errors':[],'success':False}
        validationFlags = AuthenticationLayer.check_all_new_user_validations(email1,email2,pw1,pw2,shipName)
        if len(validationFlags) > 0:
            resultDict['error'] = validationFlags
            return resultDict
        newUserTuple = AuthenticationLayer.insert_new_user(email1,pw1,shipName)
        cherrypy.session[EverywhereConstants.SESSION_KEY] = email1
        cherrypy.session[EverywhereConstants.USER_ID_KEY] = newUserTuple[0]
        cherrypy.session[EverywhereConstants.ACCOUNT_ID_KEY] = newUserTuple[1]
        cherrypy.session[EverywhereConstants.HERO_ID_KEY] = newUserTuple[2]
        resultDict['success'] = True
        return resultDict





