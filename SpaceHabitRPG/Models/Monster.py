from MonsterDefinitions import allMonsters
from MonsterDefinitions import MonsterDefinitions
from StoryModels import StoryModels
from AllDBFields import MonsterDbFields
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

  @classmethod
  def get_dbFields(cls):
    return MonsterDbFields

  def get_name(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_name()


  @property
  def maxHp(self):
    return self.dict[MonsterDbFields.MAX_HP]


  @maxHp.setter
  def maxHp(self,value):
    self.set_common_story_property(MonsterDbFields.MAX_HP,value)


  @property
  def nowHp(self):
    return self.dict[MonsterDbFields.NOW_HP]


  @nowHp.setter
  def nowHp(self,value):
    self.set_common_story_property(MonsterDbFields.NOW_HP,value)


  @property
  def lvl(self):
    return self.dict[MonsterDbFields.LVL]

  @lvl.setter
  def lvl(self,value):
    self.set_common_story_property(MonsterDbFields.LVL,value)


  def get_description(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_description()


  def get_baseXpReward(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_baseXpReward()

  def get_treasureDropRate(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_dropRate()

  def get_gold(self):
    '''
      We only want to return 1 because constantly raising this like in normal
      RPG's will skewer the motivational rewards aspect.
      But I'm keeping it as a method in case I change my mind
    '''
    return 1


  def get_treasureDrops(self):
    if not self._definition:
      self._definition = MonsterDefinitions(self.definitionKey)
    return self._definition.get_treasureDrops()

  @property
  def definitionKey(self):
    return self.dict[MonsterDbFields.DEFINITION_KEY]

  @definitionKey.setter
  def definitionKey(self,value):
    self.dict[MonsterDbFields.DEFINITION_KEY] = value
    self._changes[MonsterDbFields.DEFINITION_KEY] = value


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