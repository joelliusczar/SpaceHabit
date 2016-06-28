from HabitBaseModel import HabitBaseModel
from Zone import Zone
import DatabaseLayer
import uuid



class HeroFields:
  ACCOUNT_ID = 'accountId'
  SHIP_NAME = 'shipName'
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
  HAS_LEFT_PORT = 'hasLeftPort'
  ZONE = 'zone'



def create_new_hero(accountId = None,shipName = ""):
  hero = {
    HeroFields.ACCOUNT_ID: accountId,
    HeroFields.SHIP_NAME: shipName,
    HeroFields.LVL:1,
    HeroFields.GOLD:0,
    HeroFields.MAX_HP: 100,
    HeroFields.NOW_HP: 100,
    HeroFields.MAX_XP: 50,
    HeroFields.NOW_XP: 0,
    HeroFields.ATTACK_LVL: 1,
    HeroFields.DEFENSE_LVL: 1,
    HeroFields.PUBLIC_KEY: uuid.uuid4().hex

  }
  collection = DatabaseLayer.get_table(Hero.COLLECTION_NAME)
  id = collection.insert_one(hero).inserted_id
  return id

class Hero(HabitBaseModel):
  """
    This is a wrapper for the hero data from the database
  """

  COLLECTION_NAME = 'heros'
  _zone = None

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
    return self._dict[Hero.ID_KEY]


  @property
  def lvl(self):
    return self._dict[HeroFields.LVL]

  @lvl.setter
  def lvl(self,value):
    self._dict[HeroFields.LVL] = value
    self._changes[HeroFields.LVL] = value

  @property
  def maxHp(self):
    return self._dict[HeroFields.MAX_HP]

  @maxHp.setter
  def maxHp(self,value):
    self._dict[HeroFields.MAX_HP] = value
    self._changes[HeroFields.MAX_HP] = value

  @property
  def nowHp(self):
    return self._dict[HeroFields.NOW_HP]

  @nowHp.setter
  def nowHp(self,value):
    self._dict[HeroFields.NOW_HP] = value
    self._changes[HeroFields.NOW_HP] = value

  @property
  def maxXp(self):
    return self._dict[HeroFields.MAX_XP]

  @maxXp.setter
  def maxXp(self,value):
    self._dict[HeroFields.MAX_XP] = value
    self._changes[HeroFields.MAX_XP] = value

  @property
  def nowXp(self):
    return self._dict[HeroFields.NOW_XP]

  @nowXp.setter
  def nowXp(self,value):
    self._dict[HeroFields.NOW_XP] = value
    self._changes[HeroFields.NOW_XP] = value

  @property
  def gold(self):
    return self._dict[HeroFields.GOLD]

  @gold.setter
  def gold(self,value):
    self._dict[HeroFields.GOLD] = value
    self._changes[HeroFields.GOLD] = value

  @property
  def attackLvl(self):
    return self._dict[HeroFields.ATTACK_LVL]

  @attackLvl.setter
  def attackLvl(self,value):
    self._dict[HeroFields.ATTACK_LVL] = value
    self._changes[HeroFields.ATTACK_LVL] = value

  @property
  def defenseLvl(self):
    return self._dict[HeroFields.DEFENSE_LVL]

  @defenseLvl.setter
  def defenseLvl(self,value):
    self._dict[HeroFields.DEFENSE_LVL] = value
    self._changes[HeroFields.DEFENSE_LVL] = value

  @property
  def zoneVisitCounts(self):
    return self._dict[HeroFields.ZONE_VISIT_COUNTS]

  @zoneVisitCounts.setter
  def zoneVisitCounts(self,value):
    self._dict[HeroFields.ZONE_VISIT_COUNTS] = value
    self._changes[HeroFields.ZONE_VISIT_COUNTS] = value

  
  @property
  def zone(self):
    if not self._zone:
      self._zone = Zone(self.id,self._dict[HeroFields.ZONE])
    return self._zone
    


  @property
  def hasLeftPort(self):
    if HeroFields.HAS_LEFT_PORT in self._dict:
      return self._dict[HeroFields.HAS_LEFT_PORT]
    else:
      return False

  @hasLeftPort.setter
  def hasLeftPort(self,value):
    self._dict[HeroFields.HAS_LEFT_PORT] = value
    self._changes[HeroFields.HAS_LEFT_PORT] = value