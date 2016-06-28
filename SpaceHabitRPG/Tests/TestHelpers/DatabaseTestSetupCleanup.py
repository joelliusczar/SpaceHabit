"""
  This module is for inserting test data into the database and for cleaning up
  the test data so that it doesn't get in the way of other tests
"""

from AuthenticationLayer import AuthenticationFields as fields
import DatabaseLayer
import CryptKeeper

def clean_up():
  """
    remove all the data from the test database
  """
  connection = DatabaseLayer.open_conn()
  connection.drop_database("test")

def insert_one_user():
  collection = DatabaseLayer.get_table(fields.COLLECTION_NAME)
  id = collection.insert_one({fields.USER_LOGIN:"a@b.c",fields.USER_DESC: 
    "a@b.c",fields.USER_PASSWORD:CryptKeeper.encrypt_str("123456")}).inserted_id
  return id

def insert_one_hero():
  from Hero import HeroFields
  from Zone import ZoneFields
  from Hero import Hero
  from ZoneDefinitions import zones
  lv1Zones = zones['lvl1Zones']
  zone = {
    ZoneFields.DEFINITION_KEY: lv1Zones[0]['key'],
    ZoneFields.NAME: lv1Zones[0]['name'],
    ZoneFields.DESCRIPTION: lv1Zones[0]['description'],
    ZoneFields.MAX_MONSTERS: 10,
    ZoneFields.MONSTERS_KILLED: 0,
    }

  hero = {
    HeroFields.LVL:1,
    HeroFields.GOLD:0,
    HeroFields.MAX_HP: 100,
    HeroFields.NOW_HP: 100,
    HeroFields.MAX_XP: 50,
    HeroFields.NOW_XP: 0,
    HeroFields.ATTACK_LVL: 1,
    HeroFields.DEFENSE_LVL: 1,
    HeroFields.ZONE: zone
  }
  collection = DatabaseLayer.get_table(Hero.COLLECTION_NAME)
  id = collection.insert_one(hero).inserted_id
  return id