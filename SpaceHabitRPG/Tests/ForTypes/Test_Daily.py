from SpaceUnitTest import SpaceUnitTest
from Account  import AccountDbFields
from Daily import DailyDbFields
import DatabaseLayer
import random

TABLE_ACCOUNT = AccountDbFields.COLLECTION_NAME
TABLE_DAILIES = DailyDbFields.COLLECTION_NAME

class Test_Daily(SpaceUnitTest):
  
  def setUp(self):
    accountSet = DatabaseLayer.get_table(TABLE_ACCOUNT)
    dailySet = DatabaseLayer.get_table(TABLE_DAILIES)
    self.accountCount0 = accountSet.find({}).count()
    self.dailiesCount0 = dailySet.find({}).count()
    self.accountId = accountSet.insert_one({'test':0}).inserted_id
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
      id = dailySet.insert_one(d).inserted_id
      print(id)
    print("done")
    return super().setUp()

  def tearDown(self):
    accountSet = DatabaseLayer.get_table(TABLE_ACCOUNT)
    dailySet = DatabaseLayer.get_table(TABLE_DAILIES)
    result = dailySet.delete_many( {'ownerAccountId':self.accountId})
    accountSet.delete_one({'_id':self.accountId})
    accountCount1 = accountSet.find({}).count()
    dailiesCount1 = dailySet.find({}).count()
    self.assertEqual(accountCount1,self.accountCount0)
    self.assertEqual(dailiesCount1,self.dailiesCount0)
    return super().tearDown()


  

  def test_db_daily_sorting(self):
    from Daily import Daily
    dailies = Daily.get_dailies_by_account(self.accountId)
    for d,c in zip(dailies,self.controlList):
      self.assertEqual(d['daysUntilTrigger'],c.daysUntilTrigger)
      self.assertEqual(d['urgency'],c.urgency)
      self.assertEqual(d['difficulty'],c.difficulty)

if __name__ == '__main__':
  unittest.main()
