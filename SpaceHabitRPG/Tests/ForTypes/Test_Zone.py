from SpaceUnitTest import SpaceUnitTest
from Zone import Zone
import random
import MonkeyPatches
import DatabaseTestSetupCleanup as dbHelp

class Test_Zone(SpaceUnitTest):
    

  def test_generate_area_name_suffix(self):
    symbols = Zone.get_symbols()
    combos = set()
    for s1 in symbols:
      for s2 in symbols:
        if not s1:
          continue
        combos.add("{} {}".format(s1,s2).strip())

    for i in range(1, 10101):
      s = Zone.generate_full_zone_name_suffix(i)
      self.assertTrue(s in combos)
      combos.discard(s)
    self.assertEqual(len(combos),0)
    s = Zone.generate_full_zone_name_suffix(0)
    self.assertEqual(s,"")
    s = Zone.generate_full_zone_name_suffix(1)
    self.assertEqual(s,"Alpha")
    s = Zone.generate_full_zone_name_suffix(2)
    self.assertEqual(s,"Beta")
    s = Zone.generate_full_zone_name_suffix(9)
    self.assertEqual(s,"November")
    s = Zone.generate_full_zone_name_suffix(100)
    self.assertEqual(s,"Zed")
    s = Zone.generate_full_zone_name_suffix(101)
    self.assertEqual(s,"Alpha Alpha")
    s = Zone.generate_full_zone_name_suffix(102)
    self.assertEqual(s,"Alpha Beta")
    s = Zone.generate_full_zone_name_suffix(200)
    self.assertEqual(s,"Alpha Zed")
    s = Zone.generate_full_zone_name_suffix(201)
    self.assertEqual(s,"Beta Alpha")
    s = Zone.generate_full_zone_name_suffix(202)
    self.assertEqual(s,"Beta Beta")
    s = Zone.generate_full_zone_name_suffix(10099)
    self.assertEqual(s,"Zed Omega")
    s = Zone.generate_full_zone_name_suffix(10100)
    self.assertEqual(s,"Zed Zed")
    s = Zone.generate_full_zone_name_suffix(10101)
    self.assertEqual(s,"Alpha 2")
    s = Zone.generate_full_zone_name_suffix(10102)
    self.assertEqual(s,"Beta 2")

  def test_define_zone(self):
    random.choice = MonkeyPatches.mock_choice_first_index
    random.randint = lambda l,u: 5
    lvl = 6
    visited = {}
    z = Zone.construct_new_zone(lvl,visited)
    self.assertEqual(z.get_fullName(),"Empty Space")
    self.assertEqual(z.lvl,11)
    self.assertEqual(z.maxMonsters,5)
    self.assertEqual(len(visited),1)
    self.assertEqual(visited['emptySpace'],1)
    z = Zone.construct_new_zone(lvl,visited)
    self.assertEqual(len(visited),1)
    self.assertEqual(visited['emptySpace'],2)
    self.assertEqual(z.get_fullName(),"Empty Space Alpha")
    z = Zone.construct_new_zone(lvl,visited,True)
    self.assertEqual(z.lvl,6)
    self.assertEqual(len(visited),1)
    self.assertEqual(visited['emptySpace'],3)
    self.assertEqual(z.get_fullName(),"Empty Space Beta")


  def test_get_random_zone_definitionKey_lvl5(self):
    random.choice = MonkeyPatches.mock_choice
    lvl = 5
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"emptySpace")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"gas")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"nebula")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"safeSpace")
    MonkeyPatches.testZoneGroup = "lvl5Zones"
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"asteroidField")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"backwater")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"solar")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"uncharted")
    self.assertRaises(StopIteration,Zone.get_random_zone_definitionKey,lvl)

  def test_get_random_zone_definitionKey_lvl4(self):
    random.choice = MonkeyPatches.mock_choice
    lvl = 4
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"emptySpace")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"gas")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"nebula")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"safeSpace")
    self.assertRaises(StopIteration,Zone.get_random_zone_definitionKey,lvl)

  def test_get_random_zone_definitionKey_lvl1(self):
    random.choice = MonkeyPatches.mock_choice
    lvl = 1
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"emptySpace")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"gas")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"nebula")
    z = Zone.get_random_zone_definitionKey(lvl)
    self.assertEqual(z,"safeSpace")
    self.assertRaises(StopIteration,Zone.get_random_zone_definitionKey,lvl)





  def test_convert_number_to_naming_number_base(self):
    n = Zone.skip_powers_of_base_in_number(0,10)
    self.assertEqual(n,0)
    n = Zone.skip_powers_of_base_in_number(1,10)
    self.assertEqual(n,1)
    n = Zone.skip_powers_of_base_in_number(9,10)
    self.assertEqual(n,9)
    n = Zone.skip_powers_of_base_in_number(10,10)
    self.assertEqual(n,11)
    n = Zone.skip_powers_of_base_in_number(11,10)
    self.assertEqual(n,12)
    n = Zone.skip_powers_of_base_in_number(18,10)
    self.assertEqual(n,19)
    n = Zone.skip_powers_of_base_in_number(19,10)
    self.assertEqual(n,21)
    n = Zone.skip_powers_of_base_in_number(20,10)
    self.assertEqual(n,22)
    n = Zone.skip_powers_of_base_in_number(21,10)
    self.assertEqual(n,23)
    n = Zone.skip_powers_of_base_in_number(27,10)
    self.assertEqual(n,29)
    n = Zone.skip_powers_of_base_in_number(28,10)
    self.assertEqual(n,31)
    n = Zone.skip_powers_of_base_in_number(91,10)
    self.assertEqual(n,101)
    n = Zone.skip_powers_of_base_in_number(100,10)
    self.assertEqual(n,111)

  

  def test_get_unlocked_zones(self):
    z = Zone.get_unlocked_zone_groupKeys(1)
    self.assertEqual(len(z),1)
    z = Zone.get_unlocked_zone_groupKeys(2)
    self.assertEqual(len(z),1)
    z = Zone.get_unlocked_zone_groupKeys(4)
    self.assertEqual(len(z),1)
    z = Zone.get_unlocked_zone_groupKeys(5)
    self.assertEqual(len(z),2)
    z = Zone.get_unlocked_zone_groupKeys(9)
    self.assertEqual(len(z),2)
    z = Zone.get_unlocked_zone_groupKeys(10)
    self.assertEqual(len(z),3)
    z = Zone.get_unlocked_zone_groupKeys(14)
    self.assertEqual(len(z),3)
    z = Zone.get_unlocked_zone_groupKeys(15)
    self.assertEqual(len(z),4)
    z = Zone.get_unlocked_zone_groupKeys(19)
    self.assertEqual(len(z),4)
    z = Zone.get_unlocked_zone_groupKeys(20)
    self.assertEqual(len(z),5)
    z = Zone.get_unlocked_zone_groupKeys(24)
    self.assertEqual(len(z),5)
    z = Zone.get_unlocked_zone_groupKeys(25)
    self.assertEqual(len(z),6)
    z = Zone.get_unlocked_zone_groupKeys(29)
    self.assertEqual(len(z),6)
    z = Zone.get_unlocked_zone_groupKeys(30)
    self.assertEqual(len(z),7)
    z = Zone.get_unlocked_zone_groupKeys(300)
    self.assertEqual(len(z),7)


  def test_load_zone_from_dict(self):
    from Zone import ZoneDBFields
    zd = {
      ZoneDBFields.DEFINITION_KEY: "gas"
      }

    z = Zone.construct_model_from_dict(zd)
    self.assertEqual(z.get_fullName(),"Gas Planet Orbit")

  def test_load_zone_from_pk(self):
    
    pk = dbHelp.insert_one_test_hero()
    z1 = Zone("gas")
    z1.maxMonsters = 10
    z1.lvl = 10
    z1.save_changes(pk)
    z2 = Zone.construct_model_from_pk(z1.get_pk())
    self.assertEqual(z1.get_description(),z2.get_description())
    self.assertEqual(z1.get_fullName(),z2.get_fullName())
    self.assertEqual(z1.maxMonsters,z2.maxMonsters)
    self.assertEqual(z1.lvl,z2.lvl)

  def test_that_zone_save_changes_does_not_overwrite_hero(self):
    from Hero import Hero
    from AllDBFields import ZoneDBFields
    id = dbHelp.insert_one_test_hero()
    h = Hero.create_model_from_pk(id)
    h.zone.maxMonsters = 1000
    h.zone.save_changes(id)
    self.assertNotIn(ZoneDBFields.MAX_MONSTERS,h.dict)
    h2 = Hero.create_model_from_pk(id)
    self.assertNotIn(ZoneDBFields.MAX_MONSTERS,h2.dict)


if __name__ == '__main__':
    unittest.main()
