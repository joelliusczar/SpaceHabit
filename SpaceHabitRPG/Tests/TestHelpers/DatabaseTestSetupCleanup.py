"""
  This module is for inserting test data into the database and for cleaning up
  the test data so that it doesn't get in the way of other tests
"""

from AuthenticationLayer import AuthenticationFields as fields
import DatabaseLayer
import CryptKeeper

def clean_up():
  """
    remove all the data from the test database
  """
  connection = DatabaseLayer.open_conn()
  connection.drop_database("spacetest")

def insert_one_user():
  collection = DatabaseLayer.get_table(fields.COLLECTION_NAME)
  id = collection.insert_one({fields.USER_LOGIN:"a@b.c",fields.USER_DESC: 
    "a@b.c",fields.USER_PASSWORD:CryptKeeper.encrypt_str("123456")}).inserted_id
  return id