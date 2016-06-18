from datetime import datetime
from datetime import timezone
from Daily import Daily
from Hero import Hero
import DatabaseLayer
import uuid


class AccountFields:
  COLLECTION_NAME = 'accounts'
  ID_KEY = '_id'
  USER_ID = 'userId'
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
  CREATE_DATE = 'creationDate'



def create_new_account(userId=None):
  account = {
    AccountFields.USER_ID: userId,
    AccountFields.REMINDER_TIME: -1,
    AccountFields.DAY_START:0,
    AccountFields.DEATH_GOLD_PENALTY: .25,
    AccountFields.HERO_LVL_PENALTY: 0,
    AccountFields.ZONE_LVL_PENALTY: "LVLRESTART",
    AccountFields.ENEMY_HEALED_ON_ATTACK: False,
    AccountFields.SELF_HEALED_ON_ATTACK: False,
    AccountFields.PERMA_DEATH: False,
    AccountFields.PUBLIC_ACCOUNT: False,
    AccountFields.PUBLIC_KEY: uuid.uuid4().hex,
    AccountFields.CREATE_DATE: datetime.now(timezone.utc)
    }
  collection = DatabaseLayer.get_table(AccountFields.COLLECTION_NAME)
  id = collection.insert_one(account).inserted_id
  return id

#def get_account_by_userID(userID):
#  dbResults = DatabaseLayer.get_sorted_stuff_by_search(

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
    collection = DatabaseLayer.get_table(AccountFields.COLLECTION_NAME)
    collection.update_one({AccountFields.ID_KEY:self.id},self._changes)
    self.changes = {}

  @property
  def id(self):
    return self._dict[AccountFields.ID_KEY]


      
