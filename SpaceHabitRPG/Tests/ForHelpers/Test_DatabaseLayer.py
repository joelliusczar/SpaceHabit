from SpaceUnitTest import SpaceUnitTest
from bson.objectid import ObjectId
from Account import COLLECTION_NAME as accounts
from Daily import COLLECTION_NAME as dailiesName
import random
import DatabaseLayer

class Test_Test_DatabaseLayer(SpaceUnitTest):
    def setUp(self):
        self.accountCount0 = DatabaseLayer.get_count_of_stuff_search({},accounts)
        self.dailiesCount0 = DatabaseLayer.get_count_of_stuff_search({},dailiesName)
        self.accountId = DatabaseLayer.insert_thing({'test':0},accounts)
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
            id = DatabaseLayer.insert_thing(d,dailiesName)
            print(id)
        print("done")
        return super().setUp()

    def tearDown(self):
        dailyCollection = DatabaseLayer.get_table(dailiesName)
        result = dailyCollection.delete_many( {'ownerAccountId':self.accountId})
        DatabaseLayer.delete_thing_by_key(self.accountId,accounts)
        accountCount1 = DatabaseLayer.get_count_of_stuff_search({},accounts)
        dailiesCount1 = DatabaseLayer.get_count_of_stuff_search({},dailiesName)
        self.assertEqual(accountCount1,self.accountCount0)
        self.assertEqual(dailiesCount1,self.dailiesCount0)
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
