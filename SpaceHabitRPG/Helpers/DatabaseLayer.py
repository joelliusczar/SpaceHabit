import ConfigLayer
from pymongo import MongoClient
import pymongo

conn = None

def open_conn():
    global conn
    conn = MongoClient(ConfigLayer.get_url(), int(ConfigLayer.get_port()))
    


def get_open_connection():
    if conn is None:
        open_conn()
    return conn


def get_table(tablename):
    if conn is None:
        open_conn()
    db = conn.spacehabit
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

def get_dailies_by_account(id,isCompleted=False):
    collection = get_table("dailies")
    return collection.find({'ownerAccountId':id}, {'isCompleted':isCompleted}).sort([
        ('daysUntilTrigger',pymongo.ASCENDING),
        ('urgency',pymongo.DESCENDING),
        ('difficulty',pymongo.ASCENDING)])

def get_habits_by_account(id):
    collection = get_table("habits")
    return collection.find({'ownerAccountId':id}).sort([
        ('triggerFrequency',pymongo.DESCENDING)])

def get_todos_by_account(id):
    collection = get_table("todos")
    return collection.find({'ownerAccountId':id}).sort([
        ('dueDate',pymongo.ASCENDING),
        ('urgency',pymongo.DESCENDING),
        ('difficulty',pymongo.ASCENDING)
        ('effectiveDate',pymongo.ASCENDING)])