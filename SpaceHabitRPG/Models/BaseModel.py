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