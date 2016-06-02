import os, os.path
import random
import string

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('testweb/WebPage1.html',encoding='utf-8')

class TestCherryPyThres(object):

    @cherrypy.expose
    def hello(self):
        s = "hello, you goddamn motherfucker"
        print(s)
        return s

    @cherrypy.expose
    def crackhead(self):
        s = "You crackhead!"
        print(s)
        return s

class StringGeneratorWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        print("Hello")
        return "Yo!"

    def POST(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/yodal':{
            },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    }
    webapp = StringGenerator()
    webapp.generator = StringGeneratorWebService()
    webapp.yodal = TestCherryPyThres()
    cherrypy.quickstart(webapp, '/', conf)