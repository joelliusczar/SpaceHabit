import unittest
import Progression
from collections import OrderedDict


class Test_ProgressionTests(unittest.TestCase):

    def test_convert_number_to_naming_number_base(self):
        n = Progression.convert_number_to_naming_number_base(0,10)
        self.assertEqual(n,0)
        n = Progression.convert_number_to_naming_number_base(1,10)
        self.assertEqual(n,1)
        n = Progression.convert_number_to_naming_number_base(9,10)
        self.assertEqual(n,9)
        n = Progression.convert_number_to_naming_number_base(10,10)
        self.assertEqual(n,11)
        n = Progression.convert_number_to_naming_number_base(11,10)
        self.assertEqual(n,12)
        n = Progression.convert_number_to_naming_number_base(18,10)
        self.assertEqual(n,19)
        n = Progression.convert_number_to_naming_number_base(19,10)
        self.assertEqual(n,21)
        n = Progression.convert_number_to_naming_number_base(20,10)
        self.assertEqual(n,22)
        n = Progression.convert_number_to_naming_number_base(21,10)
        self.assertEqual(n,23)
        n = Progression.convert_number_to_naming_number_base(27,10)
        self.assertEqual(n,29)
        n = Progression.convert_number_to_naming_number_base(28,10)
        self.assertEqual(n,31)
        n = Progression.convert_number_to_naming_number_base(91,10)
        self.assertEqual(n,101)
        n = Progression.convert_number_to_naming_number_base(100,10)
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
