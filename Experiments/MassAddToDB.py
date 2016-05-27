import DatabaseLayer
import random
from bson.objectid import ObjectId

if __name__ == '__main__':
    testList = []
    for i in range(0,500):
        u = i // 100
        r = (500 -i) // 25
        f = i
        tObj = {'ownerAccountId':ObjectId("57428b8eee2a37797ef5d518"),'daysUntilTrigger':u,'urgency':r,'difficulty':f,'isCompleted':False}
        testList.append(tObj)
    random.shuffle(testList)
    
    for d in testList:
        id = DatabaseLayer.insert_thing(d,"dailies")
        print(id)
    print("done")