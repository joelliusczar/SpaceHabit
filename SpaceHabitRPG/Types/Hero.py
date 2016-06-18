import DatabaseLayer

COLLECTION_NAME = 'heros'
ACCOUNT_ID = 'accountId'
SHIP_NAME = 'shipName'
ID_KEY = '_id'
LVL = 'lvl'
GOLD = 'gold'
MAX_HP = 'maxHp'
NOW_HP = 'nowHp'
MAX_XP = 'maxXp'
NOW_XP = 'nowXp'
ATTACK_LVL = 'attackLvl'
DEFENSE_LVL = 'defenseLvl'
ZONE_VISIT_COUNTS = 'zoneVisitCounts'
PUBLIC_KEY = 'PublicKey'


def create_new_hero(accountId = None,shipName = ""):
    hero = {
        ACCOUNT_ID: accountId,
        SHIP_NAME: shipName,
        LVL:1,
        GOLD:0,
        MAX_HP: 100,
        NOW_HP: 100,
        MAX_XP: 50,
        NOW_XP: 0,
        ATTACK_LVL: 1,
        DEFENSE_LVL: 1,           
    }
    collection = DatabaseLayer.get_table(COLLECTION_NAME)
    id = collection.insert_one(hero).inserted_id
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
            self._dict = DatabaseLayer.get_thing_by_id(id,COLLECTION_NAME)
            return

    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,COLLECTION_NAME,self._changes)
        self._changes = {}

    @property
    def id(self):
        return self._dict[ID_KEY]


    @property
    def lvl(self):
        return self._dict[LVL]

    @lvl.setter
    def lvl(self,value):
        self._dict[LVL] = value
        self._changes[LVL] = value

    @property
    def maxHp(self):
        return self._dict[MAX_HP]

    @maxHp.setter
    def maxHp(self,value):
        self._dict[MAX_HP] = value
        self._changes[MAX_HP] = value

    @property
    def nowHp(self):
        return self._dict[NOW_HP]

    @nowHp.setter
    def nowHp(self,value):
        self._dict[NOW_HP] = value
        self._changes[NOW_HP] = value

    @property
    def maxXp(self):
        return self._dict[MAX_XP]

    @maxXp.setter
    def maxXp(self,value):
        self._dict[MAX_XP] = value
        self._changes[MAX_XP] = value

    @property
    def nowXp(self):
        return self._dict[NOW_XP]

    @nowXp.setter
    def nowXp(self,value):
        self._dict[NOW_XP] = value
        self._changes[NOW_XP] = value

    @property
    def gold(self):
        return self._dict[GOLD]

    @gold.setter
    def gold(self,value):
        self._dict[GOLD] = value
        self._changes[GOLD] = value

    @property
    def attackLvl(self):
        return self._dict[ATTACK_LVL]

    @attackLvl.setter
    def attackLvl(self,value):
        self._dict[ATTACK_LVL] = value
        self._changes[ATTACK_LVL] = value

    @property
    def defenseLvl(self):
        return self._dict[DEFENSE_LVL]

    @defenseLvl.setter
    def defenseLvl(self,value):
        self._dict[DEFENSE_LVL] = value
        self._changes[DEFENSE_LVL] = value

    @property
    def zoneVisitCounts(self):
        return self._dict[ZONE_VISIT_COUNTS]

    @zoneVisitCounts.setter
    def zoneVisitCounts(self,value):
        self._dict[ZONE_VISIT_COUNTS] = value
        self._changes[ZONE_VISIT_COUNTS] = value