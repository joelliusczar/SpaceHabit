import ConfigLayer
from pymongo import MongoClient
import DatabaseLayer
import pymongo

COLLECTION_NAME = 'users'
USER_LOGIN = 'login'
USER_PASSWORD = 'pw'
USER_SALT = 'salt'

connection = None

def get_connection():
    return MongoClient(ConfigLayer.get_authentication_server(), int(ConfigLayer.get_port()))

def open_conn():
    global connection
    if connection is None:
        connection = get_connection()

def get_user_collection():
    open_conn()
    db = connection.spacehabit
    return db[COLLECTION_NAME]

def get_user(login):
    return get_user_collection().find_one({USER_LOGIN:login})

def does_login_exist(login):
  if get_user_collection().find({USER_LOGIN:login}).count() > 0:
      return True
  else:
      return False

def insert_user(login,pw,salt):
    id = get_user_collection().insert_one({USER_LOGIN:login,
                                           USER_PASSWORD:pw,
                                           USER_SALT:salt}).inserted_id
    return id