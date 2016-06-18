import DatabaseLayer


class GoodsFields:
  COLLECTION_NAME = 'goods'
  ID_KEY = '_id'
  NAME = 'name'
  NOTE = 'note'
  COST = 'cost'
  TYPE = 'type'
  SPECIAL = 'special'
  PUBLIC_KEY = 'PublicKey'


class Good(object):
  """a class to model a good which is an item that can be purchased in game"""
  def __init__(self,dict=None,id = None):
    """Priority is given to dictionary object over id """
    self._changes = {}
    if dict:
      self._dict = dict
      return
    if id:
      self._dict = DatabaseLayer.get_thing_by_id(id,GoodsFields.COLLECTION_NAME)
      return
    raise ValueError("Either a reference to a dictionary or an id is required")


  def save_changes(self):
    DatabaseLayer.update_thing_by_id(self.id,GoodsFields.COLLECTION_NAME,self._changes)
    self._changes = {}

  @property
  def id(self):
    return self._dict[GoodsFieldsID_KEY]

  @property
  def name(self):
    return self._dict[GoodsFields.NAME]

  @name.setter
  def name(self,value):
    self._dict[GoodsFields.NAME] = value
    self._changes[GoodsFields.NAME] = value

  @property
  def note(self):
    return self._dict[GoodsFields.NOTE]

  @note.setter
  def note(self,value):
    self._dict[GoodsFields.NOTE] = value
    self._changes[GoodsFields.NOTE] = value

  @property
  def cost(self):
    return self._dict[GoodsFields.COST]

  @cost.setter
  def cost(self,value):
    self._dict[GoodsFields.COST] = value
    self._changes[GoodsFields.COST] = value

  @property
  def type(self):
    return self._dict[GoodsFields.TYPE]

  @type.setter
  def type(self,value):
    self._dict[GoodsFields.TYPE] = value
    self._changes[GoodsFields.TYPE] = value

  @property
  def special(self):
    return self._dict[GoodsFields.SPECIAL]

  @special.setter
  def special(self,value):
    self._dict[GoodsFields.SPECIAL] = value
    self._changes[GoodsFields.SPECIAL] = value