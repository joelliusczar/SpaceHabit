from SpaceUnitTest import SpaceUnitTest
from Monster import Monster
from AllDBFields import ZoneDefinitionFields
from AllDBFields import MonsterDefinitionFields
from AllDBFields import MonsterDbFields
import random
import MonkeyPatches
import DatabaseTestSetupCleanup as dbHelp
import TestUtilities as tu
import DatabaseLayer

class Test_Monster(SpaceUnitTest):


  @classmethod
  def setUpClass(cls):
    DatabaseLayer.isUnitTestMode = True
    dbHelp.clean_up()
    return super().setUpClass()

  def tearDown(self):
    dbHelp.clean_up()
    return super().tearDown()

  def test_get_random_monster_definitionKey(self):
    random.choice = MonkeyPatches.mock_choice
    k = Monster.get_random_monster_definitionKey(ZoneDefinitionFields.GAS)
    self.assertEqual(k,'cloudfortress')
    k = Monster.get_random_monster_definitionKey(ZoneDefinitionFields.GAS)
    self.assertEqual(k,'mScout')
    k = Monster.get_random_monster_definitionKey(ZoneDefinitionFields.GAS)
    self.assertEqual(k,'mech')
    k = Monster.get_random_monster_definitionKey(ZoneDefinitionFields.GAS)
    self.assertEqual(k,'pirate')
    k = Monster.get_random_monster_definitionKey(ZoneDefinitionFields.GAS)
    self.assertEqual(k,'poisonCloud')
    k = Monster.get_random_monster_definitionKey(ZoneDefinitionFields.GAS)
    self.assertEqual(k,'smallasteroid')
    k = Monster.get_random_monster_definitionKey(ZoneDefinitionFields.GAS)
    self.assertEqual(k,'spaceman')
    k = Monster.get_random_monster_definitionKey(ZoneDefinitionFields.GAS)
    self.assertEqual(k,'spaceslime')
    self.assertRaises(StopIteration,Monster.get_random_monster_definitionKey,ZoneDefinitionFields.GAS)

  def test_construct_new_monster(self):
    random.choice = MonkeyPatches.mock_choice_first_index
    random.randint = lambda l,h: 3
    m = Monster.construct_new_monster(ZoneDefinitionFields.GAS,10)
    self.assertEqual(m.lvl,13)

  def test_monster_properties_default(self):
    m = Monster(MonsterDefinitionFields.AMBUSH_PIRATES)
    m.nowHp = 100
    m.maxHp = 150
    m.lvl = 15


    self.assertEqual(m.nowHp,100)
    self.assertEqual(m.maxHp,150)
    self.assertEqual(m.get_baseXpReward(),1)
    self.assertEqual(m.get_treasureDropRate(),.1)
    self.assertEqual(m.definitionKey,MonsterDefinitionFields.AMBUSH_PIRATES)
    self.assertEqual(len(m.get_treasureDrops()), 0)
    self.assertEqual(m.get_name(),"Sneaky Ambush Pirates")
    self.assertEqual(m.get_description(),"These Sneaky Pirates hide behind asteroids "
        "and surprise you. They're sorta like deadlines.")


  def test_monster_properties_from_dict(self):
    hpk = dbHelp.setup_test_hero_using_default_values()
    md = dbHelp.create_test_monster_dict()
    m = Monster.construct_model_from_dict(md)

    self.assertEqual(m.nowHp,100)
    self.assertEqual(m.maxHp,150)
    self.assertEqual(m.get_baseXpReward(),1)
    self.assertEqual(m.get_treasureDropRate(),.1)
    self.assertEqual(m.definitionKey,MonsterDefinitionFields.AMBUSH_PIRATES)
    self.assertEqual(len(m.get_treasureDrops()), 0)
    self.assertEqual(m.get_name(),"Sneaky Ambush Pirates")
    self.assertEqual(m.get_description(),"These Sneaky Pirates hide behind asteroids "
        "and surprise you. They're sorta like deadlines.")

    oldCount = tu.get_record_count_from_table(MonsterDbFields.COLLECTION_NAME)

    m.save_changes(hpk)
    newcount = tu.get_record_count_from_table(MonsterDbFields.COLLECTION_NAME)
    self.assertEqual(oldCount,newcount)



if __name__ == '__main__':
    unittest.main()
