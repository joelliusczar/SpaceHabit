from SpaceUnitTest import SpaceUnitTest
import MockDatabaseLayer
import random

class Test_MockDatabaseLayer(SpaceUnitTest):
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
        id = MockDatabaseLayer.insert_user("a@b.c","p","s")
        self.assertTrue(MockDatabaseLayer.does_login_exist("a@b.c"))
        self.assertFalse(MockDatabaseLayer.does_login_exist("n"))
        user = MockDatabaseLayer.get_user("a@b.c")
        self.assertEqual(user[MockDatabaseLayer.USER_LOGIN],"a@b.c")

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


    def test_unfiltered_mockdb_count(self):
        for i in range(0,100):
            MockDatabaseLayer.insert_thing({'a':i,'b':i % 5},MockDatabaseLayer.dailies)
        count = MockDatabaseLayer.get_count_of_stuff_search({},MockDatabaseLayer.dailies)
        self.assertEqual(count,100)

    def test_filtered_mockdb_count_multi(self):
        for i in range(0,100):
            MockDatabaseLayer.insert_thing({'a':i,'b':i % 5,'c':i %10},MockDatabaseLayer.dailies)
        count = MockDatabaseLayer.get_count_of_stuff_search({'b':1, 'c':1},MockDatabaseLayer.dailies)
        self.assertEqual(count,10)

    def test_filtered_mockdb_count(self):
        for i in range(0,100):
            MockDatabaseLayer.insert_thing({'a':i,'b':i % 5},MockDatabaseLayer.dailies)
        count = MockDatabaseLayer.get_count_of_stuff_search({'b':1},MockDatabaseLayer.dailies)
        self.assertEqual(count,20)

if __name__ == '__main__':
    unittest.main()
