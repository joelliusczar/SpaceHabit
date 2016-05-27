
testHeros = {'dirkdigglerkey':
             {
            '_id':"notalameid",
            'name': "Dirk Diggler",
            'shipName': "USS Kickass!",
            'lvl':1,
            'gold':0,
            'maxHp': 100,
            'nowHp': 100,
            'maxXp': 50,
            'nowXp': 0,
            'attackLvl': 1,
            'defenseLvl': 1,           
        }}

testTables = {'heros':testHeros,
              'accounts':{},
              'dailies':{},
               'habits':{},
               'todos':{},
               'goods':{},
               'monsters':{},
               'zones':{}}



count = 0

def insert_thing(stuff, tableName):
    if tableName not in testTables:
        raise ConnectionError("This is not one of our tables")
    global count
    id = tableName + str(count)
    count += 1
    testTables[tableName][id] = stuff
    return id


def get_thing_by_id(id,tableName,returnReference = False):
    if tableName not in testTables:
        raise ConnectionError("This is not one of our tables")
    if id not in testTables[tableName]:
        raise FileNotFoundError("Not a valid key")
    testTables[tableName][id]['_id'] = id
    if returnReference:
        return testTables[tableName][id]
    return testTables[tableName][id].copy()


def update_thing_by_id(id,tableName,changes):
    if tableName not in testTables:
        raise ConnectionError("This is not one of our tables")
    if id not in testTables[tableName]:
        raise FileNotFoundError("Not a valid key")
    testItem = get_thing_by_id(id,tableName,True)
    for k,v in changes.items():
         testItem[k] = v