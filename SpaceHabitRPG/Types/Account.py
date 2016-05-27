import DatabaseLayer
from Daily import Daily
from Hero import Hero

def create_new_account():
    account = {
        'reminderTime': -1,
        'dayStart':12,
        'deathGoldPenalty': .25,
        'heroLvlPenalty':0,
        'zoneLvlPenalty':"LVLRESTART",
        'enemyHealedOnAttack': False,
        'selfHealedOnAttack': False,
        'permaDeath': False}

    id = DatabaseLayer.insert_thing(account,"accounts")
    return id

class Account(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        self._dailies = []
        self._habits = []
        self._todos = []
        self._irlGoods = []
        self._hero = None
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,"accounts")
            return
        raise ValueError("Either a reference to a dictionary or an id is required")

    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,"accounts",self.changes)
        self.changes = {}

    @property
    def id(self):
        return self._dict['_id']

    @property
    def hero(self):
        if not self._hero:
            self._hero = Hero(id = self._dict['heroId'])
        return self._hero


    def assign_heroId(self,id):
        self._dict['heroId'] = id
        self._changes['heroId'] = id
            
