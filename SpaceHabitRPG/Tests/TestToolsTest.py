import MockDatabaseLayer
import TestFunctionBuilder
import unittest
import random

class Test_TestToolsTest(unittest.TestCase):

    def test_build_sort_function_single_property(self):
        dictDict = {}
        dictDict[10] = {'a':0}
        dictDict[11] = {'a':1}
        dictDict[12] = {'a':2}
        compareFieldList = [('a',1)]
        comparer = TestFunctionBuilder.build_sort_by_function(compareFieldList,dictDict)
        t = comparer(dictDict[10],dictDict[11])
        self.assertTrue(t)
        t = comparer(dictDict[11],dictDict[10])
        self.assertFalse(t)
        t = comparer(dictDict[10],dictDict[10])
        self.assertTrue(t)

    def test_build_sort_function_double_property(self):
        dictDict = {}
        for i in range(0,15):
            dictDict[10 + i] = {'a':i % 5, 'b': 15-i}
        compareFieldList = [('a',1),('b',-1)]
        comparer = TestFunctionBuilder.build_sort_by_function(compareFieldList,dictDict)
        t = comparer(dictDict[10],dictDict[20])
        self.assertTrue(t)
        t = comparer(dictDict[10],dictDict[11])
        self.assertTrue(t)
        t = comparer(dictDict[10],dictDict[24])
        self.assertTrue(t)

    def test_insert_and_get_from_mock_db(self):
        t1 = {'a':121,'b':235,'c':316}
        id = MockDatabaseLayer.insert_thing(t1,MockDatabaseLayer.dailies)
        self.assertEqual(id, MockDatabaseLayer.dailies + "0")
        t2 = MockDatabaseLayer.get_thing_by_id(id,MockDatabaseLayer.dailies)
        self.assertEqual(t2['_id'], MockDatabaseLayer.dailies + "0")
        self.assertEqual(t2['a'], 121)
        self.assertEqual(t2['b'], 235)
        self.assertEqual(t2['c'], 316)
        t2['a'] = 440
        t3 = MockDatabaseLayer.get_thing_by_id(id,MockDatabaseLayer.dailies)
        self.assertEqual(t1['a'], 121)
        self.assertEqual(t3['a'], 121)

    def test_update_and_delete_from_mock_db(self):
        t1 = {'a':121,'b':235,'c':316}
        id = MockDatabaseLayer.insert_thing(t1,MockDatabaseLayer.dailies)
        MockDatabaseLayer.update_thing_by_id(id,MockDatabaseLayer.dailies,{'b':255,'d':415})
        self.assertFalse('d' in t1)
        self.assertEqual(t1['b'], 235)
        t2 = MockDatabaseLayer.get_thing_by_id(id,MockDatabaseLayer.dailies)
        self.assertEqual(t2['b'], 255)
        self.assertEqual(t2['d'], 415)
        MockDatabaseLayer.delete_thing_by_key(id,MockDatabaseLayer.dailies)
        t3 = MockDatabaseLayer.get_thing_by_id(id,MockDatabaseLayer.dailies)
        self.assertIsNone(t3)

    def test_user_saving_and_validation(self):
        id = MockDatabaseLayer.insert_user("a","p","s")
        self.assertTrue(MockDatabaseLayer.does_login_exist("a"))
        self.assertFalse(MockDatabaseLayer.does_login_exist("n"))
        user = MockDatabaseLayer.get_user("a")
        self.assertEqual(user[MockDatabaseLayer.USER_LOGIN],"a")

    def test_get_sorted_stuff_by_key(self):
        testId1 = MockDatabaseLayer.insert_thing({'test':0}, MockDatabaseLayer.accounts)
        testId2 = MockDatabaseLayer.insert_thing({'test':1}, MockDatabaseLayer.accounts)
        self.assertEquals(testId1, MockDatabaseLayer.accounts+"0")
        self.assertEquals(testId2, MockDatabaseLayer.accounts+"1")
        controlList = []
        for i in range(0,2000):
            s = i // 100
            b = (2000 -i) // 25
            c = i
            d = i % 5
            if d == 1:
                tObj = {'testId':testId2,'a':s,'b':b,'c':c, 'd':d}
            else:
                tObj = {'testId':testId1,'a':s,'b':b,'c':c, 'd':d}
            controlList.append(tObj)
        testList = controlList[:]
        random.shuffle(testList)
    
        for d in testList:
            id = MockDatabaseLayer.insert_thing(d,MockDatabaseLayer.dailies)
        sortByList = [('a',1),('b',-1),('c',1)]
        sorted = MockDatabaseLayer.get_sorted_stuff_by_key({'testId':testId1},MockDatabaseLayer.dailies,sortByList)
        self.assertEqual(len(sorted),1600)
        sorted = MockDatabaseLayer.get_sorted_stuff_by_key({},MockDatabaseLayer.dailies,sortByList)
        self.assertEqual(len(sorted),2000)
        for s,c in zip(sorted,controlList):
            self.assertEqual(s['a'],c['a'])
            self.assertEqual(s['b'],c['b'])
            self.assertEqual(s['c'],c['c'])

if __name__ == '__main__':
    unittest.main()
