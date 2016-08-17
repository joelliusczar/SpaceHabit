from Hero import Hero
from Zone import Zone
from SpaceUnitTest import SpaceUnitTest
import DatabaseTestSetupCleanup as dbtestHelp
import DatabaseLayer


class Test_HabitBaseModel(SpaceUnitTest):

  @classmethod
  def setUpClass(cls):
    DatabaseLayer.isUnitTestMode = True
    dbtestHelp.clean_up()
    return super().setUpClass()

  def tearDown(self):
    dbtestHelp.clean_up()
    return super().tearDown()

  def test_create_hero(self):
    hero = Hero()
    hero.attackLvl = 1
    hero.defenseLvl = 1
    hero.gold = 0
    hero.lvl = 1
    hero.maxHp = 100
    hero.maxXp = 0
    hero.zone = Zone.get_home_zone()
    hero.save_changes()
    pk = hero.get_pk()
    self.assertIsNotNone(pk)
    hero.gold = 500
    hero.save_changes()
    heroCopy = Hero.construct_model_from_pk(pk)
    self.assertEqual(heroCopy.gold,500)
    heroCopyFromDict = Hero.construct_model_from_dict(hero.dict)
    self.assertEqual(heroCopyFromDict.get_pk(),pk)

  def test_saving_zone_info(self):
    pk = dbtestHelp.create_test_hero_using_test_values()
    hero = Hero.construct_model_from_pk(pk)
    z1 = hero.zone
    z1.monstersKilled = 5
    z2 = hero.zone
    self.assertEqual(z2.monstersKilled,5)
    z1.save_changes(hero.get_pk())
    hero2 = Hero.construct_model_from_pk(pk)
    z3 = hero.zone
    self.assertEqual(z3.monstersKilled,5)

  def test_zone_on_hero_from_db(self):
    from AllDBFields import ZoneDefinitionFields
    pk = dbtestHelp.create_test_hero_using_test_values()
    hero = Hero.construct_model_from_pk(pk)
    hero.zone = dbtestHelp.create_test_zone_obj()
    self.assertEqual(hero.zone.definitionKey,ZoneDefinitionFields.EMPTY_SPACE)
    hero.save_changes()
    hero2 = Hero.construct_model_from_pk(pk)
    self.assertEqual(hero2.zone.definitionKey,ZoneDefinitionFields.EMPTY_SPACE)
    


    

if __name__ == '__main__':
  unittest.main()
