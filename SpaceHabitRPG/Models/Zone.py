from StoryModels import StoryModels
from AllDBFields import ZoneDBFields
from ZoneDefinitions import ZoneDefinition
from ZoneDefinitions import AllZones
from bson.objectid import ObjectId
from OrphanedModelException import OrphanedModelException
import DatabaseLayer
import random







class Zone(StoryModels):
  """
    This is a wrapper for the zone data from the database. This is different
    from the other models in that Zone is used as a part of the hero model.

  """

  def __init__(self, definitionKey):
    return super().__init__(definitionKey)


  @classmethod
  def construct_model_from_pk(cls,pk):
    """
      args:
        id:
          uses the id to load this model from the database.

      return: an instance of the model on which this is called
    """
    
    collection = DatabaseLayer.get_table(cls.get_dbFields().COLLECTION_NAME)
    obj = cls(None)
    obj.dict = collection.find_one({cls.get_dbFields().PK_KEY:pk})
    return obj

  def save_changes(self,heroId):
    """
      args:
        heroId:
          this needs to be an pymongo objectId. It is used as an owner 
          relationship to a hero model
         
    """
    from AllDBFields import HeroDbFields
    ownerCollection = DatabaseLayer.get_table(self.get_dbFields().OWNER_COLLECTION)
    if self.get_pk():
      if self._changes:
        ownerCollection.update_one({self.get_dbFields().PK_KEY:heroId},{'$set':self._changes})
    else:
      collection = DatabaseLayer.get_table(self.get_dbFields().COLLECTION_NAME)
      pk = collection.insert_one(self.dict).inserted_id
      self.dict[self.get_dbFields().PK_KEY] = pk
      nestedZone = {HeroDbFields.ZONE:self.dict}
      ownerCollection.update_one({self.get_dbFields().PK_KEY:heroId},{'$set':nestedZone})
    self._changes = {}


  @classmethod
  def get_dbFields(cls):
    return ZoneDBFields

  def get_zoneName(self):
    if not self._definition:
      self._definition = ZoneDefinition(self.definitionKey)
    return self._definition.get_name()


  def get_fullName(self):
    return "{0} {1}".format(self.get_zoneName(),self.suffix).rstrip()


  @property
  def suffix(self):
    if self.get_dbFields().SUFFIX in self.dict:
      return self.dict[self.get_dbFields().SUFFIX]
    else:
      return ""

  @suffix.setter
  def suffix(self,value):
    self.set_common_story_property(self.get_dbFields().SUFFIX,value)


  @property
  def monstersKilled(self):
    if self.dict[self.get_dbFields().MONSTERS_KILLED]:
      return self.dict[self.get_dbFields().MONSTERS_KILLED]
    else:
      return 0

  @monstersKilled.setter
  def monstersKilled(self,value):
    self.set_common_story_property(self.get_dbFields().MONSTERS_KILLED,value)

  @property
  def maxMonsters(self):
    return self.dict[self.get_dbFields().MAX_MONSTERS]

  @maxMonsters.setter
  def maxMonsters(self,value):
    self.set_common_story_property(self.get_dbFields().MAX_MONSTERS,value)

  @property
  def lvl(self):
    return self.dict[self.get_dbFields().LVL]

  @lvl.setter
  def lvl(self,value):
    self.set_common_story_property(self.get_dbFields().LVL,value)

  def get_description(self):
    if not self._definition:
      self._definition = ZoneDefinition(self.definitionKey)
    return self._definition.get_description()

  @property
  def previousZoneReferencePK(self):
    if self.get_dbFields().PREVIOUS_ZONE_REFERENCE_PK in self.dict:
      return self.dict[self.get_dbFields().PREVIOUS_ZONE_REFERENCE_PK]
    return None

  @previousZoneReferencePK.setter
  def previousZoneReferencePK(self,value):
    self.set_common_story_property(self.get_dbFields().PREVIOUS_ZONE_REFERENCE_PK,value)


  @property
  def nextZoneReferenceList(self):
    return self.dict[self.get_dbFields().NEXT_ZONE_REFERENCE_LIST]

  @nextZoneReferenceList.setter
  def nextZoneReferenceList(self,value):
    self.set_common_story_property(self.get_dbFields().NEXT_ZONE_REFERENCE_LIST,value)

  @property
  def alias(self):
    raise NotImplementedError()
    return self.dict[self.get_dbFields().ALIAS]

  @alias.setter
  def alias(self,value):
    raise NotImplementedError()
    self.dict[self.get_dbFields().ALIAS] = value
    self._changes[self.get_dbFields().ALIAS] = value

  @property
  def definitionKey(self):
    return self.dict[self.get_dbFields().DEFINITION_KEY]

  @definitionKey.setter
  def definitionKey(self,value):
    self.set_common_story_property(self.get_dbFields().DEFINITION_KEY,value)

  @classmethod
  def get_home_zone(cls):
    """
      this probably only needs to be called when a new hero is being created for
      a user

      args:
        heroId:
            this needs to be an pymongo objectId. It is used as an owner 
            relationship to a hero model

      returns:
        a model of type zone with starting details
    """
    from AllDBFields import ZoneDefinitionFields
    zone = Zone(ZoneDefinitionFields.HOME)

    zone.maxMonsters = 0
    zone.skillLvl = 0
    return zone

  @classmethod
  def construct_next_zone_choice(cls,heroLvl,vistiedZones,matchHeroLvl = False):

    """
      generates a zone with unique name and randomlvl

      args:
        heroLvl:
          this should be a positive integer greater than 1
        visitedZones:
          this should be a dict. the dict is used to keep tract of which
          name suffix combinations have popped up already.
        matchHeroLvl: 
          Set this to true if first level.if this is true than the zone 
          difficulty level will perfectly match the hero's level rather than
          approximate it.
        
      returns:
        a model of type zone
        also adds to the value for a key in the visitedZones dict
    """
    import GeneralUtilities as gu

    selectedZoneKey = Zone.get_random_zone_definitionKey(heroLvl)
    definition = ZoneDefinition(selectedZoneKey)
    zone = {ZoneDBFields.DEFINITION_KEY:selectedZoneKey,ZoneDBFields.LVL: heroLvl,
            ZoneDBFields.MAX_MONSTERS: random.randint(5,15),ZoneDBFields.NAME: definition.get_name(),
            ZoneDBFields.DESCRIPTION: definition.get_description()}
    if selectedZoneKey in vistiedZones: #if we've visited it before
      zone[ZoneDBFields.SUFFIX] =  Zone.generate_full_zone_name_suffix(vistiedZones[selectedZoneKey])
      zone[ZoneDBFields.FULL_NAME] = \
        "{0} {1}".format(zone[ZoneDBFields.NAME],zone[ZoneDBFields.SUFFIX]).rstrip()
      vistiedZones[selectedZoneKey] += 1
    else:
      zone[ZoneDBFields.FULL_NAME] = zone[ZoneDBFields.NAME]
      vistiedZones[selectedZoneKey] = 1
    if not matchHeroLvl:
      zone[ZoneDBFields.LVL] = gu.calculate_lvl(heroLvl,10)
    return zone


  @classmethod
  def get_random_zone_definitionKey(cls,heroLvl):
    """
      selects a random dictionary key to be used with ZoneDefinitions

      args:
        heroLvl:
          this should be a positive integer greater than 1

        returns:
          a string which is a dict key
    """
    zoneGroupKeys = Zone.get_unlocked_zone_groupKeys(heroLvl)
    selectedZoneGroupKey = random.choice(zoneGroupKeys)
    zoneList = list(AllZones[selectedZoneGroupKey].keys())
    return random.choice(zoneList)


  @classmethod 
  def generate_full_zone_name_suffix(cls,visitCount):
    """
      each time we visit a particular zone type, we don't want it to have
      the same exact name as last time. To do this, we will add a suffix to
      the name. This generates a suffic based on the number of times
      that zone has been hit.

      args:
        visitCount:
          the number of times the hero character has visited a zone
          
      returns:
        a suffix which will be a string. We will take this string and append
        it to stuff.
    """

    if visitCount < 1:
      return ""

    symbols = Zone.get_symbols()
    hugeVisitCountResult = Zone.special_action_for_extremely_huge_visitCounts(visitCount,symbols)
    numericSuffix = hugeVisitCountResult['numericSuffix']
    visitCount = hugeVisitCountResult['visitCount']
    adjustedVisitCount = Zone.skip_powers_of_base_in_number(visitCount,len(symbols))
    suffix = Zone.get_symbol_suffix(adjustedVisitCount,symbols)

    if numericSuffix > 0:
      suffix += str(numericSuffix)
    return suffix.strip()


  @classmethod
  def special_action_for_extremely_huge_visitCounts(cls,visitCount,symbols):
    """
      this gets a special suffix for extremely huge vist counts, i.e, higher
      than 10100. Also shrinks the number play nicely with the normal suffix
      generating process

      args:
        visitCount:
          the number of times the hero character has visited a zone
        symbols:
          the list of symbols. We're changing the first element to something
          magic
       return:
        a dict with the numericSuffix value and the updated visitCount
    """
    numericSuffix = 0
    if visitCount > (len(symbols)-1) * len(symbols):
      symbols[0] = "?4815162342"
      numericSuffix = Zone.get_numeric_suffix(visitCount,len(symbols))
      visitCount = Zone.adjust_visitCount_for_extremely_huge_counts(visitCount,len(symbols))
    return {'numericSuffix':numericSuffix,'visitCount':visitCount}


  @classmethod
  def get_symbol_suffix(cls,visitCount,symbols):
    """
    converts a number to a suffix.
    Think of it as converting a number to a base 100 system of sorts
      args:
        visitCount:
            the number of times the hero character has visited a zone
          symbols:
            the list of symbols. 
      return:
        a string to be zone suffix
    """
    suffix = ""
    while visitCount > 0:
      r = visitCount % len(symbols)
      visitCount //= len(symbols)
      suffix = (symbols[r] + " " + suffix)
    return suffix


  @classmethod
  def adjust_visitCount_for_extremely_huge_counts(cls,visitCount,symbolsLen):
    """
      args:
        visitCount:
          the number of times the hero character has visited a zone
        symbolsLen:
          the count of all the available symbols to be made into a suffix
    """
    return visitCount % ((symbolsLen-1) * symbolsLen) 


  @classmethod
  def get_numeric_suffix(cls,visitCount,symbolsLen):
    """
      args:
        visitCount:
          the number of times the hero character has visited a zone
        symbolsLen:
          the count of all the available symbols to be made into a suffix
    """
    #the -1 on the first array length is to account for the single symbol range of items
    return visitCount // ((symbolsLen-1) * symbolsLen) + 1 #+1 because the 1 suffix would be redundant
   

  @classmethod
  def get_symbols(cls):
    """
      if you add any items to symbols, please adjust the unit test
      to account for that
    """
    symbols =["","Alpha", "Beta","Cain","Delta", #4
      "Epsilon","Foxtrot","September","October", #8
      "November","Kilo","Juliett","Romeo","Silver","Deckard", #14
      "Sierra","Tango","Zeta","Theta","July","Ludwig","Tyrell", #21
      "Lambda","Mu","London","Victor","Quintin","Gold", #27 
      "Whiskey","Xray","Zulu","Pi","Rho","Antilles","Blanca", #34
      "Sigma","Tau","India","Hector","Quebec","Waltz","Sapphire", #41
      "Tokyo","Ramesses","Washington","Darius","Emerald","Midgard", #47
      "Futura","Charlotte","Flanders","Berlin","Onion","Ruby", #53
      "David","Pizza","Lazlo","Kong","Jerico","Diamond", #59
      "Black","White","Olaf","Biggs","Wedge","Tyrannus", #65
      "Richter","Medusa","Swan","Gemini","Noir","Xerxes",#71
      "TNT","Plutonia","Cerberus","Tiberius", #75
      "Arcturus","Prime","Tarsonis","Babylon","Sparta",#80
      "Atlanta","Yutani","Python","Ridley","Midway", #85
      "Bismark","Dextera","Dominus","Jejunum", #89
      "Superior","Distal","Eurebus","Indigo", #93
      "Xs","Rex","Titan","Zen","Apex","Omega","Zed"] #100

    return symbols

  @classmethod
  def skip_powers_of_base_in_number(cls,num,base):
    """
      Numbers naturally want to follow this pattern:
      0,A,B,C,...,Y,Z,A0,AA,AB,AC,...,AY,AZ,B0,BA,BB,BC
      But I want zone suffix naming system to follow this pattern:
      0,A,B,C,...,Y,Z,AA,AB,AC,...,AY,AZ,BA,BB,BC,... 
      This function adjust numbers to fit the wanted pattern, 
      i.e. without the proverbial mulitples of 10
      The accuracy of this function becomes unreliable after base^2

      args:
        num:
          this is the number that we're offsetting.
        base:
          an integer. multiples of this number will be skipped

      returns:
        a number that's been offset for the base occurances skipped over

    """
    if base < 1 or not float.is_integer(float(base)):
      raise ValueError("Base needs to be a positive non-zero integer")
    if not float.is_integer(float(num)):
      raise ValueError("num needs to be an integer and not a floating number")
    isNegative = False
    if num < 0:
      num *= -1
      isNegative = True
    adjusterNum = num + (num // base)
    return num + (adjusterNum // base)

  @classmethod
  def get_unlocked_zone_groupKeys(cls,heroLvl):
    """"
      gets the list of availible zones groups that can be selected depeding on the 
      hero's level

      args:
        heroLvl:
          this should be an interger 
      returns:
        a list of dict keys to the AllZones dict.
    """
    if heroLvl < 1:
      return []
    availableZonesGroups = []
    availableZonesGroups.append("lvl1Zones")
    if heroLvl >= 5:
      availableZonesGroups.append("lvl5Zones")
    if heroLvl >= 10:
      availableZonesGroups.append("lvl10Zones")
    if heroLvl >= 15:
      availableZonesGroups.append("lvl15Zones")
    if heroLvl >= 20:
      availableZonesGroups.append("lvl20Zones")
    if heroLvl >= 25:
      availableZonesGroups.append("lvl25Zones")
    if heroLvl >= 30:
      availableZonesGroups.append("lvl30Zones")
    return availableZonesGroups



