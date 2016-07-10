"""
  This is a wrapper for interaction with the database. Each of these methods
  can be overridden to connect to a different db.
"""
from pymongo import MongoClient
import ConfigLayer
import pymongo


connection = None
isUnitTestMode = False

def open_conn():
  """
    Checks if there is already an open db connection. If not then it opens
    one. Either way, it returns the open db connection.
  """
  global connection
  if connection is None:
    connection = MongoClient(ConfigLayer.get_url(), int(ConfigLayer.get_port()))
  return connection


def get_table(tableName):
  """
    gets the dataset associated with the given name. Also checks if the
    connection to the database is open or not. If it is not, then open it.

    args:
      tableName: 
        name of the dataset that is wanted by the caller

    returns:
      a dataset upon which futher inquries can be done.
  """
  global isUnitTestMode
  open_conn()
  if isUnitTestMode:
    db = connection['test']
  else:
    db = connection[ConfigLayer.get_db_name()]
  return db[tableName]


