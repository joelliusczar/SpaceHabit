import cherrypy
from Hero import Hero
from bson.objectid import ObjectId
import RpgTypeHelper


class HeroController(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self):
        hero = Hero(id = ObjectId("57466ad3c993956eb6d39004"))
        return RpgTypeHelper.convert_rpgtype_to_json(hero)

    def POST(self):
        pass

    def PUT(self):
        pass

    def DELETE(self):
        pass



