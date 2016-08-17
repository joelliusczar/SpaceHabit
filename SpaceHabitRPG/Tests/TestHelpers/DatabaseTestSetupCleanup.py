"""
  This module is for inserting test data into the database and for cleaning up
  the test data so that it doesn't get in the way of other tests
"""

from AuthenticationLayer import AuthenticationFields as authFields
from AllDBFields import ZoneDBFields
from AllDBFields import ZoneDefinitionFields
from AllDBFields import HeroDbFields
from AllDBFields import MonsterDbFields
from AllDBFields import MonsterDefinitionFields
from AllDBFields import AccountDbFields
from Monster import Monster
from Hero import Hero
from Zone import Zone
import DatabaseLayer
import CryptKeeper
import MonkeyPatches

def clean_up():
  """
    remove all the data from the test database
  """
  connection = DatabaseLayer.open_conn()
  connection.drop_database("test")

def create_test_user_using_default_values():
  loginPk = create_login_using_test_values()
  accountPk = create_test_account_using_default_values(loginPk)
  heroPk = setup_test_hero_using_default_values(accountPk)
  return {'loginPk':loginPk,'accountPk':accountPk,'heroPk':heroPk}

def create_login_using_test_values():
  collection = DatabaseLayer.get_table(authFields.COLLECTION_NAME)
  pk = collection.insert_one({authFields.USER_LOGIN:"a@b.c",authFields.USER_DESC: 
    "a@b.c",authFields.USER_PASSWORD:CryptKeeper.encrypt_str("123456")}).inserted_id
  return pk

def create_test_account_using_default_values(loginPk=None):
  from Account import Account
  accountPk = Account.create_new_account_in_db(loginPk)
  return accountPk


def create_test_hero_dict(accountPk = None):
  import uuid
  zone = create_test_zone_dict()
  zoneVisitCounts = {ZoneDefinitionFields.ASTEROID_FIELD:5,ZoneDefinitionFields.EMPTY_SPACE:11}
  hero = {
      HeroDbFields.ACCOUNT_PK_KEY: accountPk,
      HeroDbFields.SHIP_NAME: "USS testship",
      HeroDbFields.LVL:7,
      HeroDbFields.GOLD:100,
      HeroDbFields.MAX_HP: 40,
      HeroDbFields.NOW_HP: 20,
      HeroDbFields.MAX_XP: 50,
      HeroDbFields.NOW_XP: 0,
      HeroDbFields.ATTACK_LVL: 5,
      HeroDbFields.DEFENSE_LVL: 6,
      HeroDbFields.PUBLIC_KEY: uuid.uuid4().hex,
      HeroDbFields.ZONE_VISIT_COUNTS: zoneVisitCounts,
      HeroDbFields.ZONE: create_test_zone_obj().dict,
      HeroDbFields.MONSTER: create_test_monster_obj().dict
      }

  return hero

def setup_test_hero_using_default_values(accountPk = None):
  
  h = create_test_hero_using_default_values(accountPk)
  h.save_changes()
  return h.get_pk()


def create_test_hero_using_default_values(accountPk = None):
  MonkeyPatches.set_mock_choice()
  h = Hero.construct_unsaved_hero(accountPk,"")
  MonkeyPatches.reset_choice()
  return h


def create_test_hero_using_test_values(accountPk = None):
  
  heroDict = create_test_hero_dict(accountPk = None)
  h = Hero.construct_model_from_dict(heroDict)
  h.save_changes()
  return h.get_pk()


def create_test_zone_dict(zoneKey=None):
  
  
  if not zoneKey:
    zoneKey = ZoneDefinitionFields.EMPTY_SPACE
  zoneDict = {
    ZoneDBFields.DEFINITION_KEY: zoneKey,
    ZoneDBFields.SUFFIX: "Alpha",
    ZoneDBFields.MONSTERS_KILLED: 2,
    ZoneDBFields.MAX_MONSTERS: 15,
    ZoneDBFields.LVL: 3,
    }
  return zoneDict

def create_test_zone_obj(zoneKey=None):
  
  zoneDict = create_test_zone_dict(zoneKey)
  zoneObj = Zone.construct_model_from_dict(zoneDict)
  return zoneObj

def create_test_monster_dict(monsterkey=None):
  
  if not monsterkey:
    monsterkey = MonsterDefinitionFields.AMBUSH_PIRATES
  monsterDict = {
    MonsterDbFields.DEFINITION_KEY: monsterkey,
    MonsterDbFields.MAX_HP: 150,
    MonsterDbFields.NOW_HP: 100,
    MonsterDbFields.LVL: 15
    }
  return monsterDict

def create_test_monster_obj(monsterkey=None):
  
  monsterDict = create_test_monster_dict(monsterkey)
  monsterObj = Monster.construct_model_from_dict(monsterDict)
  return monsterObj
