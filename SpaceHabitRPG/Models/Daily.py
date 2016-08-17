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
    self.set_common_property(self.get_dbFields().NAME,value)

  @property
  def note(self):
    return self._dict[DailyDbFields.NOTE]

  @note.setter
  def note(self,value):
    self.set_common_property(self.get_dbFields().NOTE,value)

  @property
  def urgency(self):
    return self._dict[DailyDbFields.URGENCY]

  @urgency.setter
  def urgency(self,value):
    self.set_common_property(self.get_dbFields().URGENCY,value)

  @property
  def difficulty(self):
    return self._dict[DailyDbFields.DIFFICULTY]

  @difficulty.setter
  def difficulty(self,value):
    self.set_common_property(self.get_dbFields().DIFFICULTY,value)

  @property
  def triggerPeriodLength(self):
    return self._dict[DailyDbFields.TRIGGER_PERIOD_LENGTH]

  @triggerPeriodLength.setter
  def triggerPeriodLength(self,value):
    self.set_common_property(self.get_dbFields().TRIGGER_PERIOD_LENGTH,value)

  @property
  def daysUntilTrigger(self):
    return self._dict[DailyDbFields.DAYS_UNTIL_TRIGGER]

  @daysUntilTrigger.setter
  def daysUntilTrigger(self,value):
    self.set_common_property(self.get_dbFields().DAYS_UNTIL_TRIGGER,value)

  @property
  def activeDays(self):
    return self._dict[DailyDbFields.ACTIVE_DAYS]

  @activeDays.setter
  def activeDays(self,value):
    self.set_common_property(self.get_dbFields().ACTIVE_DAYS,value)