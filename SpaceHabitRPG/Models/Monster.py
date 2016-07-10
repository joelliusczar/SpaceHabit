from MonsterDefinitions import allMonsters
from MonsterDefinitions import MonsterDefinitions
from StoryModels import StoryModels
from AllDBFields import MonsterFields
import DatabaseLayer



  #I'm making a decision that defense will not be a field

class Monster(StoryModels):
  """
    This is a wrapper for the monster data from the database. This is different
    from the other models in that monster is used as a part of the hero model.
    Unlike Zone, I only care about the current monster being fought. I don't
    care about the previous and I don't care about the potential next.
    Consequently, I'm not going to bother saving Monster in its own collection.

  """

  def save_changes(self,heroId):
    """
      args:
        heroId:
          this needs to be an pymongo objectId. It is used as an owner 
          relationship to a hero model
         
    """
    if self._changes:
        ownerCollection.update_one({self.get_dbFields().PK_KEY:heroId},{'$set':self._changes})
        self._changes = {}


  @property
  def name(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_name()



  @property
  def nowHp(self):
    return self.dict[MonsterFields.NOW_HP]

  @nowHp.setter
  def nowHp(self,value):
    self.dict[MonsterFields.NOW_HP] = value
    self._changes[MonsterFields.NOW_HP] = value

  @property
  def maxHp(self):
    return self.dict[MonsterFields.MAX_HP]

  @maxHp.setter
  def maxHp(self,value):
    self.dict[MonsterFields.MAX_HP] = value
    self._changes[MonsterFields.MAX_HP] = value

  @property
  def lvl(self):
    return self.dict[MonsterFields.LVL]

  @lvl.setter
  def lvl(self,value):
    self.dict[MonsterFields.LVL] = value
    self._changes[MonsterFields.LVL] = value

  @property
  def description(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_description()


  @property
  def baseXpReward(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_baseXpReward()

  @property
  def treasureDropRate(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_dropRate()


  @property
  def treasureDrops(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_treasureDrops()

  @property
  def definitionKey(self):
    return self.dict[MonsterFields.DEFINITION_KEY]

  @definitionKey.setter
  def definitionKey(self,value):
    self.dict[MonsterFields.DEFINITION_KEY] = value
    self._changes[MonsterFields.DEFINITION_KEY] = value

  @property
  def zoneKey(self):
    return self.dict[MonsterFields.ZONE_KEY]

  @zoneKey.setter
  def zoneKey(self,value):
    self.dict[MonsterFields.DEFINITION_KEY] = value
    self._changes[MonsterFields.DEFINITION_KEY] = value

  @classmethod
  def get_random_monster_definitionKey(cls,zoneKey):
    """
      selects a random dictionary key to be used with ZoneDefinitions

      args:
        zoneKey:
          this should be a string. Specically, it is a key to the allMonsters
          dictionary

        returns:
          a string which is a dict key
    """
    from AllDBFields import ZoneDefinitionFields
    import random

    monsterList = list(allMonsters[zoneKey].keys())
    monsterList.extend(list(allMonsters[ZoneDefinitionFields.ALL].keys()))
    return random.choice(monsterList)

  @classmethod
  def construct_new_monster(cls,zoneKey,zoneLvl):

    """
      generates a zone with unique name and randomlvl

      args:
        zoneKey:
          this should be a string. Specically, it is a key to the allMonsters
          dictionary
        zoneLvl:
          this should be a positive integer greater than 1
        
      returns:
        a model of type Monster
    """
    import GeneralUtilities as gu

    selectedMonsterKey = Monster.get_random_monster_definitionKey(zoneKey)
    monster = Monster(selectedMonsterKey)
    monster.lvl = gu.calculate_lvl(zoneLvl,5)
    return monster

  def get_model_info(self):
    info = {}