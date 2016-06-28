from HabitBaseModel import HabitBaseModel
from datetime import datetime
from datetime import timezone
from Daily import Daily
from Hero import Hero
import DatabaseLayer
import uuid


class AccountFields:
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
  collection = DatabaseLayer.get_table(Account.COLLECTION_NAME)
  id = collection.insert_one(account).inserted_id
  return id

#def get_account_by_userID(userID):
#  dbResults = DatabaseLayer.get_sorted_stuff_by_search(

class Account(HabitBaseModel):
  """
    This is a wrapper for the account data from the database
  """
  COLLECTION_NAME = 'accounts'

  def __init__(self,dict=None,id = None):
    """
      args:
        dict:
          loads the properties of the model from the dict.
        id:
          uses the id to load this model from the database.
          If both a dict and id are supplied, the dict is used and the id is 
          ignored. 
          If nether are supplied then the model is empty
    """
    super().__init__(dict =dict,id =id)

  @property
  def id(self):
    return self._dict[Account.ID_KEY]

      
