"""
  This module is for inserting test data into the database and for cleaning up
  the test data so that it doesn't get in the way of other tests
"""

from AuthenticationLayer import AuthenticationFields as authFields
import DatabaseLayer
import CryptKeeper

def clean_up():
  """
    remove all the data from the test database
  """
  connection = DatabaseLayer.open_conn()
  connection.drop_database("test")

def insert_test_user():
  loginPk = insert_one_test_login()
  accountPk = insert_one_default_account(loginPk)
  heroPk = insert_one_default_hero(accountPk)
  return {'loginPk':loginPk,'accountPk':accountPk,'heroPk':heroPk}

def insert_one_test_login():
  collection = DatabaseLayer.get_table(authFields.COLLECTION_NAME)
  pk = collection.insert_one({authFields.USER_LOGIN:"a@b.c",authFields.USER_DESC: 
    "a@b.c",authFields.USER_PASSWORD:CryptKeeper.encrypt_str("123456")}).inserted_id
  return pk

def insert_one_default_account(loginPk=None):
  from Account import Account
  accountPk = Account.create_new_account_in_db(loginPk)
  return accountPk

def insert_one_default_hero(accountPk = None):
  from Hero import Hero
  pk = Hero.construct_new_hero_in_db(accountPk,"")
  return pk

def insert_one_test_hero(accountPk = None):
  from Hero import HeroDbFields
  from Zone import ZoneDBFields
  from Hero import Hero
  from ZoneDefinitions import AllZones
  lv1Zones = AllZones['lvl1Zones']
  zoneKey = sorted(lv1Zones.keys())[0]
  zone = {
    ZoneDBFields.DEFINITION_KEY: zoneKey,
    ZoneDBFields.MAX_MONSTERS: 10,
    ZoneDBFields.MONSTERS_KILLED: 0,
    }
  hero = {
    HeroDbFields.LVL:1,
    HeroDbFields.ACCOUNT_PK_KEY: accountPk,
    HeroDbFields.GOLD:0,
    HeroDbFields.MAX_HP: 100,
    HeroDbFields.NOW_HP: 100,
    HeroDbFields.MAX_XP: 50,
    HeroDbFields.NOW_XP: 0,
    HeroDbFields.ATTACK_LVL: 1,
    HeroDbFields.DEFENSE_LVL: 1,
    HeroDbFields.ZONE: zone
  }
  collection = DatabaseLayer.get_table(HeroDbFields.COLLECTION_NAME)
  pk = collection.insert_one(hero).inserted_id
  return pk

def create_different_zone_dict():
  from ZoneDefinitions import AllZones
  from Zone import ZoneDBFields
  from Zone import Zone
  lv1Zones = AllZones['lvl1Zones']
  zoneKey = sorted(lv1Zones.keys())[1]
  zoneDict = {
    ZoneDBFields.DEFINITION_KEY: zoneKey,
    ZoneDBFields.MAX_MONSTERS: 15,
    ZoneDBFields.MONSTERS_KILLED: 2,
    }
  zoneObj = Zone.construct_model_from_dict(zoneDict)
  return zoneObj