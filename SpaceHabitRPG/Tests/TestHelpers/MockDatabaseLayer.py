"""
    This is basically an in-memory database that is used for the unit tests
    and gets wiped when the tests are finished.
"""


from UserDBLayer import COLLECTION_NAME as TABLE_USER
from UserDBLayer import USER_LOGIN
from UserDBLayer import USER_PASSWORD
from UserDBLayer import USER_DESC
from Hero import COLLECTION_NAME as TABLE_HEROS
from Account import COLLECTION_NAME as TABLE_ACCOUNTS
from Daily import COLLECTION_NAME as TABLE_DAILIES
from Good import COLLECTION_NAME as TABLE_GOODS
from Habit import COLLECTION_NAME as TABLE_HABITS
from Monster import COLLECTION_NAME as TABLE_MONSTERS
from Todo import COLLECTION_NAME as TABLE_TODOS
from Zone import COLLECTION_NAME as TABLE_ZONES
from Heap import Heap
import TestFunctionBuilder
import EverywhereConstants




testTables = {
    TABLE_USER: {},
    TABLE_HEROS:{},
    TABLE_ACCOUNTS:{},
    TABLE_DAILIES:{},
    TABLE_GOODS:{},
    TABLE_HABITS: {},
    TABLE_TODOS:{},
    TABLE_MONSTERS:{},
    TABLE_ZONES:{}}


#this is used to keep Ids unique
count = 0

def clean_up():
    """
        set all of the dicts substituting for tables to empty dicts
        and set count to 0 so that ids start from there and so
        that it doesn't fuck with my unit tests that are dependant upon a
        certain order
    """
    global count
    count = 0
    for k,v in testTables.items():
        v = {}

def get_table(tableName):
    """
        gets the mock dataset associated with the given name.

        args:
            tableName: 
                name of the dataset that is wanted by the caller

        returns:
            a dict that itself contains a bunch of dicts
    """
    if tableName not in testTables:
        raise ConnectionError("This is not one of our tables")
    return testTables[tableName]

def insert_thing(stuff, tableName):
    """
        insert things into out mock database

        args:
            stuff: 
                this will be a dict. Ideally this will have most of the
                same properties that the rest of the items in this dataset has.
            tableName: 
                this is the name of the dataset that we're inserting
                our item into.

        returns:
            the mock primary key of the newly inserted item. It will be of the
            form: tableName + num, e.g. test0, hero7, etc.
    """
    table = get_table(tableName)
    global count
    id = tableName + str(count)
    count += 1
    table[id] = stuff.copy()
    return id


def get_thing_by_id(id,tableName,returnReference = False):
    """
        This is a wrapper method to get a single item from the mock database 
        that is associated with the given id.

        args:
            id: 
                this is a primary key for an item in the database
            tableName: 
                this is the name of the dataset that is expected to have
                the item we're looking for.
            returnReference:
                a boolean that determines if method returns a reference to the
                dict or a copy of it.

        returns:
            a dict with an _id field that matches id
    """
    table = get_table(tableName)
    if id not in table:
        return None
    testTables[tableName][id][EverywhereConstants.ID_KEY] = id
    if returnReference:
        return testTables[tableName][id]
    return testTables[tableName][id].copy()


def update_thing_by_id(id,tableName,changes):
    """
        This is a wrapper method for updating a single item in our mock db.

        args:
            id: 
                this is a primary key for an item in the database
            tableName: 
                this is the name of the dataset that is expected to have
                the item we're looking for.
            changes: 
                this will be a dict. Each field in this dict will have a value
                that overwrites the old value for that field for that item
                in the db
    """
    table = get_table(tableName)
    testItem = get_thing_by_id(id,tableName,True)
    for k,v in changes.items():
         testItem[k] = v


def delete_thing_by_key(key,tableName):
    """
        Removes a particular item from the mock database

        args:
            key:
                primary key of the item that we want to remove from the db
            tableName:
                name of the dataSet that has the item that we want to remove
    """
    table = get_table(tableName)
    del table[key]

def get_user_collection():
    return get_table(TABLE_USER)

def insert_user(login,pw):
    id = insert_thing({USER_LOGIN: login.lower(), USER_PASSWORD: pw,USER_DESC:login},TABLE_USER)
    return id

def does_login_exist(login):
    lowerLogin = login.lower()
    TABLE_USER = get_user_collection()
    for k,v in TABLE_USER.items():
        if v[USER_LOGIN] == lowerLogin:
            return True
    return False

def get_user(login):
    lowerLogin = login.lower()
    TABLE_USER = get_user_collection()
    for k,v in TABLE_USER.items():
        if v[USER_LOGIN] == lowerLogin:
            return v
    return None


def get_sorted_stuff_by_key(searchFor,tableName,sortByList):
    table = get_table(tableName)
    heap = Heap(TestFunctionBuilder.build_sort_by_function(sortByList,table))
    for k,nestedDict in table.items():
        isMatch = True
        for e,a in searchFor.items():
            if not e in nestedDict or nestedDict[e] != a:
                isMatch = False
                break
        if isMatch:
            heap.push(nestedDict)
    return heap.get_sorted_list()

def get_count_of_stuff_search(searchFor,tableName):
    table = get_table(tableName)
    count = 0
    for k,nestedDict in table.items():
        isMatch = True
        for e,a in searchFor.items():
            if not e in nestedDict or nestedDict[e] != a:
                isMatch = False
                break
        if isMatch:
            count += 1
    return count