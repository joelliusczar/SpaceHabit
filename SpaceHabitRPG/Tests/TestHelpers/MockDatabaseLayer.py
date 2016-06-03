from UserDBLayer import COLLECTION_NAME as users
from UserDBLayer import USER_LOGIN
from UserDBLayer import USER_PASSWORD
from UserDBLayer import USER_SALT
from Hero import COLLECTION_NAME as heros
from Account import COLLECTION_NAME as accounts
from Daily import COLLECTION_NAME as dailies
from Good import COLLECTION_NAME as goods
from Habit import COLLECTION_NAME as habits
from Monster import COLLECTION_NAME as monsters
from Todo import COLLECTION_NAME as todos
from Zone import COLLECTION_NAME as zones
import EverywhereConstants
from Heap import Heap
import TestFunctionBuilder




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

def clean_up():
    global count
    count = 0
    for k,v in testTables.items():
        v = {}

def get_table(tableName):
    if tableName not in testTables:
        raise ConnectionError("This is not one of our tables")
    return testTables[tableName]

def insert_thing(stuff, tableName):
    table = get_table(tableName)
    global count
    id = tableName + str(count)
    count += 1
    table[id] = stuff.copy()
    return id


def get_thing_by_id(id,tableName,returnReference = False):
    table = get_table(tableName)
    if id not in table:
        return None
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
    del table[key]

def get_user_collection():
    return get_table(users)

def insert_user(login,pw,salt):
    id = insert_thing({USER_LOGIN: login, USER_PASSWORD: pw, USER_SALT: salt},users)
    return id

def does_login_exist(login):
    users = get_user_collection()
    for k,v in users.items():
        if v[USER_LOGIN] == login:
            return True
    return False

def get_user(login):
    users = get_user_collection()
    for k,v in users.items():
        if v[USER_LOGIN] == login:
            return v
    return None


def get_sorted_stuff_by_key(seachFor,tableName,sortByList):
    table = get_table(tableName)
    heap = Heap(TestFunctionBuilder.build_sort_by_function(sortByList,table))
    for k,nestedDict in table.items():
        isMatch = True
        for e,a in seachFor.items():
            if not e in nestedDict or nestedDict[e] != a:
                isMatch = False
                break
        if isMatch:
            heap.push(nestedDict)
    return heap.get_sorted_list()