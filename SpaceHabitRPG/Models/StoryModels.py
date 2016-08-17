from BaseModel import BaseModel
from Defintions import Defintions
import DatabaseLayer



class StoryModels(BaseModel):
  """
    This will be the base class for all of models that are used as parts of 
    other models. Maily, this will refer to Zone and Monster.

    Do not try to use this class directly. Only use its subclasses
  """
  
    

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

  def set_common_story_property(self,key,value):
    """
      I noticed that I was using the same two lines all over my setters.
      So, I decided to just centralize it here.
    """
    self.dict[key] = value
    self._changes[self.get_dbFields().OWNER_PROPERTY + "." +key] = value

