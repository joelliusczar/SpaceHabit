from Hero import Hero
from SpaceUnitTest import SpaceUnitTest
import DatabaseTestSetupCleanup as dbHelp
import DatabaseLayer


class Test_HabitBaseModel(SpaceUnitTest):

  @classmethod
  def setUpClass(cls):
    dbHelp.clean_up()
    DatabaseLayer.isUnitTestMode = True
    return super().setUpClass()

  def tearDown(self):
    dbHelp.clean_up()
    return super().tearDown()

  def test_create_hero(self):
    hero = Hero()
    hero.attackLvl = 1
    hero.defenseLvl = 1
    hero.gold = 0
    hero.lvl = 1
    hero.maxHp = 100
    hero.maxXp = 0
    hero.save_changes()
    id = hero.id
    self.assertIsNotNone(id)
    hero.gold = 500
    hero.save_changes()
    heroCopy = Hero(id=id)
    self.assertEqual(heroCopy.gold,500)
    heroCopyFromDict = Hero(dict=hero._dict)
    self.assertEqual(heroCopyFromDict.id,id)

  def test_saving_zone_info(self):
    id = dbHelp.insert_one_hero()
    hero = Hero(id=id)
    z1 = hero.zone
    z1.monstersKilled = 5
    z2 = hero.zone
    self.assertEqual(z2.monstersKilled,5)
    z1.save_changes()
    hero2 = Hero(id=id)
    z3 = hero.zone
    self.assertEqual(z3.monstersKilled,5)
    
    

if __name__ == '__main__':
  unittest.main()
