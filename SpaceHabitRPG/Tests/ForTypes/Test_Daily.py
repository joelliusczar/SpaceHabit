from SpaceUnitTest import SpaceUnitTest
from Account import COLLECTION_NAME as TABLE_ACCOUNT
from Daily import COLLECTION_NAME as TABLE_DAILIES
import DatabaseLayer
import random


class Test_Daily(SpaceUnitTest):
    
    def setUp(self):
        self.accountCount0 = DatabaseLayer.get_count_of_stuff_search({},TABLE_ACCOUNT)
        self.dailiesCount0 = DatabaseLayer.get_count_of_stuff_search({},TABLE_DAILIES)
        self.accountId = DatabaseLayer.insert_thing({'test':0},TABLE_ACCOUNT)
        testList = []
        self.controlList = []
        for i in range(0,500):
            u = i // 100
            r = (500 -i) // 25
            f = i
            tObj = {'ownerAccountId':self.accountId,'daysUntilTrigger':u,'urgency':r,'difficulty':f,'isCompleted':False}
            testList.append(tObj)
            self.controlList.append(tObj)
        random.shuffle(testList)
    
        for d in testList:
            id = DatabaseLayer.insert_thing(d,TABLE_DAILIES)
            print(id)
        print("done")
        return super().setUp()

    def tearDown(self):
        dailyCollection = DatabaseLayer.get_table(TABLE_DAILIES)
        result = dailyCollection.delete_many( {'ownerAccountId':self.accountId})
        DatabaseLayer.delete_thing_by_key(self.accountId,TABLE_ACCOUNT)
        accountCount1 = DatabaseLayer.get_count_of_stuff_search({},TABLE_ACCOUNT)
        dailiesCount1 = DatabaseLayer.get_count_of_stuff_search({},TABLE_DAILIES)
        self.assertEqual(accountCount1,self.accountCount0)
        self.assertEqual(dailiesCount1,self.dailiesCount0)
        return super().tearDown()


    

    def test_db_daily_sorting(self):
        import Daily
        dailies = Daily.get_dailies_by_account(self.accountId)
        for d,c in zip(dailies,self.controlList):
            self.assertEqual(d['daysUntilTrigger'],c.daysUntilTrigger)
            self.assertEqual(d['urgency'],c.urgency)
            self.assertEqual(d['difficulty'],c.difficulty)

if __name__ == '__main__':
    unittest.main()
