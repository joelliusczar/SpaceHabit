from SpaceUnitTest import SpaceUnitTest
from Hero import Hero
import StartUpRoutine
import DatabaseTestSetupCleanup as dbHelp
import MonkeyPatches
import random
import DatabaseLayer

class Test_StartUpRoutine(SpaceUnitTest):

  EXPECTED_CHAR_COUNT_PLACEHOLDER = 879
  EXPECTED_CHAR_COUNT_TEST = 799

  @classmethod
  def setUpClass(cls):
    DatabaseLayer.isUnitTestMode = True
    dbHelp.clean_up()
    return super().setUpClass()

  def tearDown(self):
    dbHelp.clean_up()
    return super().tearDown()
  
  def test_insert_ship_name_into_intro(self):
    s = StartUpRoutine.get_intro_with_shipName_included("USS TestTest")
    self.assertEqual(len(s),self.EXPECTED_CHAR_COUNT_TEST)
    self.assertNotEqual(s.find("USS TestTest"),-1)
    s = StartUpRoutine.get_intro_with_shipName_included("")
    self.assertEqual(len(s),self.EXPECTED_CHAR_COUNT_PLACEHOLDER)
    self.assertNotEqual(s.find("USS Placeholder"),-1)
    s = StartUpRoutine.get_intro_with_shipName_included(None)
    self.assertEqual(len(s),self.EXPECTED_CHAR_COUNT_PLACEHOLDER)
    self.assertNotEqual(s.find("USS Placeholder"),-1)

  def test_build_first_time_checkin_messages(self):
    from ZoneDefinitions import ZoneDefinition
    from AllDBFields import ZoneDefinitionFields
    from AllDBFields import ZoneDBFields
    pkStruct = dbHelp.insert_total_test_user()
    hero = Hero.create_model_from_pk(pkStruct['heroPk'])
    m = StartUpRoutine.build_first_time_checkin_messages(hero)
    s0 = m['storyNotice']
    self.assertEqual(len(s0),self.EXPECTED_CHAR_COUNT_PLACEHOLDER)
    self.assertNotEqual(s0.find("USS Placeholder"),-1)
    s1 = m['zoneNotice']
    zdef = ZoneDefinition(ZoneDefinitionFields.HOME)
    self.assertEqual(s1,zdef.get_description())
    zPs = m['zonePrompt']
    self.assertEqual(len(zPs),3)
    zDef = ZoneDefinition(ZoneDefinitionFields.EMPTY_SPACE)
    zp0 = zPs[0]
    self.assertEqual(zp0[ZoneDBFields.FULL_NAME],zDef.get_name())
    self.assertEqual(zp0[ZoneDBFields.DESCRIPTION],zDef.get_description())
    zDef = ZoneDefinition(ZoneDefinitionFields.GAS)
    zp0 = zPs[1]
    self.assertEqual(zp0[ZoneDBFields.FULL_NAME],zDef.get_name())
    self.assertEqual(zp0[ZoneDBFields.DESCRIPTION],zDef.get_description())
    zDef = ZoneDefinition(ZoneDefinitionFields.NEBULA)
    zp0 = zPs[2]
    self.assertEqual(zp0[ZoneDBFields.FULL_NAME],zDef.get_name())
    self.assertEqual(zp0[ZoneDBFields.DESCRIPTION],zDef.get_description())



if __name__ == '__main__':
    unittest.main()
