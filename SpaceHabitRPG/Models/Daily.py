from HabitBaseModel import HabitBaseModel
from AllDBFields import DailyDbFields
import DatabaseLayer





class Daily(HabitBaseModel):
  """
    This is a wrapper for the daily data from the database
  """

  @classmethod
  def get_dailies_by_account(cls,accountPk,isCompleted=False):
    collection = DatabaseLayer.get_table(cls.get_dbFields().COLLECTION_NAME)
    return collection.find({cls.get_dbFields().ACCOUNT_PK_KEY:accountPk,'isCompleted':isCompleted})\
      .sort(DailyDbFields.SORT_KEY,1)

  @classmethod
  def get_dbFields(cls):
    return DailyDbFields

  @property
  def name(self):
    return self._dict[DailyDbFields.NAME]

  @name.setter
  def name(self,value):
    self._dict[DailyDbFields.NAME] = value
    self._changes[DailyDbFields.NAME] = value

  @property
  def note(self):
    return self._dict[DailyDbFields.NOTE]

  @note.setter
  def note(self,value):
    self._dict[DailyDbFields.NOTE] = value
    self._changes[DailyDbFields.NOTE] = value

  @property
  def urgency(self):
    return self._dict[DailyDbFields.URGENCY]

  @urgency.setter
  def urgency(self,value):
    self._dict[DailyDbFields.URGENCY] = value
    self._changes[DailyDbFields.URGENCY] = value

  @property
  def difficulty(self):
    return self._dict[DailyDbFields.DIFFICULTY]

  @difficulty.setter
  def difficulty(self,value):
    self._dict[DailyDbFields.DIFFICULTY] = value
    self._changes[DailyDbFields.DIFFICULTY] = value

  @property
  def triggerPeriodLength(self):
    return self._dict[DailyDbFields.TRIGGER_PERIOD_LENGTH]

  @triggerPeriodLength.setter
  def triggerPeriodLength(self,value):
    self._dict[DailyDbFields.TRIGGER_PERIOD_LENGTH] = value
    self._changes[DailyDbFields.TRIGGER_PERIOD_LENGTH] = value

  @property
  def daysUntilTrigger(self):
    return self._dict[DailyDbFields.DAYS_UNTIL_TRIGGER]

  @daysUntilTrigger.setter
  def daysUntilTrigger(self,value):
    self._dict[DailyDbFields.DAYS_UNTIL_TRIGGER] = value
    self._changes[DailyDbFields.DAYS_UNTIL_TRIGGER] = value

  @property
  def activeDays(self):
    return self._dict[DailyDbFields.ACTIVE_DAYS]

  @activeDays.setter
  def activeDays(self,value):
    self._dict[DailyDbFields.ACTIVE_DAYS] = value
    self._changes[DailyDbFields.ACTIVE_DAYS] = value