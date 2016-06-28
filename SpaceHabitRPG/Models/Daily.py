from HabitBaseModel import HabitBaseModel
import DatabaseLayer


class DailyFields:
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
  collection = DatabaseLayer.get_table(Daily.COLLECTION_NAME)
  return collection.find({Daily.ID_KEY:id,'isCompleted':isCompleted})\
    .sort(DailyFields.SORT_KEY,1)

class Daily(HabitBaseModel):
  """
    This is a wrapper for the daily data from the database
  """

  COLLECTION_NAME = 'dailies'

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
    super().__init__(dict =dict,id =id)


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