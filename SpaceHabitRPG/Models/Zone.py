import DatabaseLayer

class ZoneFields:
  ALIAS = 'alias'
  MONSTERS_KILLED = 'monstersKilled'
  MAX_MONSTERS = 'maxMonsters'
  SKILL_LVL = 'skillLvl'
  DESCRIPTION = 'description'
  PREVIOUS_ZONE_REFERENCE = 'previousZoneReference'
  NEXT_ZONE_REFERENCE_LIST = 'nextZoneReferenceList'
  NAME = 'name'
  DEFINITION_KEY = 'definitionKey'



class Zone(object):
  """
    This is a wrapper for the zone data from the database. This is different
    from the other models in that Zone is used as a part of the hero model.

  """

  COLLECTION_NAME = 'heros'
  ID_KEY = '_id'
  _changes = {}

  def __init__(self,heroId,dict):
    """
      args:
        heroId:
          this needs to be an pymongo objectId. It is used as an owner 
          relationship to a hero model
        dict:
          a dict with the info for the zone model
         
    """
    self.heroId = heroId
    self._dict = dict

  def save_changes(self):
    collection = DatabaseLayer.get_table(self.COLLECTION_NAME)
    if self.ID_KEY in self._dict:
      collection.update_one({self.ID_KEY:self.heroId},{'$set':self._changes})


  @property
  def zoneName(self):
    return self._dict[ZoneFields.NAME]

  @zoneName.setter
  def zoneName(self,value):
    self._dict[ZoneFields.NAME] = value
    self._changes[ZoneFields.NAME] = value

  @property
  def monstersKilled(self):
    if self._dict[ZoneFields.MONSTERS_KILLED]:
      return self._dict[ZoneFields.MONSTERS_KILLED]
    else:
      return 0

  @monstersKilled.setter
  def monstersKilled(self,value):
    self._dict[ZoneFields.MONSTERS_KILLED] = value
    self._changes[ZoneFields.MONSTERS_KILLED] = value

  @property
  def maxMonsters(self):
    return self._dict[ZoneFields.MAX_MONSTERS]

  @maxMonsters.setter
  def maxMonsters(self,value):
    self._dict[ZoneFields.MAX_MONSTERS] = value
    self._changes[ZoneFields.MAX_MONSTERS] = value

  @property
  def skillLvl(self):
    return self._dict[ZoneFields.SKILL_LVL]

  @skillLvl.setter
  def skillLvl(self,value):
    self._dict[ZoneFields.SKILL_LVL] = value
    self._changes[ZoneFields.SKILL_LVL] = value

  @property
  def description(self):
    return self._dict[ZoneFields.DESCRIPTION]

  @description.setter
  def description(self,value):
    self._dict[ZoneFields.DESCRIPTION] = value
    self._changes[ZoneFields.DESCRIPTION] = value

  @property
  def previousZoneReference(self):
    return self._dict[ZoneFields.PREVIOUS_ZONE_REFERENCE]

  @previousZoneReference.setter
  def previousZoneReference(self,value):
    self._dict[ZoneFields.PREVIOUS_ZONE_REFERENCE] = value
    self._changes[ZoneFields.PREVIOUS_ZONE_REFERENCE] = value

  @property
  def nextZoneReferenceList(self):
    return self._dict[ZoneFields.NEXT_ZONE_REFERENCE_LIST]

  @nextZoneReferenceList.setter
  def nextZoneReferenceList(self,value):
    self._dict[ZoneFields.NEXT_ZONE_REFERENCE_LIST] = value
    self._changes[ZoneFields.NEXT_ZONE_REFERENCE_LIST] = value

  @property
  def alias(self):
    return self._dict[ZoneFields.ALIAS]

  @alias.setter
  def alias(self,value):
    self._dict[ZoneFields.ALIAS] = value
    self._changes[ZoneFields.ALIAS] = value

  @property
  def definitionKey(self):
    return self._dict[ZoneFields.DEFINITION_KEY]

  @definitionKey.setter
  def definitionKey(self,value):
    self._dict[ZoneFields.DEFINITION_KEY] = value
    self._changes[ZoneFields.DEFINITION_KEY] = value