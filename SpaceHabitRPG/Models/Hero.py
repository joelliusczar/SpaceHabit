from HabitBaseModel import HabitBaseModel
from AllDBFields import HeroDbFields
from Zone import Zone
from Monster import Monster








class Hero(HabitBaseModel):
  """
    This is a wrapper for the hero data from the database
  """
  

  @classmethod
  def construct_new_hero_in_db(cls,accountId = None,shipName = ""):
    import uuid
    zoneVisitCounts = {}
    homeZone = Zone.get_home_zone()
    zones = []
    zones.append(Zone.construct_new_zone(1,zoneVisitCounts,True).dict)
    zones.append(Zone.construct_new_zone(1,zoneVisitCounts).dict)
    zones.append(Zone.construct_new_zone(1,zoneVisitCounts).dict)
    homeZone.nextZoneReferenceList = zones
    hero = {
      HeroDbFields.ACCOUNT_PK_KEY: accountId,
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
      HeroDbFields.IS_IN_ZONE_LIMBO: True
    }
    heroObj = cls.create_model_from_dict(hero)
    heroObj.zone = homeZone
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
    self.zone.save_changes(self.get_pk())
    if self.monster:
      self.monster.save_changes(self.get_pk())





  @property
  def lvl(self):
    return self.dict[self.get_dbFields().LVL]

  @lvl.setter
  def lvl(self,value):
    self.dict[self.get_dbFields().LVL] = value
    self._changes[self.get_dbFields().LVL] = value

  @property
  def maxHp(self):
    return self.dict[self.get_dbFields().MAX_HP]

  @maxHp.setter
  def maxHp(self,value):
    self.dict[self.get_dbFields().MAX_HP] = value
    self._changes[self.get_dbFields().MAX_HP] = value

  @property
  def nowHp(self):
    return self.dict[self.get_dbFields().NOW_HP]

  @nowHp.setter
  def nowHp(self,value):
    self.dict[self.get_dbFields().NOW_HP] = value
    self._changes[self.get_dbFields().NOW_HP] = value

  @property
  def maxXp(self):
    return self.dict[self.get_dbFields().MAX_XP]

  @maxXp.setter
  def maxXp(self,value):
    self.dict[self.get_dbFields().MAX_XP] = value
    self._changes[self.get_dbFields().MAX_XP] = value

  @property
  def nowXp(self):
    return self.dict[self.get_dbFields().NOW_XP]

  @nowXp.setter
  def nowXp(self,value):
    self.dict[self.get_dbFields().NOW_XP] = value
    self._changes[self.get_dbFields().NOW_XP] = value

  @property
  def gold(self):
    return self.dict[self.get_dbFields().GOLD]

  @gold.setter
  def gold(self,value):
    self.dict[self.get_dbFields().GOLD] = value
    self._changes[self.get_dbFields().GOLD] = value

  @property
  def attackLvl(self):
    return self.dict[self.get_dbFields().ATTACK_LVL]

  @attackLvl.setter
  def attackLvl(self,value):
    self.dict[self.get_dbFields().ATTACK_LVL] = value
    self._changes[self.get_dbFields().ATTACK_LVL] = value

  @property
  def defenseLvl(self):
    return self.dict[self.get_dbFields().DEFENSE_LVL]

  @defenseLvl.setter
  def defenseLvl(self,value):
    self.dict[self.get_dbFields().DEFENSE_LVL] = value
    self._changes[self.get_dbFields().DEFENSE_LVL] = value

  @property
  def zoneVisitCounts(self):
    return self.dict[self.get_dbFields().ZONE_VISIT_COUNTS]

  @zoneVisitCounts.setter
  def zoneVisitCounts(self,value):
    self.dict[self.get_dbFields().ZONE_VISIT_COUNTS] = value
    self._changes[self.get_dbFields().ZONE_VISIT_COUNTS] = value

  
  @property
  def zone(self):
    if not self._zone:
      self._zone = Zone.construct_model_from_dict(self.dict[self.get_dbFields().ZONE])

    return self._zone

  @zone.setter
  def zone(self,value):  
    self.dict[self.get_dbFields().ZONE] = value.dict
    self._changes[self.get_dbFields().ZONE] = value.dict
    self._zone = Zone.construct_model_from_dict(self.dict[self.get_dbFields().ZONE])


  @property
  def isInZoneLimbo(self):
    if self.get_dbFields().IS_IN_ZONE_LIMBO in self.dict:
      return self.dict[self.get_dbFields().IS_IN_ZONE_LIMBO]
    else:
      return True

  @isInZoneLimbo.setter
  def isInZoneLimbo(self,value):
    self.dict[self.get_dbFields().IS_IN_ZONE_LIMBO] = value
    self._changes[self.get_dbFields().IS_IN_ZONE_LIMBO] = value

  @property
  def monster(self):
    if self.isInZoneLimbo:
      return None
    if not self._monster:
      self._monster = Monster.construct_model_from_dict(self.dict[self.get_dbFields().MONSTER])
    return self._monster

  @monster.setter
  def monster(self,value):
    self.dict[self.get_dbFields().MONSTER] = value.dict
    self._changes[self.get_dbFields().MONSTER] = value.dict
    self._monster = Monster.construct_model_from_dict(self.dict[self.get_dbFields().MONSTER])