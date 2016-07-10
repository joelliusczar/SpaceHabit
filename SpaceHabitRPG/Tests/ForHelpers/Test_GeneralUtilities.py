from SpaceUnitTest import SpaceUnitTest
import random
import MonkeyPatches
import GeneralUtilities as gu

class Test_GeneralUtilities(SpaceUnitTest):

    def test_calculate_lvl_1(self):
      random.randint = MonkeyPatches.mock_randint
      MonkeyPatches.testRandomNum = 0
      lvl = 1
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,1)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,2)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,3)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,4)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,5)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,6)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,7)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,8)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,9)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,10)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,11)
      self.assertRaises(OverflowError,lambda :gu.calculate_lvl(lvl,10))


    def test_calculate_lvl_5(self):
      random.randint = MonkeyPatches.mock_randint
      MonkeyPatches.testRandomNum = -5
      lvl = 5
      self.assertRaises(OverflowError,lambda :gu.calculate_lvl(lvl,10))
      MonkeyPatches.testRandomNum += 1
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,1)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,2)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,3)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,4)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,5)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,6)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,7)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,8)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,9)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,10)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,11)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,12)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,13)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,14)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,15)
      self.assertRaises(OverflowError,lambda :gu.calculate_lvl(lvl,10))


    def test_calculate_lvl_10(self): 
      random.randint = MonkeyPatches.mock_randint
      MonkeyPatches.testRandomNum = -10
      lvl = 10
      self.assertRaises(OverflowError,lambda :gu.calculate_lvl(lvl,10))
      MonkeyPatches.testRandomNum += 1
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,1)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,2)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,3)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,4)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,5)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,6)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,7)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,8)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,9)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,10)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,11)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,12)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,13)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,14)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,15)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,16)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,17)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,18)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,19)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,20)
      self.assertRaises(OverflowError,lambda :gu.calculate_lvl(lvl,10))


    def test_calculate_lvl_15(self): 
      random.randint = MonkeyPatches.mock_randint
      MonkeyPatches.testRandomNum = -11
      lvl = 15
      self.assertRaises(OverflowError,lambda :gu.calculate_lvl(lvl,10))
      MonkeyPatches.testRandomNum += 1
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,5)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,6)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,7)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,8)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,9)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,10)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,11)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,12)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,13)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,14)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,15)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,16)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,17)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,18)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,19)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,20)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,21)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,22)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,23)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,24)
      z = gu.calculate_lvl(lvl,10)
      self.assertEqual(z,25)
      self.assertRaises(OverflowError,lambda :gu.calculate_lvl(lvl,10))


if __name__ == '__main__':
    unittest.main()
