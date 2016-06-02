import DatabaseLayer

COLLECTION_NAME = 'monsters'
ID_KEY = '_id'
NAME = 'name'
NOW_HP = 'nowHP'
MAX_HP = 'maxHp'
LVL = 'lvl'
DESCRIPTION = 'description'
BASE_XP_REWARD = 'baseXpReward'
TRASURE_DROP_RATE = 'treasureDropRate'
TRASURE_DROPS = 'treasureDrops'


class Monster(object):
    """description of class"""
    def __init__(self,dict=None,id = None):
        """Priority is given to dictionary object over id """
        self._changes = {}
        if dict:
            self._dict = dict
            return
        if id:
            self._dict = DatabaseLayer.get_thing_by_id(id,COLLECTION_NAME)
            return
        raise ValueError("Either a reference to a dictionary or an id is required")


    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,COLLECTION_NAME,self._changes)
        self._changes = {}

    @property
    def id(self):
        return self._dict[ID_KEY]

    @property
    def name(self):
        return self._dict[NAME]

    @name.setter
    def name(self,value):
        self._dict[NAME] = value
        self._changes[NAME] = value

    @property
    def nowHp(self):
        return self._dict[NOW_HP]

    @nowHp.setter
    def nowHp(self,value):
        self._dict[NOW_HP] = value
        self._changes[NOW_HP] = value

    @property
    def maxHp(self):
        return self._dict[MAX_HP]

    @maxHp.setter
    def maxHp(self,value):
        self._dict[MAX_HP] = value
        self._changes[MAX_HP] = value

    @property
    def lvl(self):
        return self._dict[LVL]

    @lvl.setter
    def lvl(self,value):
        self._dict[LVL] = value
        self._changes[LVL] = value

    @property
    def description(self):
        return self._dict[DESCRIPTION]

    @description.setter
    def description(self,value):
        self._dict[DESCRIPTION] = value
        self._changes[DESCRIPTION] = value

    @property
    def baseXpReward(self):
        return self._dict[BASE_XP_REWARD]

    @baseXpReward.setter
    def baseXpReward(self,value):
        self._dict[BASE_XP_REWARD] = value
        self._changes[BASE_XP_REWARD] = value

    @property
    def treasureDropRate(self):
        return self._dict[TRASURE_DROP_RATE]

    @treasureDropRate.setter
    def treasureDropRate(self,value):
        self._dict[TRASURE_DROP_RATE] = value
        self._changes[TRASURE_DROP_RATE] = value

    @property
    def treasureDrops(self):
        return self._dict[TRASURE_DROPS]

    @treasureDrops.setter
    def treasureDrops(self,value):
        self._dict[TRASURE_DROPS] = value
        self._changes[TRASURE_DROPS] = value