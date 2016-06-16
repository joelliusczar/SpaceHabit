from SpaceUnitTest import SpaceUnitTest

class Test_SpaceUnitTest(SpaceUnitTest):
    def test_assertBool(self):
        t1 = None
        t2 = 6
        self.assertRaises(AssertionError, lambda :self.assertFalse(t1))
        self.assertRaises(AssertionError, lambda :self.assertTrue(t2))
        self.assertNotEqual(t1,False)
        self.assertNotEqual(t2,True)

if __name__ == '__main__':
    unittest.main()
