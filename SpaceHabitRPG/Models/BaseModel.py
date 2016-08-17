from AllDBFields import BaseFields

class BaseModel(object):

  @classmethod
  def get_dbFields(cls):
    return BaseFields

  def __init__(self):
    self._changes = {}
    self.dict = {}

  def get_pk(self):
    if not self.get_dbFields().PK_KEY in self.dict:
      return None
    return self.dict[self.get_dbFields().PK_KEY]

  def set_common_property(self,key,value):
    """
      I noticed that I was using the same two lines all over my setters.
      So, I decided to just centralize it here.
    """
    self.dict[key] = value
    self._changes[key] = value