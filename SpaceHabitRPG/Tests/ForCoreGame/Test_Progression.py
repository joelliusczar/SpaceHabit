from SpaceUnitTest import SpaceUnitTest
from collections import OrderedDict
import Progression
import random

testRandomNum = 0
testRandomIter = None

def mock_randint(lowerBound,upperBound):
  """
    this will be used to replace the default random.randint method.
    We need a test method that will act consistently.

    args:
      lowerBound:
        this should be the mininum value that this method can return
      upperBound:
        this should be the maximum value that this method can return

    returns:
      the global variable testRandomNum
  """
  global testRandomNum
  if testRandomNum < lowerBound or testRandomNum > upperBound:
    raise OverflowError("out of bounds")
  testRandomNum += 1
  return testRandomNum -1

def mock_choice(array):
  """
    this will be used to replace the default random.choice method.
    We need a test method that will act consistently.

    args:
      array
        this is the list from which values will be selected

      returns:
        an item from the list. You know what you put in there.
  """
  global testRandomIter
  if not testRandomIter:
    testRandomIter = iter(array)

  return next(testRandomIter)


class Test_Progression(SpaceUnitTest):

  def test_define_zone(self):
    random.choice = lambda a: a[0]
    random.randint = lambda l,u: 5
    lvl = 6
    visited = {}
    z = Progression.define_zone(lvl,visited)
    self.assertEqual(z.zoneName,"Gas Planet Orbit")
    self.assertEqual(z.skillLvl,11)
    self.assertEqual(z.maxMonsters,5)
    self.assertEqual(len(visited),1)
    self.assertEqual(visited['gas'],1)
    z = Progression.define_zone(lvl,visited)
    self.assertEqual(len(visited),1)
    self.assertEqual(visited['gas'],2)
    self.assertEqual(z.zoneName,"Gas Planet Orbit Alpha")
    z = Progression.define_zone(lvl,visited,True)
    self.assertEqual(z.skillLvl,6)
    self.assertEqual(len(visited),1)
    self.assertEqual(visited['gas'],3)
    self.assertEqual(z.zoneName,"Gas Planet Orbit Beta")


  def test_select_random_zone_from_definitions_lvl5(self):
    random.choice = mock_choice
    lvl = 5
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Gas Planet Orbit")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Empty Space")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Asteroid Belt")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Nebula")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Secure Space")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Giant Space Garbage Ball Orbit")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Solar Orbit")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Uncharted Planet Orbit")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Backwater Planet Orbit")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Resort Planet Orbit")
    self.assertRaises(StopIteration,Progression.select_random_zone_from_definitions,lvl)

  def test_select_random_zone_from_definitions_lvl4(self):
    random.choice = mock_choice
    lvl = 4
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Gas Planet Orbit")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Empty Space")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Asteroid Belt")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Nebula")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Secure Space")
    self.assertRaises(StopIteration,Progression.select_random_zone_from_definitions,lvl)

  def test_select_random_zone_from_definitions_lvl1(self):
    random.choice = mock_choice
    lvl = 1
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Gas Planet Orbit")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Empty Space")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Asteroid Belt")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Nebula")
    z = Progression.select_random_zone_from_definitions(lvl)
    self.assertEqual(z.zoneName,"Secure Space")
    self.assertRaises(StopIteration,Progression.select_random_zone_from_definitions,lvl)


  def test_calculate_zone_lvl_1(self):
    random.randint = mock_randint
    global testRandomNum
    testRandomNum = 0
    lvl = 1
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,1)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,2)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,3)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,4)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,5)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,6)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,7)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,8)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,9)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,10)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,11)
    self.assertRaises(OverflowError,lambda :Progression.calculate_zone_lvl(lvl))


  def test_calculate_zone_lvl_5(self):
    random.randint = mock_randint
    global testRandomNum
    testRandomNum = -5
    lvl = 5
    self.assertRaises(OverflowError,lambda :Progression.calculate_zone_lvl(lvl))
    testRandomNum += 1
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,1)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,2)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,3)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,4)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,5)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,6)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,7)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,8)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,9)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,10)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,11)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,12)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,13)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,14)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,15)
    self.assertRaises(OverflowError,lambda :Progression.calculate_zone_lvl(lvl))


  def test_calculate_zone_lvl_10(self): 
    random.randint = mock_randint
    global testRandomNum
    testRandomNum = -10
    lvl = 10
    self.assertRaises(OverflowError,lambda :Progression.calculate_zone_lvl(lvl))
    testRandomNum += 1
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,1)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,2)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,3)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,4)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,5)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,6)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,7)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,8)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,9)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,10)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,11)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,12)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,13)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,14)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,15)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,16)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,17)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,18)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,19)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,20)
    self.assertRaises(OverflowError,lambda :Progression.calculate_zone_lvl(lvl))


  def test_calculate_zone_lvl_15(self): 
    random.randint = mock_randint
    global testRandomNum
    testRandomNum = -11
    lvl = 15
    self.assertRaises(OverflowError,lambda :Progression.calculate_zone_lvl(lvl))
    testRandomNum += 1
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,5)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,6)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,7)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,8)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,9)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,10)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,11)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,12)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,13)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,14)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,15)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,16)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,17)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,18)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,19)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,20)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,21)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,22)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,23)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,24)
    z = Progression.calculate_zone_lvl(lvl)
    self.assertEqual(z,25)
    self.assertRaises(OverflowError,lambda :Progression.calculate_zone_lvl(lvl))


  def test_convert_number_to_naming_number_base(self):
    n = Progression.offset_number_for_base(0,10)
    self.assertEqual(n,0)
    n = Progression.offset_number_for_base(1,10)
    self.assertEqual(n,1)
    n = Progression.offset_number_for_base(9,10)
    self.assertEqual(n,9)
    n = Progression.offset_number_for_base(10,10)
    self.assertEqual(n,11)
    n = Progression.offset_number_for_base(11,10)
    self.assertEqual(n,12)
    n = Progression.offset_number_for_base(18,10)
    self.assertEqual(n,19)
    n = Progression.offset_number_for_base(19,10)
    self.assertEqual(n,21)
    n = Progression.offset_number_for_base(20,10)
    self.assertEqual(n,22)
    n = Progression.offset_number_for_base(21,10)
    self.assertEqual(n,23)
    n = Progression.offset_number_for_base(27,10)
    self.assertEqual(n,29)
    n = Progression.offset_number_for_base(28,10)
    self.assertEqual(n,31)
    n = Progression.offset_number_for_base(91,10)
    self.assertEqual(n,101)
    n = Progression.offset_number_for_base(100,10)
    self.assertEqual(n,111)

  def test_generate_area_name_suffix(self):
    symbols =["","Alpha", "Beta","Cain","Delta", #4
      "Epsilon","Foxtrot","September","October", #8
      "November","Kilo","Juliett","Romeo","Silver","Deckard", #14
      "Sierra","Tango","Zeta","Theta","July","Ludwig","Tyrell", #21
      "Lambda","Mu","London","Victor","Quintin","Gold", #27 
      "Whiskey","Xray","Zulu","Pi","Rho","Antilles","Blanca", #34
      "Sigma","Tau","India","Hector","Quebec","Waltz","Sapphire", #41
      "Tokyo","Ramesses","Washington","Darius","Emerald","Midgard", #47
      "Futura","Charlotte","Flanders","Berlin","Onion","Ruby", #53
      "David","Pizza","Lazlo","Kong","Jerico","Diamond", #59
      "Black","White","Olaf","Biggs","Wedge","Tyrannus", #65
      "Richter","Medusa","Swan","Gemini","Noir","Xerxes",#71
      "TNT","Plutonia","Cerberus","Tiberius", #75
      "Arcturus","Prime","Tarsonis","Babylon","Sparta",#80
      "Atlanta","Yutani","Python","Ridley","Midway", #85
      "Bismark","Dextera","Dominus","Jejunum", #89
      "Superior","Distal","Eurebus","Indigo", #93
      "Xs","Rex","Titan","Zen","Apex","Omega","Zed"] #100
    combos = set()
    for s1 in symbols:
      for s2 in symbols:
        if not s1:
          continue
        combos.add("{} {}".format(s1,s2).strip())

    for i in range(1, 10101):
      s = Progression.generate_zone_name_suffix(i)
      self.assertTrue(s in combos)
      combos.discard(s)
    self.assertEqual(len(combos),0)
    s = Progression.generate_zone_name_suffix(0)
    self.assertEqual(s,"")
    s = Progression.generate_zone_name_suffix(1)
    self.assertEqual(s,"Alpha")
    s = Progression.generate_zone_name_suffix(2)
    self.assertEqual(s,"Beta")
    s = Progression.generate_zone_name_suffix(9)
    self.assertEqual(s,"November")
    s = Progression.generate_zone_name_suffix(100)
    self.assertEqual(s,"Zed")
    s = Progression.generate_zone_name_suffix(101)
    self.assertEqual(s,"Alpha Alpha")
    s = Progression.generate_zone_name_suffix(102)
    self.assertEqual(s,"Alpha Beta")
    s = Progression.generate_zone_name_suffix(200)
    self.assertEqual(s,"Alpha Zed")
    s = Progression.generate_zone_name_suffix(201)
    self.assertEqual(s,"Beta Alpha")
    s = Progression.generate_zone_name_suffix(202)
    self.assertEqual(s,"Beta Beta")
    s = Progression.generate_zone_name_suffix(10099)
    self.assertEqual(s,"Zed Omega")
    s = Progression.generate_zone_name_suffix(10100)
    self.assertEqual(s,"Zed Zed")
    s = Progression.generate_zone_name_suffix(10101)
    self.assertEqual(s,"Alpha 2")
    s = Progression.generate_zone_name_suffix(10102)
    self.assertEqual(s,"Beta 2")

  def test_get_unlocked_zones(self):
    z = Progression.get_unlocked_zones(1)
    self.assertEqual(len(z),5)
    z = Progression.get_unlocked_zones(2)
    self.assertEqual(len(z),5)
    z = Progression.get_unlocked_zones(4)
    self.assertEqual(len(z),5)
    z = Progression.get_unlocked_zones(5)
    self.assertEqual(len(z),10)
    z = Progression.get_unlocked_zones(9)
    self.assertEqual(len(z),10)
    z = Progression.get_unlocked_zones(10)
    self.assertEqual(len(z),13)
    z = Progression.get_unlocked_zones(14)
    self.assertEqual(len(z),13)
    z = Progression.get_unlocked_zones(15)
    self.assertEqual(len(z),16)
    z = Progression.get_unlocked_zones(19)
    self.assertEqual(len(z),16)
    z = Progression.get_unlocked_zones(20)
    self.assertEqual(len(z),19)
    z = Progression.get_unlocked_zones(24)
    self.assertEqual(len(z),19)
    z = Progression.get_unlocked_zones(25)
    self.assertEqual(len(z),24)
    z = Progression.get_unlocked_zones(29)
    self.assertEqual(len(z),24)
    z = Progression.get_unlocked_zones(30)
    self.assertEqual(len(z),27)
    z = Progression.get_unlocked_zones(300)
    self.assertEqual(len(z),27)
    doubles = set()
    for a in z:
      self.assertFalse(a['key'] in doubles)
      doubles.add(a['key'])

if __name__ == '__main__':
  unittest.main()

