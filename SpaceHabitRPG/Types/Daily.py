import DatabaseLayer


class DailyFields:
  COLLECTION_NAME = 'dailies'
  ID_KEY = '_id'
  NAME = 'name'
  NOTE = 'note'
  URGENCY = 'urgency'
  DIFFICULTY = 'difficulty'
  TRIGGER_PERIOD_LENGTH = 'triggerPeriodLength'
  DAYS_UNTIL_TRIGGER = 'daysUntilTrigger'
  SORT_KEY = 'sortKey'
  ACTIVE_DAYS = 'activeDays'
  PUBLIC_KEY = 'PublicKey'

def get_dailies_by_account(id,isCompleted=False):
  collection = DatabaseLayer.get_table(DailyFields.COLLECTION_NAME)
  return collection.find({DailyFields.ID_KEY:id,'isCompleted':isCompleted})\
    .sort(DailyFields.SORT_KEY,1)

class Daily(object):
  """description of class"""
  def __init__(self,dict=None,id = None):
    """Priority is given to dictionary object over id """
    self._changes = {}
    if dict:
      self._dict = dict
      return
    if id:
      collection = DatabaseLayer.get_table(DailyFields.COLLECTION_NAME)
      self._dict = collection.find_one({DailyFields.ID_KEY:id})
      return
    raise ValueError("Either a reference to a dictionary or an id is required")


  def save_changes(self):
    collection = DatabaseLayer.get_table(DailyFields.COLLECTION_NAME)
    collection.update_one({DailyFields.ID_KEY:self.id},self._changes)
    self._changes = {}

  @property
  def id(self):
    return self._dict[DailyFields.ID_KEY]

  @property
  def name(self):
    return self._dict[DailyFields.NAME]

  @name.setter
  def name(self,value):
    self._dict[DailyFields.NAME] = value
    self._changes[DailyFields.NAME] = value

  @property
  def note(self):
    return self._dict[DailyFields.NOTE]

  @note.setter
  def note(self,value):
    self._dict[DailyFields.NOTE] = value
    self._changes[DailyFields.NOTE] = value

  @property
  def urgency(self):
    return self._dict[DailyFields.URGENCY]

  @urgency.setter
  def urgency(self,value):
    self._dict[DailyFields.URGENCY] = value
    self._changes[DailyFields.URGENCY] = value

  @property
  def difficulty(self):
    return self._dict[DailyFields.DIFFICULTY]

  @difficulty.setter
  def difficulty(self,value):
    self._dict[DailyFields.DIFFICULTY] = value
    self._changes[DailyFields.DIFFICULTY] = value

  @property
  def triggerPeriodLength(self):
    return self._dict[DailyFields.TRIGGER_PERIOD_LENGTH]

  @triggerPeriodLength.setter
  def triggerPeriodLength(self,value):
    self._dict[DailyFields.TRIGGER_PERIOD_LENGTH] = value
    self._changes[DailyFields.TRIGGER_PERIOD_LENGTH] = value

  @property
  def daysUntilTrigger(self):
    return self._dict[DailyFields.DAYS_UNTIL_TRIGGER]

  @daysUntilTrigger.setter
  def daysUntilTrigger(self,value):
    self._dict[DailyFields.DAYS_UNTIL_TRIGGER] = value
    self._changes[DailyFields.DAYS_UNTIL_TRIGGER] = value

  @property
  def activeDays(self):
    return self._dict[DailyFields.ACTIVE_DAYS]

  @activeDays.setter
  def activeDays(self,value):
    self._dict[DailyFields.ACTIVE_DAYS] = value
    self._changes[DailyFields.ACTIVE_DAYS] = value