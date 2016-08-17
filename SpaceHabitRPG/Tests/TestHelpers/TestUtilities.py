"""
  Just a bunch of(or a few) methods to help with unit testing.
"""
import DatabaseLayer

def get_record_count_from_table(tableName):
  """
    this will usually be used to count how many records were inserted into the
    database

    args:
      tableName:
        the name of the table that we want to count records from

      returns:
        the record count in our collection of interest
  """
  collection = DatabaseLayer.get_table(tableName)
  return collection.find({}).count()