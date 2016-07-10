from SpaceUnitTest import SpaceUnitTest
from Zone import Zone
from Hero import Hero
import DatabaseTestSetupCleanup as dbHelp
import DatabaseLayer

class Test_Hero(SpaceUnitTest):
    
  @classmethod
  def setUpClass(cls):
    DatabaseLayer.isUnitTestMode = True
    dbHelp.clean_up()
    return super().setUpClass()

  def tearDown(self):
    dbHelp.clean_up()
    return super().tearDown()

  def test_if_hero_save_saves_zone(self):
    tmpSave = Zone.save_changes
    Zone.save_changes = lambda s,h: 0
    id = dbHelp.insert_one_test_hero()
    h = Hero.create_model_from_pk(id)
    h.zone.maxMonsters = 100
    h.save_changes()
    h2 = Hero.create_model_from_pk(id)
    self.assertNotEqual(h2.zone.maxMonsters,100)
    Zone.save_changes = tmpSave



if __name__ == '__main__':
    unittest.main()
