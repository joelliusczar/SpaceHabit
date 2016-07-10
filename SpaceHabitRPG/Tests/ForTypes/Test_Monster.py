from SpaceUnitTest import SpaceUnitTest
from Monster import Monster
from AllDBFields import ZoneDefinitionFields
import random
import MonkeyPatches

class Test_Monster(SpaceUnitTest):

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

if __name__ == '__main__':
    unittest.main()
