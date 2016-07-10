from BaseModel import BaseModel
import DatabaseLayer


class StoryModels(BaseModel):
  """
    This will be the base class for all of models that are used as parts of 
    other models. Maily, this will refer to Zone and Monster.
  """
  

  @classmethod
  def construct_model_from_pk(cls,pk):
    """
      args:
        id:
          uses the id to load this model from the database.

      return: an instance of the model on which this is called
    """
    
    collection = DatabaseLayer.get_table(cls.get_dbFields().COLLECTION_NAME)
    obj = cls(None)
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
    obj = cls(None)
    obj.dict = dict
    return obj

  def __init__(self,definitionKey):
    """
      args:
        definitionKey:
          a string dictionary key used with one the definition classes. The hashed value
          is a sub-dict that contains the definition info

    """
    super().__init__()
    self._definition = None
    if not definitionKey:
      return
    self.definitionKey = definitionKey
  

