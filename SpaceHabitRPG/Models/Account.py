from HabitBaseModel import HabitBaseModel
from AllDBFields import AccountDbFields
from datetime import datetime
from datetime import timezone
from Daily import Daily
from Hero import Hero
import DatabaseLayer
import uuid








#def get_account_by_userID(userID):
#  dbResults = DatabaseLayer.get_sorted_stuff_by_search(

class Account(HabitBaseModel):
  """
    This is a wrapper for the account data from the database
  """

  @classmethod
  def create_new_account_in_db(cls,loginPk=None):
    account = {
      AccountDbFields.LOGIN_PK_KEY: loginPk,
      AccountDbFields.REMINDER_TIME: -1,
      AccountDbFields.DAY_START:0,
      AccountDbFields.DEATH_GOLD_PENALTY: .25,
      AccountDbFields.HERO_LVL_PENALTY: 0,
      AccountDbFields.ZONE_LVL_PENALTY: "LVLRESTART",
      AccountDbFields.PERMA_DEATH: False,
      AccountDbFields.PUBLIC_ACCOUNT: False,
      AccountDbFields.PUBLIC_KEY: uuid.uuid4().hex,
      AccountDbFields.CREATE_DATE: datetime.utcnow().timestamp(),
      AccountDbFields.PREVENT_POPUPS: False
    }
    collection = DatabaseLayer.get_table(cls.get_dbFields().COLLECTION_NAME)
    pk = collection.insert_one(account).inserted_id
    return pk

  @classmethod
  def get_dbFields(cls):
    return AccountDbFields
      
  @property
  def lastCheckInTime(self):
    if AccountDbFields.LAST_CHECKIN_TIME in self.dict:
      return self.dict[self.get_dbFields().LAST_CHECKIN_TIME]
    return None


  @lastCheckInTime.setter
  def lastCheckInTime(self,value):
    self.dict[self.get_dbFields().LAST_CHECKIN_TIME] = value

  @property
  def preventPopups(self):
    return self.dict[self.get_dbFields().PREVENT_POPUPS]

  @preventPopups.setter
  def preventPopups(self,value):
    self.dict[self.get_dbFields().PREVENT_POPUPS] = value