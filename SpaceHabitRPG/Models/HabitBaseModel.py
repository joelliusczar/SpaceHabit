import DatabaseLayer

class HabitBaseModel(object):
  """
    This will be the base class for all of my models. And since my save
    changes is going to use pretty much the same logic in all of my models,
    I'm going to centralize the logic in this base glass. I know that that is
    a frown upon use of inheritance but fuck it.
  """
  
  COLLECTION_NAME = None
  ID_KEY = '_id'
  _changes = {}
  _dict = {}


  def __init__(self,dict=None,id = None):
    """
      args:
        dict:
          loads the properties of the model from the dict.
        id:
          uses the id to load this model from the database.
          If both a dict and id are supplied, the dict is used and the id is 
          ignored. 
          If nether are supplied then the model is empty

    """
    
    if dict:
      self._dict = dict
      return
    if id:
      collection = DatabaseLayer.get_table(self.COLLECTION_NAME)
      self._dict = collection.find_one({self.ID_KEY:id})
      return
    self._dict = {}

  def save_changes(self):
    collection = DatabaseLayer.get_table(self.COLLECTION_NAME)
    if self.ID_KEY in self._dict:
      collection.update_one({self.ID_KEY:self.id},{'$set':self._changes})
    else:
      id = collection.insert_one(self._dict).inserted_id
      self._dict[self.ID_KEY] = id
    self._changes = {}


