from SpaceUnitTest import SpaceUnitTest
from Zone import Zone
from Hero import Hero
from Monster import Monster
import DatabaseTestSetupCleanup as dbHelp
import TestUtilities as tu
import DatabaseLayer
from AllDBFields import ZoneDefinitionFields
from AllDBFields import MonsterDefinitionFields
from AllDBFields import HeroDbFields
from AllDBFields import ZoneDBFields

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
    id = dbHelp.create_test_hero_using_test_values()
    h = Hero.construct_model_from_pk(id)
    h.zone.maxMonsters = 100
    h.save_changes()
    h2 = Hero.construct_model_from_pk(id)
    self.assertNotEqual(h2.zone.maxMonsters,100)
    Zone.save_changes = tmpSave

  def test_hero_properties_default(self):
    h = Hero()
    h.lvl = 7
    h.maxHp = 100
    h.nowHp = 75
    h.maxXp = 40
    h.nowXp = 20
    h.gold = 100
    h.attackLvl = 5
    h.defenseLvl = 6
    h.zoneVisitCounts = {ZoneDefinitionFields.ASTEROID_FIELD:3,ZoneDefinitionFields.CAVE:11}
    h.zone = Zone(ZoneDefinitionFields.EMPTY_SPACE)
    h.monster = Monster(MonsterDefinitionFields.AMBUSH_PIRATES)
    h.shipName = "USS KickAss"

    self.assertEqual(h.lvl,7)
    self.assertEqual(h.maxHp,100)
    self.assertEqual(h.nowHp,75)
    self.assertEqual(h.maxXp,40)
    self.assertEqual(h.nowXp,20)
    self.assertEqual(h.gold,100)
    self.assertEqual(h.attackLvl,5)
    self.assertEqual(h.defenseLvl,6)
    self.assertDictEqual(h.zoneVisitCounts,{ZoneDefinitionFields.ASTEROID_FIELD:3,ZoneDefinitionFields.CAVE:11})
    self.assertEqual(h.zone.definitionKey,ZoneDefinitionFields.EMPTY_SPACE)
    self.assertEqual(h.monster.definitionKey,MonsterDefinitionFields.AMBUSH_PIRATES)
    self.assertEqual(h.shipName,"USS KickAss")

  def test_hero_properties_from_dict(self):
    hDict = dbHelp.create_test_hero_dict()
    h = Hero.construct_model_from_dict(hDict)
    h.save_changes()

    self.assertIsNotNone(h.get_pk())

    self.assertEqual(h.lvl,7)
    self.assertEqual(h.maxHp,40)
    self.assertEqual(h.nowHp,20)
    self.assertEqual(h.maxXp,50)
    self.assertEqual(h.nowXp,0)
    self.assertEqual(h.gold,100)
    self.assertEqual(h.attackLvl,5)
    self.assertEqual(h.defenseLvl,6)
    self.assertDictEqual(h.zoneVisitCounts,{ZoneDefinitionFields.ASTEROID_FIELD:5,ZoneDefinitionFields.EMPTY_SPACE:11})
    self.assertEqual(h.zone.definitionKey,ZoneDefinitionFields.EMPTY_SPACE)
    self.assertIsNotNone(h.zone.get_pk())
    self.assertEqual(h.monster.definitionKey,MonsterDefinitionFields.AMBUSH_PIRATES)
    self.assertEqual(h.shipName,"USS testship")

  def test_hero_properties_from_id(self):
    hPk = dbHelp.create_test_hero_using_test_values()

    h = Hero.construct_model_from_pk(hPk)

    self.assertIsNotNone(h.get_pk())

    self.assertEqual(h.lvl,7)
    self.assertEqual(h.maxHp,40)
    self.assertEqual(h.nowHp,20)
    self.assertEqual(h.maxXp,50)
    self.assertEqual(h.nowXp,0)
    self.assertEqual(h.gold,100)
    self.assertEqual(h.attackLvl,5)
    self.assertEqual(h.defenseLvl,6)
    self.assertDictEqual(h.zoneVisitCounts,{ZoneDefinitionFields.ASTEROID_FIELD:5,ZoneDefinitionFields.EMPTY_SPACE:11})
    self.assertEqual(h.zone.definitionKey,ZoneDefinitionFields.EMPTY_SPACE)
    self.assertIsNotNone(h.zone.get_pk())
    self.assertEqual(h.monster.definitionKey,MonsterDefinitionFields.AMBUSH_PIRATES)
    self.assertEqual(h.shipName,"USS testship")

  def test_save_counts(self):
    hDict = dbHelp.create_test_hero_dict()
    h = Hero.construct_model_from_dict(hDict)
    oldHeroCount = tu.get_record_count_from_table(HeroDbFields.COLLECTION_NAME)
    oldZoneCOunt = tu.get_record_count_from_table(ZoneDBFields.COLLECTION_NAME)
    h.save_changes()
    newHeroCount = tu.get_record_count_from_table(HeroDbFields.COLLECTION_NAME)
    newZoneCount = tu.get_record_count_from_table(ZoneDBFields.COLLECTION_NAME)
    self.assertEqual(oldHeroCount+1,newHeroCount)
    self.assertEqual(oldZoneCOunt+1,newZoneCount)

    oldHeroCount = tu.get_record_count_from_table(HeroDbFields.COLLECTION_NAME)
    oldZoneCOunt = tu.get_record_count_from_table(ZoneDBFields.COLLECTION_NAME)
    h.save_changes()
    newHeroCount = tu.get_record_count_from_table(HeroDbFields.COLLECTION_NAME)
    newZoneCount = tu.get_record_count_from_table(ZoneDBFields.COLLECTION_NAME)
    self.assertEqual(oldHeroCount,newHeroCount)
    self.assertEqual(oldZoneCOunt,newZoneCount)


  def test_next_zones_have_no_pk(self):
    h = dbHelp.create_test_hero_using_default_values()
    zones = h.zone.nextZoneReferenceList
    for z in zones:
      self.assertNotIn(ZoneDBFields.PK_KEY,z)

if __name__ == '__main__':
    unittest.main()
