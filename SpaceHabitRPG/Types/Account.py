import DatabaseLayer
from Daily import Daily
from Hero import Hero

COLLECTION_NAME = 'users'
ID_KEY = '_id'
USER_ID = 'heroId'
REMINDER_TIME = 'reminderTime'
DAY_START = 'dayStart'
DEATH_GOLD_PENALTY = 'deathGoldPenalty'
HERO_LVL_PENALTY = 'heroLvlPenalty'
ZONE_LVL_PENALTY = 'zoneLvlPenalty'
ENEMY_HEALED_ON_ATTACK = 'enemyHealedOnAttack'
SELF_HEALED_ON_ATTACK = 'selfHealedOnAttack'
PERMA_DEATH = 'permaDeath'
STORY_MODE_IS_ON = 'storyModeIsOn'
PUBLIC_ACCOUNT = 'publicAccount'
PUBLIC_KEY = 'PublicKey'



def create_new_account(userId=None):
    account = {
        USER_ID: userId,
        REMINDER_TIME: -1,
        DAY_START:12,
        DEATH_GOLD_PENALTY: .25,
        HERO_LVL_PENALTY:0,
        ZONE_LVL_PENALTY:"LVLRESTART",
        ENEMY_HEALED_ON_ATTACK: False,
        SELF_HEALED_ON_ATTACK: False,
        PERMA_DEATH: False}

    id = DatabaseLayer.insert_thing(account,COLLECTION_NAME)
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
            self._dict = DatabaseLayer.get_thing_by_id(id,COLLECTION_NAME)
            return
        raise ValueError("Either a reference to a dictionary or an id is required")

    def save_changes(self):
        DatabaseLayer.update_thing_by_id(self.id,COLLECTION_NAME,self.changes)
        self.changes = {}

    @property
    def id(self):
        return self._dict[ID_KEY]


            
