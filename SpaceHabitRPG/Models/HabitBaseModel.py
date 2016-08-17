from BaseModel import BaseModel
import DatabaseLayer



class HabitBaseModel(BaseModel):
  """
    This will be the base class for all of my models. And since my save
    changes is going to use pretty much the same logic in all of my models,
    I'm going to centralize the logic in this base glass. I know that that is
    a frown upon use of inheritance but fuck it.
  """
  
  
  
  

  @classmethod
  def construct_model_from_pk(cls,pk):
    """
      args:
        id:
          uses the id to load this model from the database.

      return: an instance of the model on which this is called
    """
    if not cls.get_dbFields().COLLECTION_NAME:
      raise NotImplementedError("This needs a collection name to work")

    collection = DatabaseLayer.get_table(cls.get_dbFields().COLLECTION_NAME)
    obj = cls()
    obj.dict = collection.find_one({cls.get_dbFields().PK_KEY:pk})
    return obj
    

  @classmethod
  def construct_model_from_dict(cls,dict):
    """
      args:
        dict:
          loads the properties of the model from the dict.

      return: an instance of the model on which this is called

    """
    obj = cls()
    obj.dict = dict
    return obj


  def save_changes(self):

    collection = DatabaseLayer.get_table(self.get_dbFields().COLLECTION_NAME)
    if self.get_pk():
      if self._changes:
        collection.update_one({self.get_dbFields().PK_KEY:self.get_pk()},{'$set':self._changes})
    else:
      pk = collection.insert_one(self.dict).inserted_id
      self.dict[self.get_dbFields().PK_KEY] = pk
    self._changes = {}


