import DatabaseLayer

class Monster(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,"monsters")
            return
        raise ValueError("Either a reference to a dictionary or an id is required")


    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,"monsters",self._changes)
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
    def nowHp(self):
        return self._dict['nowHp']

    @nowHp.setter
    def nowHp(self,value):
        self._dict['nowHp'] = value
        self._changes['nowHp'] = value

    @property
    def maxHp(self):
        return self._dict['maxHp']

    @maxHp.setter
    def maxHp(self,value):
        self._dict['maxHp'] = value
        self._changes['maxHp'] = value

    @property
    def lvl(self):
        return self._dict['lvl']

    @lvl.setter
    def lvl(self,value):
        self._dict['lvl'] = value
        self._changes['lvl'] = value

    @property
    def description(self):
        return self._dict['description']

    @description.setter
    def description(self,value):
        self._dict['description'] = value
        self._changes['description'] = value

    @property
    def baseXpReward(self):
        return self._dict['baseXpReward']

    @baseXpReward.setter
    def baseXpReward(self,value):
        self._dict['baseXpReward'] = value
        self._changes['baseXpReward'] = value

    @property
    def treasureDropRate(self):
        return self._dict['treasureDropRate']

    @treasureDropRate.setter
    def treasureDropRate(self,value):
        self._dict['treasureDropRate'] = value
        self._changes['treasureDropRate'] = value

    @property
    def treasureDrops(self):
        return self._dict['treasureDrops']

    @treasureDrops.setter
    def treasureDrops(self,value):
        self._dict['treasureDrops'] = value
        self._changes['treasureDrops'] = value