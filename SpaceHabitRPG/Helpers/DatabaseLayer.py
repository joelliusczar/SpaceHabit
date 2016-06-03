import ConfigLayer
from pymongo import MongoClient
import pymongo



connection = None

def get_open_connection():
    return MongoClient(ConfigLayer.get_url(), int(ConfigLayer.get_port()))
    

def open_conn():
    global connection
    if connection is None:
        connection = get_open_connection()
    return connection



def get_table(tablename):
    open_conn()
    db = connection.spacehabit
    return db[tablename]

def get_thing_by_id(id,tableName):
    collection = get_table(tableName)
    return collection.find_one({'_id':id})

def insert_thing(stuff, tableName):
    collection = get_table(tableName)
    id = collection.insert_one(stuff).inserted_id
    return id

def update_thing_by_id(id,tableName,changes):
    collection = get_table(tableName)
    collection.update(
            {'_id': id},
            {
            '$set': changes,    
            }
        )


def delete_thing_by_key(key,tableName):
    collection = get_table(tableName)
    collection.remove({'_id':key})

def get_sorted_stuff_by_key(seachForDict,tableName,sortByList):
    collection = get_table(tableName)
    return collection.find(seachForDict).sort(sortByList)
