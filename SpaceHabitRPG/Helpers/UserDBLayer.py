import ConfigLayer
from pymongo import MongoClient
import DatabaseLayer
import pymongo

COLLECTION_NAME = 'users'
USER_LOGIN = 'login'
USER_PASSWORD = 'pw'
USER_SALT = 'salt'
USER_DESC = 'desc'

connection = None

def get_connection():
    """
        wrappper around the opening of the connection to the db
    """
    return MongoClient(ConfigLayer.get_authentication_server(), int(ConfigLayer.get_port()))


def open_conn():
    """
        Checks if there is already an open db connection. If not then it opens
        one. Either way, it returns the open db connection.
    """
    global connection
    if connection is None:
        connection = get_connection()


def get_user_collection():
    open_conn()
    db = connection.spacehabit
    return db[COLLECTION_NAME]

def get_user(login):
    return get_user_collection().find_one({USER_LOGIN:login.lower()})

def does_login_exist(login):
  if get_user_collection().find({USER_LOGIN:login.lower()}).count() > 0:
      return True
  else:
      return False

def insert_user(login,pw):
    id = get_user_collection().insert_one({USER_LOGIN:login.lower(),
                                           USER_PASSWORD:pw,
                                           USER_DESC: login}).inserted_id
    return id