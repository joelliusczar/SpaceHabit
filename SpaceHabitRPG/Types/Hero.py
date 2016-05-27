import DatabaseLayer


def create_new_hero(shipName):
    hero = {
        'shipName':shipName,
        'lvl':1,
        'gold':0,
        'maxHp': 100,
        'nowHp': 100,
        'maxXp': 50,
        'nowXp': 0,
        'attackLvl': 1,
        'defenseLvl': 1,           
    }
    id  = DatabaseLayer.insert_thing(hero,"heros")
    return id

class Hero(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,"heros")
            return

    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,"heros",self._changes)
        self._changes = {}



    @property
    def id(self):
        return self._dict['_id']

    @property
    def name(self):
        return self._dict['name']

    @name.setter
    def name(self,value):
        self._dict['name'] = value
        self._changes['name'] = value

    @property
    def lvl(self):
        return self._dict['lvl']

    @lvl.setter
    def lvl(self,value):
        self._dict['lvl'] = value
        self._changes['lvl'] = value

    @property
    def maxHp(self):
        return self._dict['maxHp']

    @maxHp.setter
    def maxHp(self,value):
        self._dict['maxHp'] = value
        self._changes['maxHp'] = value

    @property
    def nowHp(self):
        return self._dict['nowHp']

    @nowHp.setter
    def nowHp(self,value):
        self._dict['nowHp'] = value
        self._changes['nowHp'] = value

    @property
    def maxXp(self):
        return self._dict['maxXp']

    @maxXp.setter
    def maxXp(self,value):
        self._dict['maxXp'] = value
        self._changes['maxXp'] = value

    @property
    def nowXp(self):
        return self._dict['nowXp']

    @nowXp.setter
    def nowXp(self,value):
        self._dict['nowXp'] = value
        self._changes['nowXp'] = value

    @property
    def gold(self):
        return self._dict['gold']

    @gold.setter
    def gold(self,value):
        self._dict['gold'] = value
        self._changes['gold'] = value

    @property
    def attackLvl(self):
        return self._dict['attackLvl']

    @attackLvl.setter
    def attackLvl(self,value):
        self._dict['attackLvl'] = value
        self._changes['attackLvl'] = value

    @property
    def defenseLvl(self):
        return self._dict['defenseLvl']

    @defenseLvl.setter
    def defenseLvl(self,value):
        self._dict['defenseLvl'] = value
        self._changes['defenseLvl'] = value

    @property
    def zoneVisitCounts(self):
        return self._dict['zoneVisitCounts']

    @zoneVisitCounts.setter
    def zoneVisitCounts(self,value):
        self._dict['zoneVisitCounts'] = value
        self._changes['zoneVisitCounts'] = value