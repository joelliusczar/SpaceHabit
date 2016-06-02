import cherrypy
import os
import AuthenticationLayer
import EverywhereConstants
import json


class LoginController(object):
    """description of class"""

    @cherrypy.expose
    def index(self):
        return open("HabitFrontend/login.html",encoding="utf-8")

    @cherrypy.expose
    def login(self, login,pw):
        validationResults = AuthenticationLayer.authenticate_user(login,pw)
        if validationResults[0]:
            cherrypy.session[EverywhereConstants.SESSION_KEY] = login
            return ""
        else:
            return validationResults[1]

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.allow(methods=['POST'])
    def save_new_user(self,email1,email2,pw1,pw2,shipName):
        validationResults = AuthenticationLayer.validate_everything_new_user(email1,email2,pw1,pw2)
        if len(validationResults[0]) > 0 or len(validationResults[1]) > 0:
            return json.dumps(validationResults)
        newUserTuple = AuthenticationLayer.insert_new_user(email1,pw1,shipName)
        cherrypy.session[EverywhereConstants.SESSION_KEY] = email1
        cherrypy.session[EverywhereConstants.USER_ID_KEY] = newUserTuple[0]
        cherrypy.session[EverywhereConstants.ACCOUNT_ID_KEY] = newUserTuple[1]
        cherrypy.session[EverywhereConstants.HERO_ID_KEY] = newUserTuple[2]
        return ""





