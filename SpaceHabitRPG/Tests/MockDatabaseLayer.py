from UserDBLayer import COLLECTION_NAME as users
from Hero import COLLECTION_NAME as heros
from Account import COLLECTION_NAME as accounts
from Daily import COLLECTION_NAME as dailies
from Good import COLLECTION_NAME as goods
from Habit import COLLECTION_NAME as habits
from Monster import COLLECTION_NAME as monsters
from Todo import COLLECTION_NAME as todos
from Zone import COLLECTION_NAME as zones
import EverywhereConstants




testTables = {
    users: {},
    heros:{},
    accounts:{},
    dailies:{},
    goods:{},
    habits: {},
    todos:{},
    monsters:{},
    zones:{}}



count = 0

def get_table(tablename):
    if tableName not in testTables:
        raise ConnectionError("This is not one of our tables")
    return testTables[tableName]

def insert_thing(stuff, tableName):
    if tableName not in testTables:
        raise ConnectionError("This is not one of our tables")
    global count
    id = tableName + str(count)
    count += 1
    testTables[tableName][id] = stuff
    return id


def get_thing_by_id(id,tableName,returnReference = False):
    table = get_table(tableName)
    if id not in table:
        raise FileNotFoundError("Not a valid key")
    testTables[tableName][id][EverywhereConstants.ID_KEY] = id
    if returnReference:
        return testTables[tableName][id]
    return testTables[tableName][id].copy()


def update_thing_by_id(id,tableName,changes):
    table = get_table(tableName)
    testItem = get_thing_by_id(id,tableName,True)
    for k,v in changes.items():
         testItem[k] = v

def delete_thing_by_key(key,tableName):
    table = get_table(tableName)
    if id not in table:
        raise FileNotFoundError("Not a valid key")
    del collection[id]

def get_user_collection():
    return get_table(users)

def insert_user(login,pw,salt):
    import UserDBLayer
    id = insert_thing({UserDBLayer.USER_LOGIN: login, UserDBLayer.USER_PASSWORD: pw, UserDBLayer.USER_SALT: salt},users)
    return id

def does_login_exist(login):
    import UserDBLayer
    users = get_user_collection()
    for k,v in users.items():
        if v[UserDBLayer.USER_LOGIN] == login:
            return True
    return False

def get_user(login):
    users = get_user_collection()
    for k,v in users.items():
        if v[UserDBLayer.USER_LOGIN] == login:
            return v
    return None
