from HabitBaseModel import HabitBaseModel
from AllDBFields import HeroDbFields
from Zone import Zone
from Monster import Monster








class Hero(HabitBaseModel):
  """
    This is a wrapper for the hero data from the database
  """
  
  @classmethod
  def construct_unsaved_hero(cls,accountPk = None,shipName = ""):
    """
      args:
        accountPk: 
          an objectId for the accounts collection
        shipName:
          string. self-explainatory
      returns:
        an instance of the Hero class. Doesn't exist in db
    """
    import uuid
    zoneVisitCounts = {}
    homeZone = Zone.get_home_zone()
    zonesChoices = []
    zonesChoices.append(Zone.construct_next_zone_choice(1,zoneVisitCounts,True))
    zonesChoices.append(Zone.construct_next_zone_choice(1,zoneVisitCounts))
    zonesChoices.append(Zone.construct_next_zone_choice(1,zoneVisitCounts))
    homeZone.nextZoneReferenceList = zonesChoices
    hero = {
      HeroDbFields.ACCOUNT_PK_KEY: accountPk,
      HeroDbFields.SHIP_NAME: shipName,
      HeroDbFields.LVL:1,
      HeroDbFields.GOLD:0,
      HeroDbFields.MAX_HP: 100,
      HeroDbFields.NOW_HP: 100,
      HeroDbFields.MAX_XP: 50,
      HeroDbFields.NOW_XP: 0,
      HeroDbFields.ATTACK_LVL: 1,
      HeroDbFields.DEFENSE_LVL: 1,
      HeroDbFields.PUBLIC_KEY: uuid.uuid4().hex,
      HeroDbFields.ZONE_VISIT_COUNTS: zoneVisitCounts,
      HeroDbFields.ZONE: homeZone.dict
    }
    heroObj = cls.construct_model_from_dict(hero)
    return heroObj

  @classmethod
  def construct_new_hero_in_db(cls,accountPk = None,shipName = ""):
    """
      args:
        accountPk: 
          an objectId for the accounts collection
        shipName:
          string. self-explainatory
      returns:
        an objectId for the heros collection
    """
    heroObj = Hero.construct_unsaved_hero(accountPk,shipName)
    heroObj.save_changes()
    return heroObj.get_pk()

  def __init__(self):
    self._zone = None
    self._monster = None
    super().__init__()

  @classmethod
  def get_dbFields(cls):
    return HeroDbFields

  def save_changes(self):
    super().save_changes()
    if self.zone:
      self.zone.save_changes(self.get_pk())
    if self.monster:
      self.monster.save_changes(self.get_pk())





  @property
  def lvl(self):
    return self.dict[self.get_dbFields().LVL]

  @lvl.setter
  def lvl(self,value):
    self.set_common_property(self.get_dbFields().LVL,value)

  @property
  def maxHp(self):
    return self.dict[self.get_dbFields().MAX_HP]

  @maxHp.setter
  def maxHp(self,value):
    self.set_common_property(self.get_dbFields().MAX_HP,value)

  @property
  def nowHp(self):
    return self.dict[self.get_dbFields().NOW_HP]

  @nowHp.setter
  def nowHp(self,value):
    self.set_common_property(self.get_dbFields().NOW_HP,value)

  @property
  def maxXp(self):
    return self.dict[self.get_dbFields().MAX_XP]

  @maxXp.setter
  def maxXp(self,value):
    self.set_common_property(self.get_dbFields().MAX_XP,value)

  @property
  def nowXp(self):
    return self.dict[self.get_dbFields().NOW_XP]

  @nowXp.setter
  def nowXp(self,value):
    self.set_common_property(self.get_dbFields().NOW_XP,value)

  @property
  def gold(self):
    return self.dict[self.get_dbFields().GOLD]

  @gold.setter
  def gold(self,value):
    self.set_common_property(self.get_dbFields().GOLD,value)

  @property
  def attackLvl(self):
    return self.dict[self.get_dbFields().ATTACK_LVL]

  @attackLvl.setter
  def attackLvl(self,value):
    self.set_common_property(self.get_dbFields().ATTACK_LVL,value)

  @property
  def defenseLvl(self):
    return self.dict[self.get_dbFields().DEFENSE_LVL]

  @defenseLvl.setter
  def defenseLvl(self,value):
    self.set_common_property(self.get_dbFields().DEFENSE_LVL,value)

  @property
  def zoneVisitCounts(self):
    return self.dict[self.get_dbFields().ZONE_VISIT_COUNTS]

  @zoneVisitCounts.setter
  def zoneVisitCounts(self,value):
    self.set_common_property(self.get_dbFields().ZONE_VISIT_COUNTS,value)

  
  @property
  def zone(self):
    if not self._zone:
      if self.get_dbFields().ZONE in self.dict:
        self._zone = Zone.construct_model_from_dict(self.dict[self.get_dbFields().ZONE])
      else:
        return None

    return self._zone

  @zone.setter
  def zone(self,value):  
    self.dict[self.get_dbFields().ZONE] = value.dict
    self._changes[self.get_dbFields().ZONE] = value.dict
    self._zone = Zone.construct_model_from_dict(self.dict[self.get_dbFields().ZONE])


  @property
  def monster(self):
    if not self._monster:
      if self.get_dbFields().MONSTER in self.dict:
        self._monster = Monster.construct_model_from_dict(self.dict[self.get_dbFields().MONSTER])
      else:
        return None
    return self._monster

  @monster.setter
  def monster(self,value):
    self.dict[self.get_dbFields().MONSTER] = value.dict
    self._changes[self.get_dbFields().MONSTER] = value.dict
    self._monster = Monster.construct_model_from_dict(self.dict[self.get_dbFields().MONSTER])

  @property
  def shipName(self):
    if self.get_dbFields().SHIP_NAME in self.dict:
      return self.dict[self.get_dbFields().SHIP_NAME]
    else:
      return ""

  @shipName.setter
  def shipName(self,value):
    self.set_common_property(self.get_dbFields().SHIP_NAME,value)